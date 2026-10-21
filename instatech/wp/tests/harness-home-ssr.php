<?php
// Tests for instatech-home-ssr.php against a saved raw homepage.
// Run: php instatech/wp/tests/harness-home-ssr.php instatech/wp/mu-plugins/instatech-home-ssr.php <home-raw.html>
define( 'ABSPATH', '/x/' );
function add_action( $h, $cb, $p = 10 ) {}
require $argv[1];
$raw = file_get_contents( $argv[2] );

$fail = 0;
function check( $l, $c ) { global $fail; echo ( $c ? 'PASS ' : 'FAIL ' ), $l, "\n"; if ( ! $c ) { $fail++; } }
$ids = array( 'tiles', 'cats', 'audio', 'chargers', 'rvgrid' );
$filled = function ( $h ) use ( $ids ) { $n = 0; foreach ( $ids as $i ) { if ( false === strpos( $h, 'id="' . $i . '"></div>' ) && false !== strpos( $h, 'id="' . $i . '">' ) ) { $n++; } } return $n; };

$out = instatech_home_ssr( $raw );
check( 'live HTML: all 5 sections server-rendered', 5 === $filled( $out ) );
check( 'live HTML: product links now in server HTML', false !== strpos( $out, 'href="https://instatech.uk/product/h1-stereo-wireless-headphones/"' ) && false !== strpos( $out, 'href="https://instatech.uk/product-category/cables/"' ) );
check( 'live HTML: device tiles and reviews present', false !== strpos( $out, 'Book now' ) && false !== strpos( $out, 'Verified Google review' ) );

$pre = str_replace( '<iframe data-lazyloaded="1" src="about:blank" data-src="\'+REPAIRDESK_URL+\'"', '<iframe src="\'+REPAIRDESK_URL+\'"', $raw );
check( 'pre-LiteSpeed HTML (what the plugin sees): fingerprint still matches', $pre !== $raw && 5 === $filled( instatech_home_ssr( $pre ) ) );

$edited = str_replace( "['Charging Cables','Lightning, USB-C, braided XL'", "['Charging Cables','Lightning, USB-C, braided XXL'", $raw );
check( 'edited homepage script: steps aside, page unchanged', $edited !== $raw && $edited === instatech_home_ssr( $edited ) );

check( 'idempotent: second pass changes nothing', $out === instatech_home_ssr( $out ) );
check( 'non-homepage HTML untouched', '<p>x</p>' === instatech_home_ssr( '<p>x</p>' ) );
check( 'rest of the page untouched', strlen( $out ) - strlen( $raw ) === array_sum( array_map( 'strlen', instatech_home_ssr_sections() ) ) );
file_put_contents( sys_get_temp_dir() . '/home-ssr-out.html', $out );
exit( $fail ? 1 : 0 );
