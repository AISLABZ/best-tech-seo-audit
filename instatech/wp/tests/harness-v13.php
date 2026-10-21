<?php
// Stubbed-WordPress tests for v1.3.0 (Battery Replacement in menus/footer once the page exists).
// Run: php instatech/wp/tests/harness-v13.php instatech/wp/mu-plugins/instatech-seo-fixes.php
define( 'ABSPATH', '/x/' );
$F = array();
$OPT = array();
function add_filter( $h, $cb, $p = 10, $n = 1 ) { global $F; $F[ $h ][] = array( $cb, $n ); }
function add_action( $h, $cb, $p = 10, $n = 1 ) {}
function apply( $h, ...$a ) { global $F; foreach ( $F[ $h ] as $f ) { $a[0] = call_user_func_array( $f[0], array_slice( $a, 0, $f[1] ) ); } return $a[0]; }
function get_option( $k ) { global $OPT; return isset( $OPT[ $k ] ) ? $OPT[ $k ] : false; }
function is_admin() { return false; }
function is_front_page() { return false; }
function home_url( $p = '' ) { return 'https://instatech.uk' . $p; }
function trailingslashit( $s ) { return rtrim( $s, '/' ) . '/'; }
function untrailingslashit( $s ) { return rtrim( $s, '/' ); }
function esc_url( $u ) { return $u; }
function esc_html( $s ) { return htmlspecialchars( $s ); }
function wp_strip_all_tags( $s ) { return strip_tags( $s ); }
$POST = null;
function get_post() { global $POST; return $POST; }
require $argv[1];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }
class W { public $n; function __construct( $n ) { $this->n = $n; } function get_name() { return $this->n; } }

$mk    = function ( $id, $parent, $url, $title ) { return (object) array( 'ID' => $id, 'db_id' => $id, 'menu_item_parent' => $parent, 'url' => $url, 'title' => $title, 'classes' => array() ); };
$menu  = array( $mk( 76017, 0, '', 'Repairs' ), $mk( 75859, 76017, 'https://instatech.uk/mobile-repair-services/', 'Mobile Repair Services' ), $mk( 75858, 76017, 'https://instatech.uk/tablet-repairs/', 'Tablet Repairs' ) );
$links = '<ul class="custom_links_list"><li class="custom_links_list_item"><a class="custom_links_list_item_link" href="https://instatech.uk/mobile-repair-services/" target="_blank"><span class="custom_links_list_item_title">Mobile Repair</span></a></li><li class="custom_links_list_item"><a class="custom_links_list_item_link" href="https://instatech.uk/tablet-repairs/"><span class="custom_links_list_item_title">Tablet Repair</span></a></li></ul>';
$post  = '<a href="https://instatech.uk/layouts/battery/">Battery replacements</a>';

// Before the page exists: no battery links anywhere.
$o = apply( 'wp_nav_menu_objects', $menu );
check( 'before: menu has Screen Repair only', 4 === count( $o ) && 'Screen Repair' === $o[2]->title );
$f = apply( 'elementor/widget/render_content', $links, new W( 'trx_widget_custom_links' ) );
check( 'before: footer has no battery link', false === strpos( $f, 'battery-replacement' ) );
$POST = (object) array( 'post_name' => 'how-long-does-phone-repair-take' );
check( 'before: post link goes to Mobile Repair', false !== strpos( apply( 'the_content', $post ), 'href="https://instatech.uk/mobile-repair-services/"' ) );

// After the page exists.
$OPT['instatech_page_created_battery-replacement'] = '12345';
$o = apply( 'wp_nav_menu_objects', $menu );
check( 'after: menu order Mobile, Screen, Battery, Tablet', 5 === count( $o ) && 'Screen Repair' === $o[2]->title && 'Battery Replacement' === $o[3]->title && 'Tablet Repairs' === $o[4]->title );
check( 'after: unique menu IDs', count( array_unique( array_map( function ( $i ) { return $i->ID; }, $o ) ) ) === 5 );
check( 'after: battery URL', 'https://instatech.uk/mobile-repair-services/battery-replacement/' === $o[3]->url );
check( 'after: idempotent', 5 === count( apply( 'wp_nav_menu_objects', $o ) ) );
$f = apply( 'elementor/widget/render_content', $links, new W( 'trx_widget_custom_links' ) );
check( 'after: footer order Mobile, Screen, Battery, Tablet', strpos( $f, 'Mobile Repair' ) < strpos( $f, 'Screen Repair' ) && strpos( $f, 'Screen Repair' ) < strpos( $f, 'Battery Replacement' ) && strpos( $f, 'Battery Replacement' ) < strpos( $f, 'Tablet Repair' ) );
check( 'after: footer idempotent', $f === apply( 'elementor/widget/render_content', $f, new W( 'trx_widget_custom_links' ) ) );
check( 'after: post link goes to battery page', false !== strpos( apply( 'the_content', $post ), 'href="https://instatech.uk/mobile-repair-services/battery-replacement/"' ) );
$POST = (object) array( 'post_name' => 'laptop-repair-near-me-what-to-check-first' );
check( 'laptop post still goes to laptop page', false !== strpos( apply( 'the_content', '<a href="https://instatech.uk/layouts/battery/">swollen battery</a>' ), '/laptop-desktop-repair/' ) );

exit( $fail ? 1 : 0 );
