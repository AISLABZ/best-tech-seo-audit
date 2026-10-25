<?php
// Stubbed-WordPress tests for v1.5.0 device menu: section ids on the four hubs and the menu script rewrite.
// Run: php instatech/wp/tests/harness-v15.php instatech/wp/mu-plugins/instatech-seo-fixes.php <dir>
// <dir> holds <slug>.raw.html for the four hubs (server HTML) and itm.js (the decoded inline menu script).
define( 'ABSPATH', '/x/' );
define( 'OBJECT', 'OBJECT' );
$LIVE = true; $PAGE = null;
function add_filter() {}
function add_action() {}
function get_page_by_path( $p ) { global $LIVE; return $LIVE ? (object) array( 'post_status' => 'publish' ) : null; }
function is_page( $s = null ) { global $PAGE; return null !== $PAGE; }
function get_queried_object() { global $PAGE; return $PAGE; }
require $argv[1];
$dir = $argv[2];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }

// Menu script: every problem link must resolve to a real page or to an id the hub now has.
$js  = file_get_contents( "$dir/itm.js" );
$doc = '<script>' . $js . '</script>';
$out = instatech_seo_device_menu( $doc );
check( 'menu: battery repointed to the live page', false !== strpos( $out, "'/mobile-repair-services/battery-replacement/'" ) && false === strpos( $out, "'/mobile-repair-services/#battery'" ) );
check( 'menu: laptop power, water and case go to #diagnostic', 3 === substr_count( $out, "'/laptop-desktop-repair/#diagnostic'" ) );
check( 'menu: device buttons navigate', false !== strpos( $out, 'location.href=D[i].hub' ) );
check( 'menu: idempotent', $out === instatech_seo_device_menu( $out ) );
file_put_contents( sys_get_temp_dir() . '/itm-v15.js', substr( $out, 8, -9 ) );
$LIVE = false;
check( 'menu: battery link kept when the page is not live', false !== strpos( instatech_seo_device_menu( $doc ), "'/mobile-repair-services/#battery'" ) );
$LIVE = true;

preg_match_all( "#'/([a-z-]+)/\\#([a-z]+)'#", $out, $links, PREG_SET_ORDER );
check( 'menu: 25 hash links remain', 25 === count( $links ) );
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
echo $fail ? "$fail FAILED\n" : "ALL PASS\n";
exit( $fail ? 1 : 0 );
