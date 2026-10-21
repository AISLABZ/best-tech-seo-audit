<?php
/**
 * Plugin Name: InstaTech audit fixes
 * Description: Fixes from the 21 Oct 2026 performance and catalogue audit. Output filters only, no database writes.
 *              Kept separate from instatech-seo-fixes.php so the two can be deployed independently.
 *              Roll back by replacing this file with an empty one, or define INSTATECH_AUDIT_FIXES_OFF in wp-config.php.
 * Version:     1.0.0
 * Source:      https://github.com/aislabz/best-tech-seo-audit (instatech/wp/mu-plugins/instatech-audit-fixes.php)
 */

defined( 'ABSPATH' ) || exit;

if ( defined( 'INSTATECH_AUDIT_FIXES_OFF' ) && INSTATECH_AUDIT_FIXES_OFF ) {
	return;
}

/**
 * Duplicate products (second copy at a "-2" slug) whose price and stock match the original, mapped to the original.
 * Pairs with different prices are left alone until the owner decides which price stands.
 */
function instatech_audit_duplicate_products() {
	return array(
		'/product/a1-aux-cable-1m-2/'                                      => '/product/a1-aux-cable-1m/',
		'/product/a10-lightning-to-3-5mm-audiolightning-charging-splitter-2/' => '/product/a10-lightning-to-3-5mm-audiolightning-charging-splitter/',
		'/product/a35-usb-c-to-audio3-5mm-charging-adapter-2/'             => '/product/a35-usb-c-to-audio3-5mm-charging-adapter/',
		'/product/ethernet-cable-1-gbps-speed-2m-2/'                       => '/product/ethernet-cable-1-gbps-speed-2m/',
		'/product/ethernet-cable-1-gbps-speed-5m-2/'                       => '/product/ethernet-cable-1-gbps-speed-5m/',
		'/product/ethernet-cable-10-gbps-speed-2m-2/'                      => '/product/ethernet-cable-10-gbps-speed-2m/',
		'/product/ethernet-cable-10-gbps-speed-5m-2/'                      => '/product/ethernet-cable-10-gbps-speed-5m/',
		'/product/j21-lightning-to-3-5mm-audiolightning-charging-splitter-2/' => '/product/j21-lightning-to-3-5mm-audiolightning-charging-splitter/',
		'/product/smart-watch-usb-a-charging-cable-2/'                     => '/product/smart-watch-usb-a-charging-cable/',
		'/product/z-series-3-5mm-to-3-5mm-audio-cable-1-2m-2/'             => '/product/z-series-3-5mm-to-3-5mm-audio-cable-1-2m/',
		'/product/z-series-lightning-to-3-5mm-audio-cable-1-2m-2/'         => '/product/z-series-lightning-to-3-5mm-audio-cable-1-2m/',
		'/product/z-series-usb-c-to-3-5mm-audio-cable-1-2m-2/'             => '/product/z-series-usb-c-to-3-5mm-audio-cable-1-2m/',
	);
}

/**
 * Path of a URL or request URI, with a trailing slash and no query string.
 */
function instatech_audit_path( $url ) {
	$path = wp_parse_url( (string) $url, PHP_URL_PATH );
	return trailingslashit( is_string( $path ) ? $path : '/' );
}

/**
 * 301 each duplicate product page to its original.
 */
add_action(
	'template_redirect',
	function () {
		if ( is_admin() || ! is_singular( 'product' ) ) {
			return;
		}
		$uri = isset( $_SERVER['REQUEST_URI'] ) ? (string) wp_unslash( $_SERVER['REQUEST_URI'] ) : '';
		$map = instatech_audit_duplicate_products();
		$key = instatech_audit_path( $uri );
		if ( isset( $map[ $key ] ) ) {
			wp_safe_redirect( home_url( $map[ $key ] ), 301, 'InstaTech audit fixes' );
			exit;
		}
	},
	0
);

/**
 * Sitemaps: drop the redirected duplicates, and drop the shop archive from product-sitemap.xml
 * (it is already listed in page-sitemap.xml).
 */
add_filter(
	'rank_math/sitemap/entry',
	function ( $url ) {
		if ( ! is_array( $url ) || empty( $url['loc'] ) ) {
			return $url;
		}
		$path = instatech_audit_path( $url['loc'] );
		if ( isset( instatech_audit_duplicate_products()[ $path ] ) ) {
			return false;
		}
		$uri = isset( $_SERVER['REQUEST_URI'] ) ? (string) wp_unslash( $_SERVER['REQUEST_URI'] ) : '';
		if ( '/shop/' === $path && false !== strpos( $uri, 'product-sitemap' ) ) {
			return false;
		}
		return $url;
	},
	99
);

add_filter(
	'rank_math/sitemap/post_type_archive_link',
	function ( $link, $post_type ) {
		return 'product' === $post_type ? false : $link;
	},
	99,
	2
);

/**
 * Serve sitemaps fresh so the exclusions above take effect without a manual cache clear.
 */
add_filter( 'rank_math/sitemap/enable_caching', '__return_false' );

/**
 * Product schema: drop the " - InstaTech" title suffix from the product name.
 */
add_filter(
	'rank_math/json_ld',
	function ( $data ) {
		if ( ! is_array( $data ) ) {
			return $data;
		}
		foreach ( $data as $key => $node ) {
			if ( ! is_array( $node ) || empty( $node['@type'] ) || empty( $node['name'] ) || ! is_string( $node['name'] ) ) {
				continue;
			}
			if ( in_array( 'Product', (array) $node['@type'], true ) ) {
				$data[ $key ]['name'] = preg_replace( '/\s+[-–|]\s+InstaTech$/i', '', $node['name'] );
			}
		}
		return $data;
	},
	99
);
