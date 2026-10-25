<?php
// Stubbed-WordPress tests for v1.5.x: device menu (section ids, menu links) and the service page content filter.
// Run: php instatech/wp/tests/harness-v15.php instatech/wp/mu-plugins/instatech-seo-fixes.php <dir>
// <dir> holds <slug>.raw.html for the four hubs (server HTML) and itm.js (the decoded inline menu script).
// Writes the footer script to <dir>/itm-fix.js for the browser test.
define( 'ABSPATH', '/x/' );
define( 'OBJECT', 'OBJECT' );
$LIVE = true; $PAGE = null;
$F = array();
function add_filter( $h, $cb ) { global $F; $F[ $h ][] = $cb; }
function add_action() {}
function wp_json_encode( $v ) { return json_encode( $v, JSON_UNESCAPED_SLASHES ); }
function get_page_by_path( $p ) { global $LIVE; return $LIVE ? (object) array( 'post_status' => 'publish' ) : null; }
function is_page( $s = null ) { global $PAGE; return null !== $PAGE; }
function get_queried_object() { global $PAGE; return $PAGE; }
require $argv[1];
$dir = $argv[2];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }

// Menu links: apply the footer script's map to the menu data; every link must resolve to a page or a hub section id.
$js   = file_get_contents( "$dir/itm.js" );
$map  = instatech_seo_device_menu_links();
$out  = strtr( $js, array_combine( array_map( function ( $k ) { return "'$k'"; }, array_keys( $map ) ), array_map( function ( $v ) { return "'$v'"; }, $map ) ) );
check( 'menu: battery repointed to the live page', false !== strpos( $out, "'/mobile-repair-services/battery-replacement/'" ) && false === strpos( $out, "'/mobile-repair-services/#battery'" ) );
check( 'menu: laptop power, water and case go to #diagnostic', 3 === substr_count( $out, "'/laptop-desktop-repair/#diagnostic'" ) );
$script = instatech_seo_device_menu_script();
check( 'footer script: device buttons navigate to hubs', false !== strpos( $script, 'location.href=H[k]' ) && false !== strpos( $script, '"/smartwatch-repair-service/"' ) );
file_put_contents( "$dir/itm-fix.js", $script );
$LIVE = false;
check( 'menu: section links kept while the pages are not live', array() === instatech_seo_section_pages() && ! isset( instatech_seo_device_menu_links()['/mobile-repair-services/#battery'] ) );
$LIVE = true;

preg_match_all( "#'/([a-z-]+)/\\#([a-z]+)'#", $out, $links, PREG_SET_ORDER );
check( 'menu: charging and water point at their pages once live', false !== strpos( $out, "'/mobile-repair-services/charging-port-repair/'" ) && false !== strpos( $out, "'/mobile-repair-services/water-damage-repair/'" ) );
check( 'menu: 23 hash links remain', 23 === count( $links ) );
$pages = array();
foreach ( $links as $l ) {
	if ( ! isset( $pages[ $l[1] ] ) ) {
		$PAGE = (object) array( 'post_name' => $l[1], 'post_parent' => 0 );
		$in   = file_get_contents( "$dir/{$l[1]}.raw.html" );
		$pages[ $l[1] ] = instatech_seo_device_menu( $in );
		check( "{$l[1]}: idempotent", $pages[ $l[1] ] === instatech_seo_device_menu( $pages[ $l[1] ] ) );
		check( "{$l[1]}: visible text unchanged", strip_tags( $pages[ $l[1] ] ) === strip_tags( $in ) );
	}
	check( "/{$l[1]}/#{$l[2]} lands on a section", 1 === substr_count( $pages[ $l[1] ], ' id="' . $l[2] . '"' ) );
}
$PAGE = (object) array( 'post_name' => 'tablet-repairs', 'post_parent' => 75806 );
$in = file_get_contents( "$dir/tablet-repairs.raw.html" );
check( 'child pages untouched', instatech_seo_device_menu( $in ) === $in );
// Service page content: battery step label restored, links to hub sections moved to the new pages.
// The live page lost its backslashes on insert, so the test input does too.
$broken = stripslashes( file_get_contents( __DIR__ . '/../../pages/battery-replacement.block.html' ) );
$filter = end( $F['the_content'] );
$fixed  = $filter( $broken );
check( 'battery page: step label separator restored', false !== strpos( $fixed, "' of 4 \\u00b7 '" ) && false === strpos( $fixed, "of 4 u00b7" ) );
check( 'battery page: related links move to the new pages', false !== strpos( $fixed, 'href="/mobile-repair-services/charging-port-repair/"' ) && false !== strpos( $fixed, 'href="/mobile-repair-services/water-damage-repair/"' ) );
check( 'battery page: filter idempotent', $fixed === $filter( $fixed ) );
check( 'other content untouched', '<p>x</p>' === $filter( '<p>x</p>' ) );
$LIVE = false;
check( 'battery page: hub links kept while the new pages are not live', false !== strpos( $filter( $broken ), 'href="/mobile-repair-services/#charging"' ) );
$LIVE = true;
echo $fail ? "$fail FAILED\n" : "ALL PASS\n";
exit( $fail ? 1 : 0 );
