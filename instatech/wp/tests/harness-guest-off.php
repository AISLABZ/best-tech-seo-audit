<?php
// Stubbed tests for the one-shot LiteSpeed Guest Mode change.
// Run: php instatech/wp/tests/harness-guest-off.php instatech/wp/mu-plugins/instatech-litespeed-guest-off.php
namespace LiteSpeed {
	class Base { const O_GUEST = 'guest'; const O_GUEST_OPTM = 'guest_optm'; }
	class Conf {
		public static $inst; public $v = array( 'guest' => true, 'guest_optm' => true ); public $calls = 0; public $throw = false;
		public static function cls() { return self::$inst; }
		public function conf( $k ) { return $this->v[ $k ]; }
		public function update_confs( $m ) { $this->calls++; if ( $this->throw ) { throw new \RuntimeException( 'boom' ); } foreach ( $m as $k => $val ) { $this->v[ $k ] = $val; } }
	}
}
namespace {
	define( 'ABSPATH', '/x/' );
	define( 'WP_CONTENT_DIR', sys_get_temp_dir() . '/itx-wpc-' . getmypid() );
	$ACT = array(); $OPT = array();
	function add_action( $h, $cb, $p = 10 ) { global $ACT; $ACT[ $h ][] = $cb; }
	function get_option( $k ) { global $OPT; return isset( $OPT[ $k ] ) ? $OPT[ $k ] : false; }
	function add_option( $k, $v ) { global $OPT; if ( isset( $OPT[ $k ] ) ) { return false; } $OPT[ $k ] = $v; return true; }
	function update_option( $k, $v ) { global $OPT; $OPT[ $k ] = $v; }
	function delete_option( $k ) { global $OPT; unset( $OPT[ $k ] ); }
	function get_plugins() {} function WP_Filesystem() {}
	function wp_mkdir_p( $d ) { return is_dir( $d ) || mkdir( $d, 0777, true ); }
	function wp_json_encode( $d, $f = 0 ) { return json_encode( $d, $f ); }
	function run() { global $ACT; foreach ( $ACT['wp_loaded'] as $cb ) { $cb(); } }
	require $argv[1];

	$fail = 0;
	function check( $l, $c ) { global $fail; echo ( $c ? 'PASS ' : 'FAIL ' ), $l, "\n"; if ( ! $c ) { $fail++; } }
	$log = function () { return json_decode( file_get_contents( WP_CONTENT_DIR . '/instatech-ops/litespeed-guest.json' ), true ); };

	\LiteSpeed\Conf::$inst = new \LiteSpeed\Conf();
	run();
	$c = \LiteSpeed\Conf::$inst;
	check( 'both options saved off via update_confs', false === $c->v['guest'] && false === $c->v['guest_optm'] && 1 === $c->calls );
	check( 'log records before/after', $log()['before']['guest'] === true && $log()['after']['guest'] === false && 'ok' === $log()['result'] );
	run();
	check( 'runs only once', 1 === $c->calls );

	$OPT = array(); \LiteSpeed\Conf::$inst = new \LiteSpeed\Conf(); \LiteSpeed\Conf::$inst->throw = true;
	run();
	check( 'error is caught and logged, not thrown', 'error' === $log()['result'] && 'boom' === $log()['error'] );
	check( 'after an error it stops (no retry loop) and releases the lock', 0 === strpos( get_option( 'instatech_ls_guest_off_done' ), 'error' ) && false === get_option( 'instatech_ls_guest_off_lock' ) );
	run();
	check( 'no second attempt after an error', 1 === \LiteSpeed\Conf::$inst->calls );

	$OPT = array( 'instatech_ls_guest_off_lock' => 1 ); \LiteSpeed\Conf::$inst = new \LiteSpeed\Conf();
	run();
	check( 'concurrent request backs off', 0 === \LiteSpeed\Conf::$inst->calls );
	exit( $fail ? 1 : 0 );
}
