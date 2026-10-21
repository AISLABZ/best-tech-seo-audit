<?php
/**
 * Plugin Name: InstaTech SEO fixes
 * Description: Phase 1 SEO fixes from the instatech.uk audit (Oct 2026). Output filters only, no database writes.
 *              Roll back by replacing this file with an empty one, or define INSTATECH_SEO_FIXES_OFF in wp-config.php.
 * Version:     1.4.0
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
 * Whether a page is published at the given path. Navigation only links to pages that exist.
 * get_page_by_path() results are held in the WordPress object cache, so repeat calls are cheap.
 */
function instatech_seo_page_live( $path ) {
	$page = get_page_by_path( $path, OBJECT, 'page' );
	return $page && 'publish' === $page->post_status;
}

/**
 * Per-post overrides where the generic target is not the best match for the anchor.
 */
function instatech_seo_link_overrides() {
	$overrides = array(
		'desktop-computer-repair-near-me'           => array( '/electronics-repair-2/' => '/laptop-desktop-repair/' ),
		'laptop-repair-near-me-what-to-check-first' => array( '/layouts/battery/' => '/laptop-desktop-repair/' ),
		'wireless-earphones-for-calls'              => array( '/services/laptop-desktop-repair/' => '/mobile-repair-services/' ),
	);
	if ( instatech_seo_page_live( 'mobile-repair-services/battery-replacement' ) ) {
		$overrides['how-long-does-phone-repair-take'] = array( '/layouts/battery/' => '/mobile-repair-services/battery-replacement/' );
	}
	return $overrides;
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
 * Repair pages to list after Mobile Repair Services in the menus and footer, in order. A page is only listed once it
 * exists, so navigation never points at a missing page.
 */
function instatech_seo_service_links() {
	$links = array(
		array(
			'title' => 'Screen Repair',
			'url'   => instatech_seo_screen_repair_url(),
		),
	);
	if ( instatech_seo_page_live( 'mobile-repair-services/battery-replacement' ) ) {
		$links[] = array(
			'title' => 'Battery Replacement',
			'url'   => home_url( '/mobile-repair-services/battery-replacement/' ),
		);
	}
	return $links;
}

/**
 * Header and mobile menus: add the repair pages under Repairs, directly after Mobile Repair Services.
 */
add_filter(
	'wp_nav_menu_objects',
	function ( $items ) {
		if ( is_admin() || ! is_array( $items ) ) {
			return $items;
		}

		$present = array();
		foreach ( $items as $item ) {
			if ( isset( $item->url ) ) {
				$present[ untrailingslashit( $item->url ) ] = true;
			}
		}
		$missing = array();
		foreach ( instatech_seo_service_links() as $link ) {
			if ( empty( $present[ untrailingslashit( $link['url'] ) ] ) ) {
				$missing[] = $link;
			}
		}
		if ( ! $missing ) {
			return $items;
		}

		$anchor = untrailingslashit( home_url( '/mobile-repair-services/' ) );
		$out    = array();
		foreach ( $items as $item ) {
			$out[] = $item;
			if ( ! isset( $item->url ) || untrailingslashit( $item->url ) !== $anchor ) {
				continue;
			}

			foreach ( $missing as $n => $link ) {
				$new                        = clone $item;
				$new->ID                    = 990000 + ( 100 * $n ) + (int) $item->ID;
				$new->db_id                 = $new->ID;
				$new->object_id             = 0;
				$new->object                = 'custom';
				$new->type                  = 'custom';
				$new->type_label            = 'Custom Link';
				$new->title                 = $link['title'];
				$new->url                   = $link['url'];
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
		}

		return $out;
	},
	20
);

/**
 * Footer widgets: add the repair pages to the services link list and link the "About Us" heading.
 */
add_filter(
	'elementor/widget/render_content',
	function ( $content, $widget ) {
		if ( ! is_string( $content ) || ! is_object( $widget ) || ! method_exists( $widget, 'get_name' ) ) {
			return $content;
		}
		$name = $widget->get_name();

		if ( 'trx_widget_custom_links' === $name && false !== strpos( $content, '/mobile-repair-services/"' ) ) {
			$li = '';
			foreach ( instatech_seo_service_links() as $link ) {
				if ( false === strpos( $content, 'href="' . esc_url( $link['url'] ) . '"' ) ) {
					$li .= '<li class="custom_links_list_item"><a class="custom_links_list_item_link" href="'
						. esc_url( $link['url'] )
						. '"><span class="custom_links_list_item_title">' . esc_html( $link['title'] ) . '</span></a></li>';
				}
			}
			if ( '' !== $li ) {
				$content = preg_replace(
					'#(<li class="custom_links_list_item"><a [^>]*href="[^"]*/mobile-repair-services/"[^>]*>.*?</li>)#s',
					'$1' . str_replace( array( '\\', '$' ), array( '\\\\', '\\$' ), $li ),
					$content,
					1
				);
			}
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

/**
 * In-text links to the repair pages, on wording that already exists in each page. Each rule is the exact text to find
 * (first occurrence only) and the replacement with the link added; nothing else in the copy changes. A rule only applies
 * while its target page is published and is skipped if the page already links there.
 */
function instatech_seo_contextual_links() {
	$battery = home_url( '/mobile-repair-services/battery-replacement/' );
	$screen  = instatech_seo_screen_repair_url();
	$style   = ' style="color:inherit;text-decoration:underline;text-underline-offset:2px"';

	return array(
		'guide-to-phone-battery-replacement-uk' => array(
			'target' => $battery,
			'find'   => 'fit a compatible replacement battery and test charging',
			'repl'   => 'fit a compatible <a href="' . $battery . '">replacement battery</a> and test charging',
		),
		'why-is-my-phone-battery-draining'      => array(
			'target' => $battery,
			'find'   => 'a battery replacement can be a better value choice',
			'repl'   => 'a <a href="' . $battery . '">battery replacement</a> can be a better value choice',
		),
		'iphone-battery-health-not-showing'     => array(
			'target' => $battery,
			'find'   => 'there is no fee. Battery replacement starts',
			'repl'   => 'there is no fee. <a href="' . $battery . '">Battery replacement</a> starts',
		),
		'bloomsbury'                            => array(
			'target' => $battery,
			'find'   => 'most phone screens and batteries are done while you wait',
			'repl'   => 'most <a href="' . $screen . '"' . $style . '>phone screens</a> and <a href="' . $battery . '"' . $style . '>batteries</a> are done while you wait',
		),
		'moorgate'                              => array(
			'target' => $battery,
			'find'   => 'most phone screens and batteries are done while you wait',
			'repl'   => 'most <a href="' . $screen . '"' . $style . '>phone screens</a> and <a href="' . $battery . '"' . $style . '>batteries</a> are done while you wait',
		),
	);
}

add_filter(
	'the_content',
	function ( $content ) {
		if ( is_admin() || ! is_string( $content ) ) {
			return $content;
		}
		$post = get_post();
		if ( ! $post ) {
			return $content;
		}
		$rules = instatech_seo_contextual_links();
		if ( ! isset( $rules[ $post->post_name ] ) ) {
			return $content;
		}
		$rule = $rules[ $post->post_name ];
		if ( false !== strpos( $content, 'href="' . $rule['target'] . '"' ) || false === strpos( $content, $rule['find'] ) ) {
			return $content;
		}
		if ( ! instatech_seo_page_live( 'mobile-repair-services/battery-replacement' ) ) {
			return $content;
		}
		$at = strpos( $content, $rule['find'] );
		return substr_replace( $content, $rule['repl'], $at, strlen( $rule['find'] ) );
	},
	1001
);

/**
 * Each shop's Google Business Profile, resolved from Google Maps on 21 Oct 2026.
 * cid gives a permanent link to the listing; place_id pins directions to it.
 */
function instatech_seo_shop_listings() {
	return array(
		'bloomsbury' => array(
			'cid'      => '10641785332690239296',
			'place_id' => 'ChIJg5Ii0NUbdkgRQL_2omA3r5M',
		),
		'moorgate'   => array(
			'cid'      => '8404697699929828128',
			'place_id' => 'ChIJm5ZiHwAddkgRICvcMAd8o3Q',
		),
	);
}

/**
 * Point Google Maps search links (in schema, buttons and text links) at the exact listings, and pin directions links
 * to the listing's place ID. Embedded map iframes (output=embed) are left untouched.
 */
function instatech_seo_maps_links( $html ) {
	if ( ! is_string( $html ) || false === strpos( $html, 'google.' ) ) {
		return $html;
	}

	$shops = instatech_seo_shop_listings();
	$cid   = array(
		'bloomsbury' => 'https://maps.google.com/?cid=' . $shops['bloomsbury']['cid'],
		'moorgate'   => 'https://maps.google.com/?cid=' . $shops['moorgate']['cid'],
	);

	$html = str_replace(
		array(
			'https://www.google.com/maps/place/instaTech+-+(Bloomsbury)/',
			'https://www.google.com/maps/place/instaTech+-+Moorgate/',
		),
		array( $cid['bloomsbury'], $cid['moorgate'] ),
		$html
	);

	// Address searches, only where the URL ends there (a quote follows), so embeds keep working.
	$html = preg_replace(
		array(
			'#https://www\.google\.com/maps\?q=67\+Marchmont\+Street,\+London\+WC1N\+1AP(?=\\\\?"|&quot;|\')#',
			'#https://www\.google\.com/maps\?q=16\+City\+Road,\+London\+EC1Y\+2AA(?=\\\\?"|&quot;|\')#',
		),
		array( $cid['bloomsbury'], $cid['moorgate'] ),
		$html
	);

	// Directions: add the destination place ID unless one is already present.
	$html = preg_replace(
		array(
			'#(https://www\.google\.com/maps/dir/\?api=1(?:&amp;|&)destination=67\+Marchmont\+Street\+London\+WC1N\+1AP)(?!(?:&amp;|&)destination_place_id)#',
			'#(https://www\.google\.com/maps/dir/\?api=1(?:&amp;|&)destination=16\+City\+Road\+London\+EC1Y\+2AA)(?!(?:&amp;|&)destination_place_id)#',
		),
		array(
			'$1&amp;destination_place_id=' . $shops['bloomsbury']['place_id'],
			'$1&amp;destination_place_id=' . $shops['moorgate']['place_id'],
		),
		$html
	);

	return $html;
}

add_action(
	'template_redirect',
	function () {
		if ( is_admin() || is_feed() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
			return;
		}
		ob_start( 'instatech_seo_maps_links' );
	},
	1
);

add_action(
	'wp_head',
	function () {
		if ( is_front_page() ) {
			echo '<style id="instatech-seo-h1">.it-h1-kw{display:block;font-size:13px;font-weight:700;letter-spacing:.08em;line-height:1.4;text-transform:uppercase;opacity:.85;margin:0 0 10px;white-space:normal}</style>' . "\n";
		}
	},
	99
);

/**
 * Keyword-cluster changes approved by the owner on 21 Oct 2026 (instatech/proposals/2026-10-21-keyword-cluster-decisions.md).
 * /buy-sell-phones/ owns trade-in, so the accessories page drops it from its title, description and H1. Both shops
 * repair tablets, so the tablet page targets London rather than Bloomsbury only. No prices are added (owner rule).
 */
function instatech_seo_page_overrides() {
	return array(
		'phone-accessories-trade-in' => array(
			'title'       => 'Phone Accessories London – Bloomsbury & Moorgate | InstaTech',
			'description' => 'Chargers, cables, power banks, earphones and car mounts in stock at our Bloomsbury and Moorgate shops, open 7 days. Selling your phone? Get a cash offer.',
			'copy'        => array(
				'<h1>Phone accessories and phone trade-ins in central London</h1>' => '<h1>Phone accessories in central London</h1>',
				'<h2>Sell or trade in your phone</h2>'                              => '<h2>Selling your phone?</h2>',
				'<a class="btn p" href="/buy-sell-phones/">Sell or trade in</a>'    => '<a class="btn p" href="/buy-sell-phones/">Sell your phone for cash</a>',
			),
		),
		'tablet-repairs'             => array(
			'title'       => 'iPad & Tablet Repair London – Open 7 Days | InstaTech',
			'description' => 'iPad and tablet repair at our Bloomsbury WC1 and Moorgate EC1 shops: screens, batteries, charging ports and water damage. Free diagnostic, open 7 days.',
			'copy'        => array(
				'<h1>Professional<br><em>Tablet Repair</em><br>Services</h1>' => '<h1>iPad and tablet<br><em>repair</em><br>in London</h1>',
				"<h2>iPad and tablet repair in Bloomsbury, near Russell Square and King's Cross</h2>" => '<h2>iPad and tablet repair in Bloomsbury and Moorgate</h2>',
				'We repair iPads and Android tablets at 67 Marchmont Street, WC1N 1AP, a short walk from Russell Square station and about ten minutes from King\'s Cross St Pancras.' => 'We repair iPads and Android tablets at both our shops: 67 Marchmont Street, WC1N 1AP, a short walk from Russell Square station and about ten minutes from King\'s Cross St Pancras, and 16 City Road, EC1Y 2AA, near Moorgate and Old Street.',
			),
		),
	);
}

function instatech_seo_page_override() {
	if ( ! is_page() ) {
		return null;
	}
	$page = get_queried_object();
	if ( ! $page || ! empty( $page->post_parent ) ) {
		return null;
	}
	$map = instatech_seo_page_overrides();
	return isset( $map[ $page->post_name ] ) ? $map[ $page->post_name ] : null;
}

function instatech_seo_override_title( $title ) {
	$o = instatech_seo_page_override();
	return $o ? $o['title'] : $title;
}

function instatech_seo_override_description( $description ) {
	$o = instatech_seo_page_override();
	return $o ? $o['description'] : $description;
}

add_filter( 'rank_math/frontend/title', 'instatech_seo_override_title', 100 );
add_filter( 'rank_math/opengraph/facebook/og_title', 'instatech_seo_override_title', 100 );
add_filter( 'rank_math/opengraph/twitter/twitter_title', 'instatech_seo_override_title', 100 );
add_filter( 'rank_math/frontend/description', 'instatech_seo_override_description', 100 );
add_filter( 'rank_math/opengraph/facebook/og_description', 'instatech_seo_override_description', 100 );
add_filter( 'rank_math/opengraph/twitter/twitter_description', 'instatech_seo_override_description', 100 );

/**
 * Exact-string copy swaps on the pages above. A string that is not found is left alone, so a later edit in Elementor
 * simply turns the swap off.
 */
function instatech_seo_page_copy( $html ) {
	$o = is_string( $html ) ? instatech_seo_page_override() : null;
	return $o ? strtr( $html, $o['copy'] ) : $html;
}

add_action(
	'template_redirect',
	function () {
		if ( is_admin() || is_feed() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
			return;
		}
		ob_start( 'instatech_seo_page_copy' );
	},
	2
);
