<?php
// Stubbed-WordPress tests for v1.3.0 (keyword-cluster page overrides).
// Run: php instatech/wp/tests/harness-v13.php instatech/wp/mu-plugins/instatech-seo-fixes.php
define( 'ABSPATH', '/x/' );
function add_filter( $h, $cb, $p = 10, $n = 1 ) {}
function add_action( $h, $cb, $p = 10, $n = 1 ) {}
$GLOBALS['it_page'] = null;
function is_page() { return null !== $GLOBALS['it_page']; }
function get_queried_object() { return $GLOBALS['it_page']; }
require $argv[1];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }
function page( $slug, $parent = 0 ) { $GLOBALS['it_page'] = (object) array( 'post_name' => $slug, 'post_parent' => $parent ); }

page( 'phone-accessories-trade-in' );
check( 'accessories title', 'Phone Accessories London – Bloomsbury & Moorgate | InstaTech' === instatech_seo_override_title( 'x' ) );
check( 'accessories description has no trade-in', false === stripos( instatech_seo_override_description( 'x' ), 'trade-in' ) );
$o = instatech_seo_page_copy( '<h1>Phone accessories and phone trade-ins in central London</h1><section class="sell"><h2>Sell or trade in your phone</h2><a class="btn p" href="/buy-sell-phones/">Sell or trade in</a></section>' );
check( 'accessories H1', false !== strpos( $o, '<h1>Phone accessories in central London</h1>' ) );
check( 'exact anchor to buy-sell', false !== strpos( $o, 'href="/buy-sell-phones/">Sell your phone for cash</a>' ) );

page( 'tablet-repairs' );
check( 'tablet title London-wide', false === strpos( instatech_seo_override_title( 'x' ), 'Bloomsbury' ) );
$all = '';
foreach ( instatech_seo_page_overrides() as $p ) { $all .= $p['title'] . $p['description'] . implode( '', $p['copy'] ); }
check( 'no pricing in any override', ! preg_match( '/£|&pound;|\bfrom £/i', $all ) );
$o = instatech_seo_page_copy( "<h1>Professional<br><em>Tablet Repair</em><br>Services</h1><h2>iPad and tablet repair in Bloomsbury, near Russell Square and King's Cross</h2>" );
check( 'tablet H1', false !== strpos( $o, '<h1>iPad and tablet<br><em>repair</em><br>in London</h1>' ) );
check( 'tablet H2 names both shops', false !== strpos( $o, 'Bloomsbury and Moorgate</h2>' ) );

page( 'tablet-repairs', 5 );
check( 'child page with same slug untouched', 'x' === instatech_seo_override_title( 'x' ) );
page( 'about-us' );
check( 'other pages untouched', 'x' === instatech_seo_override_title( 'x' ) && 'y' === instatech_seo_page_copy( 'y' ) );
$GLOBALS['it_page'] = null;
check( 'non-page untouched', 'x' === instatech_seo_override_description( 'x' ) );

exit( $fail ? 1 : 0 );
