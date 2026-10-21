<?php
/**
 * Plugin Name: InstaTech SEO fixes
 * Description: Phase 1 SEO fixes from the instatech.uk audit (Oct 2026). Output filters only, no database writes.
 *              Roll back by replacing this file with an empty one, or define INSTATECH_SEO_FIXES_OFF in wp-config.php.
 * Version:     1.1.0
 * Source:      https://github.com/aislabz/best-tech-seo-audit (instatech/wp/mu-plugins/instatech-seo-fixes.php)
 */

defined( 'ABSPATH' ) || exit;

if ( defined( 'INSTATECH_SEO_FIXES_OFF' ) && INSTATECH_SEO_FIXES_OFF ) {
	return;
}

/**
 * Dead or redirecting internal links found in blog posts, mapped to their final URL.
 */
function instatech_seo_link_map() {
	return array(
		'/electronics-store-1/'                            => '/product-category/chargers/',
		'/electronics-store-2/'                            => '/locations/',
		'/electronics-repair-1/'                           => '/laptop-desktop-repair/',
		'/electronics-repair-2/'                           => '/mobile-repair-services/',
		'/signs-your-gadget-needs-repair-service-soon/'    => '/mobile-repair-services/',
		'/budget-friendly-gadgets-with-premium-features/'  => '/shop/',
		'/layouts/display/'                                => '/tablet-repairs/',
		'/layouts/battery/'                                => '/mobile-repair-services/',
		'/services/tablet-repairs/'                        => '/tablet-repairs/',
		'/services/laptop-desktop-repair/'                 => '/laptop-desktop-repair/',
		'/request-quote/'                                  => '/book-an-appointment/',
		'/testimonials/'                                   => '/about-us/',
		'/choose-car-phone-holder-mount/'                  => '/best-phone-mounts-for-cars/',
		'/3-in-1-trio-1-charging-cable/'                   => '/product/3-in-1-trio-1-charging-cable/',
	);
}

/**
 * Per-post overrides where the generic target is not the best match for the anchor.
 */
function instatech_seo_link_overrides() {
	return array(
		'desktop-computer-repair-near-me'           => array( '/electronics-repair-2/' => '/laptop-desktop-repair/' ),
		'laptop-repair-near-me-what-to-check-first' => array( '/layouts/battery/' => '/laptop-desktop-repair/' ),
		'wireless-earphones-for-calls'              => array( '/services/laptop-desktop-repair/' => '/mobile-repair-services/' ),
	);
}

add_filter(
	'the_content',
	function ( $content ) {
		if ( is_admin() || ! is_string( $content ) || false === strpos( $content, 'href' ) ) {
			return $content;
		}

		$map  = instatech_seo_link_map();
		$post = get_post();
		if ( $post ) {
			$overrides = instatech_seo_link_overrides();
			if ( isset( $overrides[ $post->post_name ] ) ) {
				$map = array_merge( $map, $overrides[ $post->post_name ] );
			}
		}

		$home = home_url();

		return preg_replace_callback(
			'#href=(["\'])((?:https?://(?:www\.)?instatech\.uk)?(/[^"\'\#?]*))([\#?][^"\']*)?\1#i',
			function ( $m ) use ( $map, $home ) {
				$path = trailingslashit( $m[3] );
				if ( ! isset( $map[ $path ] ) ) {
					return $m[0];
				}
				return 'href=' . $m[1] . esc_url( $home . $map[ $path ] ) . $m[1];
			},
			$content
		);
	},
	999
);

/**
 * Noindex theme demo layouts and the Uncategorized archive. Links stay followed.
 */
add_filter(
	'rank_math/frontend/robots',
	function ( $robots ) {
		$uri      = isset( $_SERVER['REQUEST_URI'] ) ? (string) wp_unslash( $_SERVER['REQUEST_URI'] ) : '';
		$is_demo  = 0 === strpos( $uri, '/layouts/' );
		$is_uncat = is_category( 'uncategorized' );
		if ( $is_demo || $is_uncat ) {
			$robots['index']  = 'noindex';
			$robots['follow'] = 'follow';
		}
		return $robots;
	},
	99
);

/**
 * Fill empty meta descriptions on product categories, blog categories and products.
 */
add_filter(
	'rank_math/frontend/description',
	function ( $description ) {
		if ( is_string( $description ) && '' !== trim( $description ) ) {
			return $description;
		}

		if ( is_tax( 'product_cat' ) ) {
			$term = get_queried_object();
			if ( $term && ! empty( $term->name ) ) {
				return sprintf(
					'Shop %s at InstaTech. Buy online or collect today from our Bloomsbury (WC1) and Moorgate (EC1) shops in central London.',
					$term->name
				);
			}
		}

		if ( is_category() ) {
			$term = get_queried_object();
			if ( $term && ! empty( $term->name ) ) {
				return sprintf(
					'%s guides from InstaTech\'s central London repair technicians: practical advice on phones, laptops, tablets and smartwatches.',
					$term->name
				);
			}
		}

		if ( is_singular( 'product' ) ) {
			$title = wp_strip_all_tags( get_the_title() );
			if ( '' !== $title ) {
				$text = sprintf(
					'%s from InstaTech. Buy online or collect today from our Bloomsbury and Moorgate shops in central London.',
					$title
				);
				return mb_strlen( $text ) > 160 ? rtrim( mb_substr( $text, 0, 157 ) ) . '...' : $text;
			}
		}

		return $description;
	},
	99
);

/**
 * One brand spelling in titles.
 */
add_filter(
	'rank_math/frontend/title',
	function ( $title ) {
		return is_string( $title ) ? str_replace( 'instaTech', 'InstaTech', $title ) : $title;
	},
	99
);

/**
 * Connect the Organization entity to the brand's social profiles.
 */
add_filter(
	'rank_math/json_ld',
	function ( $data ) {
		if ( ! is_array( $data ) ) {
			return $data;
		}

		$profiles = array(
			'https://www.instagram.com/instatechlondon/',
			'https://www.tiktok.com/@instatechlondon',
			'https://www.facebook.com/profile.php?id=61590593272480',
		);

		foreach ( $data as $key => $node ) {
			if ( ! is_array( $node ) || empty( $node['@type'] ) ) {
				continue;
			}
			$types = (array) $node['@type'];
			if ( ! in_array( 'Organization', $types, true ) ) {
				continue;
			}
			$existing             = isset( $node['sameAs'] ) ? (array) $node['sameAs'] : array();
			$data[ $key ]['sameAs'] = array_values( array_unique( array_merge( $existing, $profiles ) ) );
			if ( isset( $node['name'] ) && is_string( $node['name'] ) ) {
				$data[ $key ]['name'] = str_replace( 'instaTech', 'InstaTech', $node['name'] );
			}
		}

		return $data;
	},
	99
);

/**
 * Fallback alt text for images that have none: the product or post the image belongs to,
 * otherwise the attachment title.
 */
add_filter(
	'wp_get_attachment_image_attributes',
	function ( $attr, $attachment ) {
		if ( is_admin() || ! is_array( $attr ) || ( isset( $attr['alt'] ) && '' !== trim( $attr['alt'] ) ) ) {
			return $attr;
		}

		$alt = '';
		if ( $attachment && ! empty( $attachment->post_parent ) ) {
			$alt = get_the_title( $attachment->post_parent );
		}
		if ( '' === $alt && in_the_loop() ) {
			$alt = get_the_title();
		}
		if ( '' === $alt && $attachment ) {
			$alt = preg_replace( '/[-_]+/', ' ', $attachment->post_title );
		}

		$alt = trim( wp_strip_all_tags( (string) $alt ) );
		if ( '' !== $alt ) {
			$attr['alt'] = $alt;
		}
		return $attr;
	},
	99,
	2
);

/**
 * URL of the screen repair money page, which needs internal links from navigation.
 */
function instatech_seo_screen_repair_url() {
	return home_url( '/mobile-repair-services/screen-repair/' );
}

/**
 * Header and mobile menus: add "Screen Repair" under Repairs, directly after Mobile Repair Services.
 */
add_filter(
	'wp_nav_menu_objects',
	function ( $items ) {
		if ( is_admin() || ! is_array( $items ) ) {
			return $items;
		}

		$target = untrailingslashit( instatech_seo_screen_repair_url() );
		$anchor = untrailingslashit( home_url( '/mobile-repair-services/' ) );
		foreach ( $items as $item ) {
			if ( isset( $item->url ) && untrailingslashit( $item->url ) === $target ) {
				return $items;
			}
		}

		$out = array();
		foreach ( $items as $item ) {
			$out[] = $item;
			if ( ! isset( $item->url ) || untrailingslashit( $item->url ) !== $anchor ) {
				continue;
			}

			$new                        = clone $item;
			$new->ID                    = 990000 + (int) $item->ID;
			$new->db_id                 = $new->ID;
			$new->object_id             = 0;
			$new->object                = 'custom';
			$new->type                  = 'custom';
			$new->type_label            = 'Custom Link';
			$new->title                 = 'Screen Repair';
			$new->url                   = instatech_seo_screen_repair_url();
			$new->attr_title            = '';
			$new->target                = '';
			$new->xfn                   = '';
			$new->description           = '';
			$new->classes               = array( 'menu-item', 'menu-item-type-custom', 'menu-item-object-custom' );
			$new->current               = false;
			$new->current_item_ancestor = false;
			$new->current_item_parent   = false;
			$out[]                      = $new;
		}

		return $out;
	},
	20
);

/**
 * Footer widgets: add Screen Repair to the services link list and link the "About Us" heading.
 */
add_filter(
	'elementor/widget/render_content',
	function ( $content, $widget ) {
		if ( ! is_string( $content ) || ! is_object( $widget ) || ! method_exists( $widget, 'get_name' ) ) {
			return $content;
		}
		$name = $widget->get_name();

		if ( 'trx_widget_custom_links' === $name
			&& false !== strpos( $content, '/mobile-repair-services/"' )
			&& false === strpos( $content, '/screen-repair/' ) ) {
			$li      = '<li class="custom_links_list_item"><a class="custom_links_list_item_link" href="'
				. esc_url( instatech_seo_screen_repair_url() )
				. '"><span class="custom_links_list_item_title">Screen Repair</span></a></li>';
			$content = preg_replace(
				'#(<li class="custom_links_list_item"><a [^>]*href="[^"]*/mobile-repair-services/"[^>]*>.*?</li>)#s',
				'$1' . $li,
				$content,
				1
			);
		}

		if ( 'trx_sc_title' === $name
			&& false !== strpos( $content, '<span class="sc_item_title_text">About Us</span>' )
			&& false === strpos( $content, '/about-us/' ) ) {
			$content = str_replace(
				'<span class="sc_item_title_text">About Us</span>',
				'<span class="sc_item_title_text"><a href="' . esc_url( home_url( '/about-us/' ) ) . '" style="color:inherit">About Us</a></span>',
				$content
			);
		}

		return $content;
	},
	20,
	2
);

/**
 * Homepage: the hero H1 carries a campaign message. Prefix it with a small, visible line naming the service and
 * location so the H1 describes the page. The campaign headline and its styling are untouched. Skips itself once the
 * H1 already mentions repair.
 */
function instatech_seo_home_h1( $html ) {
	if ( ! is_string( $html ) || false !== strpos( $html, 'it-h1-kw' ) || ! is_front_page() ) {
		return $html;
	}
	if ( ! preg_match( '#<h1\b[^>]*>(.*?)</h1>#is', $html, $m ) ) {
		return $html;
	}
	if ( false !== stripos( wp_strip_all_tags( $m[1] ), 'repair' ) ) {
		return $html;
	}
	return preg_replace(
		'#(<h1\b[^>]*>)#i',
		'$1<span class="it-h1-kw">Phone, laptop &amp; tablet repair in central London</span>',
		$html,
		1
	);
}
add_filter( 'the_content', 'instatech_seo_home_h1', 1000 );
add_filter( 'elementor/widget/render_content', 'instatech_seo_home_h1', 21 );

add_action(
	'wp_head',
	function () {
		if ( is_front_page() ) {
			echo '<style id="instatech-seo-h1">.it-h1-kw{display:block;font-size:13px;font-weight:700;letter-spacing:.08em;line-height:1.4;text-transform:uppercase;opacity:.85;margin:0 0 10px;white-space:normal}</style>' . "\n";
		}
	},
	99
);
