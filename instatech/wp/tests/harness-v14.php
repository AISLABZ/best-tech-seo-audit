<?php
// Stubbed-WordPress tests for v1.4.0 contextual links, run against saved live page bodies.
// Run: php instatech/wp/tests/harness-v14.php instatech/wp/mu-plugins/instatech-seo-fixes.php <dir of saved article bodies: <slug>.body.html>
define( 'ABSPATH', '/x/' );
define( 'OBJECT', 'OBJECT' );
$F = array(); $LIVE = true; $POST = null;
function add_filter( $h, $cb, $p = 10, $n = 1 ) { global $F; $F[ $h ][ $p ][] = array( $cb, $n ); }
function add_action( $h, $cb, $p = 10, $n = 1 ) {}
function apply( $h, ...$a ) { global $F; ksort( $F[ $h ] ); foreach ( $F[ $h ] as $list ) { foreach ( $list as $f ) { $a[0] = call_user_func_array( $f[0], array_slice( $a, 0, $f[1] ) ); } } return $a[0]; }
function get_page_by_path( $p ) { global $LIVE; return $LIVE ? (object) array( 'post_status' => 'publish' ) : null; }
function get_option( $k ) { return false; }
function is_admin() { return false; }
function is_front_page() { return false; }
function home_url( $p = '' ) { return 'https://instatech.uk' . $p; }
function trailingslashit( $s ) { return rtrim( $s, '/' ) . '/'; }
function untrailingslashit( $s ) { return rtrim( $s, '/' ); }
function esc_url( $u ) { return $u; }
function esc_html( $s ) { return htmlspecialchars( $s ); }
function wp_strip_all_tags( $s ) { return strip_tags( $s ); }
function get_post() { global $POST; return $POST; }
require $argv[1];
$dir = $argv[2];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }
$B = 'href="https://instatech.uk/mobile-repair-services/battery-replacement/"';
$S = 'href="https://instatech.uk/mobile-repair-services/screen-repair/"';

foreach ( array( 'guide-to-phone-battery-replacement-uk', 'why-is-my-phone-battery-draining', 'iphone-battery-health-not-showing', 'bloomsbury', 'moorgate' ) as $slug ) {
	$POST = (object) array( 'post_name' => $slug );
	$in   = file_get_contents( "$dir/$slug.body.html" );
	$out  = apply( 'the_content', $in );
	check( "$slug: exactly one new battery link", substr_count( $out, $B ) - substr_count( $in, $B ) === 1 );
	check( "$slug: idempotent", $out === apply( 'the_content', $out ) );
	check( "$slug: visible text unchanged", strip_tags( $out ) === strip_tags( $in ) );
	if ( in_array( $slug, array( 'bloomsbury', 'moorgate' ), true ) ) {
		check( "$slug: also links phone screens", substr_count( $out, $S ) - substr_count( $in, $S ) === 1 );
	}
}

$POST = (object) array( 'post_name' => 'how-long-does-phone-repair-take' );
$in   = file_get_contents( "$dir/how-long-does-phone-repair-take.body.html" );
check( 'unlisted page gets no contextual link', substr_count( apply( 'the_content', $in ), $B ) === substr_count( $in, $B ) + ( false !== strpos( $in, '/layouts/battery/' ) ? 1 : 0 ) );

$LIVE = false;
$POST = (object) array( 'post_name' => 'why-is-my-phone-battery-draining' );
$in   = file_get_contents( "$dir/why-is-my-phone-battery-draining.body.html" );
check( 'no link while the battery page is unpublished', substr_count( apply( 'the_content', $in ), $B ) === substr_count( $in, $B ) );

exit( $fail ? 1 : 0 );
