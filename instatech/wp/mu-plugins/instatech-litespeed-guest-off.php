<?php
/**
 * Plugin Name: InstaTech one-shot: LiteSpeed Guest Mode off
 * Description: Approved by the owner on 21 Oct 2026 (Option A). Guest Mode made every first visit load twice
 *              (guest.vary.php, then a reload to the device variant). Saves Guest Mode and Guest Optimization as OFF
 *              through LiteSpeed's own settings save (Conf::update_confs, the same call the Save button makes), once.
 *              Writes the before/after values to wp-content/instatech-ops/litespeed-guest.json. Safe to leave in place;
 *              replace with an empty file to retire it. To undo: switch Guest Mode back on in LiteSpeed Cache → General.
 */

defined( 'ABSPATH' ) || exit;

add_action(
	'wp_loaded',
	function () {
		if ( get_option( 'instatech_ls_guest_off_done' ) || ! class_exists( '\LiteSpeed\Conf' ) ) {
			return;
		}
		// add_option fails if the key exists, so only one request can run the change.
		if ( ! add_option( 'instatech_ls_guest_off_lock', time(), '', false ) ) {
			return;
		}

		$log = array( 'time' => gmdate( 'c' ) );
		try {
			if ( ! function_exists( 'get_plugins' ) ) {
				require_once ABSPATH . 'wp-admin/includes/plugin.php';
			}
			if ( ! function_exists( 'WP_Filesystem' ) ) {
				require_once ABSPATH . 'wp-admin/includes/file.php';
			}

			$conf               = \LiteSpeed\Conf::cls();
			$log['before']      = array(
				'guest'      => $conf->conf( \LiteSpeed\Base::O_GUEST ),
				'guest_optm' => $conf->conf( \LiteSpeed\Base::O_GUEST_OPTM ),
			);
			$conf->update_confs(
				array(
					\LiteSpeed\Base::O_GUEST      => false,
					\LiteSpeed\Base::O_GUEST_OPTM => false,
				)
			);
			$log['after']  = array(
				'guest'      => $conf->conf( \LiteSpeed\Base::O_GUEST ),
				'guest_optm' => $conf->conf( \LiteSpeed\Base::O_GUEST_OPTM ),
			);
			$log['result'] = 'ok';
		} catch ( \Throwable $e ) {
			$log['result'] = 'error';
			$log['error']  = $e->getMessage();
		}
		// One attempt only, success or not: an error is logged for review instead of retried on every request.
		update_option( 'instatech_ls_guest_off_done', $log['result'] . ' ' . gmdate( 'c' ), false );
		delete_option( 'instatech_ls_guest_off_lock' );

		$dir = WP_CONTENT_DIR . '/instatech-ops';
		if ( wp_mkdir_p( $dir ) ) {
			file_put_contents( $dir . '/litespeed-guest.json', wp_json_encode( $log, JSON_PRETTY_PRINT ) );
		}
	},
	99
);
