<?php
// Stubbed-WordPress tests for the one-shot page creator.
// Run: php instatech/wp/tests/harness-creator.php instatech/wp/mu-plugins/instatech-create-battery-replacement.php instatech/pages/battery-replacement.block.html
define( 'ABSPATH', '/x/' );
define( 'OBJECT', 'OBJECT' );
$ACT = array(); $OPT = array(); $META = array(); $INSERTS = array(); $EXISTS = false; $KSES = true; $KSES_OFF_DURING_INSERT = null;
function add_action( $h, $cb, $p = 10 ) { global $ACT; $ACT[ $h ][] = $cb; }
function get_option( $k ) { global $OPT; return isset( $OPT[ $k ] ) ? $OPT[ $k ] : false; }
function add_option( $k, $v ) { global $OPT; if ( isset( $OPT[ $k ] ) ) { return false; } $OPT[ $k ] = $v; return true; }
function update_option( $k, $v ) { global $OPT; $OPT[ $k ] = $v; return true; }
function delete_option( $k ) { global $OPT; unset( $OPT[ $k ] ); return true; }
function get_page_by_path( $p ) { global $EXISTS; return $EXISTS ? (object) array( 'ID' => 1 ) : null; }
function has_filter( $h, $f ) { global $KSES; return $KSES ? 10 : false; }
function kses_remove_filters() { global $KSES; $KSES = false; }
function kses_init_filters() { global $KSES; $KSES = true; }
function wp_insert_post( $a ) { global $INSERTS, $KSES, $KSES_OFF_DURING_INSERT; $KSES_OFF_DURING_INSERT = ! $KSES; $INSERTS[] = $a; return 4242; }
function is_wp_error( $x ) { return false; }
function update_post_meta( $id, $k, $v ) { global $META; $META[ $k ] = $v; }
function run() { global $ACT; foreach ( $ACT['init'] as $cb ) { $cb(); } }
require $argv[1];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }

run();
check( 'creates exactly one page', 1 === count( $INSERTS ) );
$p = $INSERTS[0];
check( 'published under Mobile Repair Services', 'publish' === $p['post_status'] && 75806 === $p['post_parent'] && 'battery-replacement' === $p['post_name'] && 'page' === $p['post_type'] );
// Nowdoc drops the newline before its terminator; nothing else may differ.
check( 'content is the built block', rtrim( $p['post_content'] ) === rtrim( file_get_contents( $argv[2] ) ) );
check( 'kses off during insert, restored after', true === $KSES_OFF_DURING_INSERT && true === $KSES );
check( 'Rank Math title/description/keyword set', 'Phone Battery Replacement London – Same Day | InstaTech' === $META['rank_math_title'] && false !== strpos( $META['rank_math_description'], 'Free diagnostic' ) && 'phone battery replacement london' === $META['rank_math_focus_keyword'] );
check( 'records created page id', '4242' === get_option( 'instatech_page_created_battery-replacement' ) && false === get_option( 'instatech_page_creating_battery-replacement' ) );
run();
check( 'second request does nothing', 1 === count( $INSERTS ) );

$OPT = array(); $INSERTS = array(); $EXISTS = true;
run();
check( 'existing page is never duplicated', 0 === count( $INSERTS ) && 'exists' === get_option( 'instatech_page_created_battery-replacement' ) );

$OPT = array( 'instatech_page_creating_battery-replacement' => 1 ); $INSERTS = array(); $EXISTS = false;
run();
check( 'concurrent request backs off while another is creating', 0 === count( $INSERTS ) );

exit( $fail ? 1 : 0 );
