<?php
// Stubbed-WordPress tests for the v1.1.0 additions (menu, footer, homepage H1).
// Run: php instatech/wp/tests/harness-v11.php instatech/wp/mu-plugins/instatech-seo-fixes.php
define( 'ABSPATH', '/x/' );
$F = array();
$A = array();
function add_filter( $h, $cb, $p = 10, $n = 1 ) { global $F; $F[ $h ][] = array( $cb, $n ); }
function add_action( $h, $cb, $p = 10, $n = 1 ) { global $A; $A[ $h ][] = $cb; }
function apply( $h, ...$a ) { global $F; foreach ( $F[ $h ] as $f ) { $a[0] = call_user_func_array( $f[0], array_slice( $a, 0, $f[1] ) ); } return $a[0]; }
$FRONT = true;
function is_admin() { return false; }
function is_front_page() { global $FRONT; return $FRONT; }
function home_url( $p = '' ) { return 'https://instatech.uk' . $p; }
function trailingslashit( $s ) { return rtrim( $s, '/' ) . '/'; }
function untrailingslashit( $s ) { return rtrim( $s, '/' ); }
function esc_url( $u ) { return $u; }
function wp_strip_all_tags( $s ) { return strip_tags( $s ); }
function get_post() { return null; } function get_option( $k ) { return false; } function esc_html( $s ) { return $s; }
require $argv[1];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }

// Menu.
$mk = function ( $id, $parent, $url, $title ) { return (object) array( 'ID' => $id, 'db_id' => $id, 'menu_item_parent' => $parent, 'url' => $url, 'title' => $title, 'classes' => array( 'menu-item' ) ); };
$menu = array( $mk( 76017, 0, '', 'Repairs' ), $mk( 75859, 76017, 'https://instatech.uk/mobile-repair-services/', 'Mobile Repair Services' ), $mk( 75858, 76017, 'https://instatech.uk/tablet-repairs/', 'Tablet Repairs' ) );
$out  = apply( 'wp_nav_menu_objects', $menu );
check( 'menu gains one item', 4 === count( $out ) );
check( 'Screen Repair sits after Mobile Repair', 'Screen Repair' === $out[2]->title && '76017' == $out[2]->menu_item_parent );
check( 'Screen Repair URL', 'https://instatech.uk/mobile-repair-services/screen-repair/' === $out[2]->url );
check( 'original item untouched', 'Mobile Repair Services' === $out[1]->title && 75859 === $out[1]->ID );
check( 'idempotent when link already exists', 4 === count( apply( 'wp_nav_menu_objects', $out ) ) );

// Footer widgets.
class W { public $n; function __construct( $n ) { $this->n = $n; } function get_name() { return $this->n; } }
$links = '<ul class="custom_links_list"><li class="custom_links_list_item"><a class="custom_links_list_item_link" href="https://instatech.uk/mobile-repair-services/" target="_blank"><span class="custom_links_list_item_title">Mobile Repair</span></a></li><li class="custom_links_list_item"><a class="custom_links_list_item_link" href="https://instatech.uk/tablet-repairs/" target="_blank"><span class="custom_links_list_item_title">Tablet Repair</span></a></li></ul>';
$FRONT = false;
$o = apply( 'elementor/widget/render_content', $links, new W( 'trx_widget_custom_links' ) );
check( 'footer gains Screen Repair once', 1 === substr_count( $o, '/screen-repair/' ) );
check( 'footer order: Mobile, Screen, Tablet', strpos( $o, 'Mobile Repair' ) < strpos( $o, 'Screen Repair' ) && strpos( $o, 'Screen Repair' ) < strpos( $o, 'Tablet Repair' ) );
$t = '<h6 class="sc_item_title"><span class="sc_item_title_text">About Us</span></h6>';
check( 'About Us heading linked', false !== strpos( apply( 'elementor/widget/render_content', $t, new W( 'trx_sc_title' ) ), 'href="https://instatech.uk/about-us/"' ) );
check( 'other widgets untouched', $links === apply( 'elementor/widget/render_content', $links, new W( 'text-editor' ) ) );

// Homepage H1.
$FRONT = true;
$hero  = '<span class="hbadge">Coming soon</span><h1 class="hh-c oc-h1"><span class="oc-l1">2 shops weren&rsquo;t enough.</span><br><em class="oc-em">Oxford Circus is next.</em></h1>';
$o     = apply( 'the_content', $hero );
check( 'H1 gains service line', false !== strpos( $o, '<h1 class="hh-c oc-h1"><span class="it-h1-kw">Phone, laptop &amp; tablet repair in central London</span><span class="oc-l1">' ) );
check( 'H1 idempotent', $o === apply( 'the_content', $o ) );
check( 'H1 untouched when it already says repair', '<h1>Phone repair London</h1>' === apply( 'the_content', '<h1>Phone repair London</h1>' ) );
$FRONT = false;
check( 'H1 untouched off the homepage', $hero === apply( 'the_content', $hero ) );

exit( $fail ? 1 : 0 );
