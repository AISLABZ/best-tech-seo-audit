<?php
// Stubbed-WordPress tests for the one-shot page creator.
// Run: php instatech/wp/tests/harness-creator.php instatech/wp/mu-plugins/instatech-create-<slug>.php instatech/pages/<slug>.block.html <slug>
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
// Like WordPress, wp_insert_post() unslashes its input.
function wp_insert_post( $a ) { global $INSERTS, $KSES, $KSES_OFF_DURING_INSERT; $KSES_OFF_DURING_INSERT = ! $KSES; $a['post_content'] = stripslashes( $a['post_content'] ); $INSERTS[] = $a; return 4242; }
function wp_slash( $s ) { return addslashes( $s ); }
function is_wp_error( $x ) { return false; }
function update_post_meta( $id, $k, $v ) { global $META; $META[ $k ] = $v; }
function run() { global $ACT; foreach ( $ACT['init'] as $cb ) { $cb(); } }
require $argv[1];
$slug = isset( $argv[3] ) ? $argv[3] : 'battery-replacement';

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }

run();
check( 'creates exactly one page', 1 === count( $INSERTS ) );
$p = $INSERTS[0];
check( 'published under Mobile Repair Services', 'publish' === $p['post_status'] && 75806 === $p['post_parent'] && $slug === $p['post_name'] && 'page' === $p['post_type'] );
// Nowdoc drops the newline before its terminator; nothing else may differ.
check( 'content is the built block, backslashes intact', rtrim( $p['post_content'] ) === rtrim( file_get_contents( $argv[2] ) ) );
check( 'kses off during insert, restored after', true === $KSES_OFF_DURING_INSERT && true === $KSES );
check( 'Rank Math title/description/keyword set', false !== strpos( $META['rank_math_title'], '| InstaTech' ) && false !== strpos( $META['rank_math_description'], 'Free diagnostic' ) && false !== strpos( $META['rank_math_focus_keyword'], 'london' ) );
check( 'no prices in content or meta', ! preg_match( '/£\s?\d/', $p['post_content'] . implode( ' ', $META ) ) );
check( 'records created page id', '4242' === get_option( 'instatech_page_created_' . $slug ) && false === get_option( 'instatech_page_creating_' . $slug ) );
run();
check( 'second request does nothing', 1 === count( $INSERTS ) );

$OPT = array(); $INSERTS = array(); $EXISTS = true;
run();
check( 'existing page is never duplicated', 0 === count( $INSERTS ) && 'exists' === get_option( 'instatech_page_created_' . $slug ) );

$OPT = array( 'instatech_page_creating_' . $slug => 1 ); $INSERTS = array(); $EXISTS = false;
run();
check( 'concurrent request backs off while another is creating', 0 === count( $INSERTS ) );

exit( $fail ? 1 : 0 );
