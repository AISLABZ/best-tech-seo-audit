<?php
/**
 * Plugin Name: InstaTech SEO fixes
 * Description: Audit fixes from 21 Oct 2026. Noindexes template residue, fills missing meta descriptions,
 *              and completes the Organization and author entities in Rank Math's schema.
 * Version:     1.0.0
 *
 * Install: upload to wp-content/mu-plugins/ (create the folder if it does not exist). Must-use plugins
 * load automatically and cannot be deactivated from wp-admin. Every hook below is a Rank Math filter,
 * so the file does nothing if Rank Math is ever removed. Purge LiteSpeed Cache after uploading.
 */

defined( 'ABSPATH' ) || exit;

/*
 * -------------------------------------------------------------------------
 * Settings. Edit these, nothing else.
 * -------------------------------------------------------------------------
 */

// Profiles that describe the same business. Add each one as it goes live
// (Google Business Profiles, Bing Places, Apple Maps, Trustpilot, Yelp, Instagram, Facebook...).
const INSTATECH_SAME_AS = array(
	'https://www.tiktok.com/@instatechlondon',
);

// Shown as the blog author until a named technician profile exists. Replace with a real person's name
// (and set that person as the post author in WordPress) as soon as possible: a named expert is the point.
const INSTATECH_FALLBACK_AUTHOR = 'InstaTech Repair Team';

// Indexable URLs that are template residue or empty archives.
const INSTATECH_NOINDEX_PATHS = array(
	'/blog-standard/',
	'/category/uncategorized/',
);

/*
 * -------------------------------------------------------------------------
 * 1. Noindex template residue and keep it out of the sitemap.
 * -------------------------------------------------------------------------
 */

function instatech_request_path() {
	$uri  = isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '/';
	$path = wp_parse_url( $uri, PHP_URL_PATH );
	return trailingslashit( $path ? $path : '/' );
}

add_filter(
	'rank_math/frontend/robots',
	function ( $robots ) {
		if ( in_array( instatech_request_path(), INSTATECH_NOINDEX_PATHS, true ) ) {
			$robots['index']  = 'noindex';
			$robots['follow'] = 'follow';
		}
		return $robots;
	}
);

add_filter(
	'rank_math/sitemap/entry',
	function ( $url, $type, $object ) {
		if ( ! empty( $url['loc'] ) ) {
			$path = trailingslashit( (string) wp_parse_url( $url['loc'], PHP_URL_PATH ) );
			if ( in_array( $path, INSTATECH_NOINDEX_PATHS, true ) ) {
				return false;
			}
		}
		return $url;
	},
	10,
	3
);

/*
 * -------------------------------------------------------------------------
 * 2. Meta descriptions for archives and products that have none.
 *    Only used when the Rank Math field is empty, so anything written in
 *    wp-admin later takes precedence automatically.
 * -------------------------------------------------------------------------
 */

const INSTATECH_TERM_DESCRIPTIONS = array(
	// Product categories.
	'cables'                  => 'Charging and data cables for iPhone, Android, laptops and tablets: USB-C, Lightning, MagSafe, HDMI and Ethernet. From InstaTech, central London.',
	'audio'                   => 'Earphones, headphones, speakers and audio adapters for iPhone and Android, from InstaTech, the phone repair and accessories shop in central London.',
	'chargers'                => 'Phone, laptop, wireless and car chargers, including USB-C PD fast chargers with UK plugs. Buy online or in store at InstaTech, central London.',
	'in-car'                  => 'Car phone mounts and dual-USB car chargers to keep your phone powered and in view on the road. Shop in-car accessories at InstaTech London.',
	'miscellaneous'           => 'Phone and computer extras: stylus pens, travel adapters, hubs and more. Shop online or pick them up at InstaTech in central London.',
	'usb-c-pd-cable'          => 'USB-C to USB-C power delivery cables for fast charging phones, tablets and laptops. Durable lengths for every setup, from InstaTech London.',
	'usb-a-cables'            => 'USB-A charging and data cables for Lightning, USB-C and Micro USB devices. Reliable replacements for older chargers, from InstaTech London.',
	'computer-cables'         => 'HDMI, Ethernet and USB-C hub cables for laptops, desktops and monitors. Shop computer cables at InstaTech, central London.',
	'audio-cables'            => 'USB-C and Lightning to 3.5mm audio cables and splitters, so you can use wired headphones with a modern phone. From InstaTech London.',
	'for-iphone-c-type'       => 'USB-C to Lightning cables for fast charging iPhone and iPad with a USB-C power adapter. Shop iPhone cables at InstaTech London.',
	'for-c-c-phones'          => 'USB-C to USB-C cables for Samsung, Pixel, iPhone 15 and later, and other USB-C phones. Fast charging and data, from InstaTech London.',
	'smart-watch-usb-c'       => 'USB-C smartwatch charging cables for Apple Watch and other wearables. Replace a lost or worn charger at InstaTech, central London.',
	'for-iphones-a-type'      => 'USB-A to Lightning cables for charging iPhone and iPad from a standard USB plug, car port or computer. From InstaTech London.',
	'for-usb-c-a-devices'     => 'USB-A to USB-C cables for charging USB-C phones and tablets from standard USB plugs, laptops and car ports. From InstaTech London.',
	'for-micro-usb-a-devices' => 'USB-A to Micro USB cables for older Android phones, speakers, power banks and accessories. Shop at InstaTech, central London.',
	'smart-watch-usb-a'       => 'USB-A smartwatch charging cables for Apple Watch and other wearables. Replace a lost or worn charger at InstaTech, central London.',
	'usb-c-hubs'              => 'USB-C hubs and multi-port adapters adding HDMI, USB-A and card readers to MacBooks and laptops. Shop at InstaTech London.',
	'magsafe-cables'          => 'MagSafe charging cables and pads for iPhone 12 and later. Fast magnetic wireless charging, from InstaTech, central London.',
	'ethernet-cables'         => 'Ethernet cables from 1 Gbps to 40 Gbps in 2m and 5m lengths for stable wired internet. Shop at InstaTech, central London.',
	'hdmi-cables'             => 'HDMI and USB-C to HDMI cables for connecting laptops, phones and tablets to a TV or monitor. From InstaTech, central London.',
	'audio-adapters'          => 'Lightning and USB-C to 3.5mm headphone adapters and charging splitters for iPhone and Android. Shop at InstaTech London.',
	'wired-earphones'         => 'Wired earphones with 3.5mm, USB-C and Lightning connectors, with built-in mic for calls. Shop at InstaTech, central London.',
	'wireless-earphones'      => 'Wireless Bluetooth earphones and headphones for iPhone and Android, with clear calls and long battery life. From InstaTech London.',
	'wireless-speakers'       => 'Portable Bluetooth wireless speakers for home, travel and parties. Shop wireless speakers at InstaTech, central London.',
	'power-bank'              => 'Portable power banks from 10,000mAh to 20,000mAh with fast USB-C charging for phones and tablets. Shop at InstaTech London.',
	'phone-chargers'          => 'UK plug phone chargers including 20W to 45W USB-C PD fast chargers for iPhone, Samsung and Pixel. From InstaTech London.',
	'wireless-charger'        => 'Qi and MagSafe-compatible wireless chargers for iPhone, Samsung and earbuds. Shop wireless chargers at InstaTech, central London.',
	'macbook-laptop-charger'  => 'Replacement MacBook and laptop chargers, including USB-C PD power adapters. Get the right charger at InstaTech, central London.',
	'car-mount'               => 'Car phone mounts and holders for dashboards and air vents, keeping navigation in view. Shop car mounts at InstaTech London.',
	'car-chargers'            => 'Fast dual-port car chargers with USB-A and USB-C for charging phones on the move. Shop car chargers at InstaTech, central London.',
	'for-stylus-pen'          => 'Stylus pens for iPad, iOS and Android tablets and phones, for drawing and note-taking. Shop stylus pens at InstaTech London.',
	'computer-accessories'    => 'Computer accessories for laptops and desktops: USB-C hubs, HDMI and Ethernet cables, chargers and adapters. From InstaTech London.',
	'lifestyle-travel'        => 'Travel adapters, power banks and travel tech for UK and worldwide trips. Shop lifestyle and travel accessories at InstaTech London.',
	// Blog categories.
	'gadgets'                 => 'Guides to chargers, power banks, earphones and other phone gadgets: what to buy and what works, from the InstaTech repair team in London.',
	'devices'                 => 'Practical advice on phones, tablets, laptops and smartwatches: buying, troubleshooting and care, from InstaTech, central London.',
	'tips'                    => 'Quick tips to fix common phone, tablet and laptop problems yourself, and when to bring it in. From the InstaTech repair team, London.',
	'repair'                  => 'Repair guides and costs for phone screens, batteries, charging ports and water damage, from InstaTech, the walk-in repair shop in London.',
	'repair-lab'              => 'Repair Lab: deeper write-ups from InstaTech technicians on logic boards, part pairing and tricky repairs, from our central London shops.',
);

const INSTATECH_PRODUCT_DESCRIPTIONS = array(
	'me-02-stereo-earphones'                              => 'ME-02 stereo wired earphones with 3.5mm jack and in-line mic for calls and music. Buy online or in store at InstaTech, central London.',
	'h1-stereo-wireless-headphones'                       => 'H1 stereo wireless Bluetooth headphones with built-in mic and long battery life. Buy online or in store at InstaTech, central London.',
	'world-travel-adapter-series-x'                       => 'World Travel Adapter Series X: one plug for UK, EU, US and AU sockets with USB charging ports. Buy at InstaTech, central London.',
	'world-travel-adapter-series-x-2'                     => 'World Travel Adapter Series X: one plug for UK, EU, US and AU sockets with USB charging ports. Buy at InstaTech, central London.',
	'compact-energybar-t10-10000mah'                      => 'Compact EnergyBar T10 10,000mAh power bank: pocket-sized backup power for phones and earbuds. Buy at InstaTech, central London.',
	'energybar-t20-20000mah'                              => 'EnergyBar T20 20,000mAh power bank: several full phone charges for travel and long days out. Buy at InstaTech, central London.',
	'ethernet-cable-1-gbps-speed-2m'                      => '2m Ethernet cable rated to 1 Gbps for stable wired internet to routers, consoles and PCs. Buy at InstaTech, central London.',
	'ethernet-cable-1-gbps-speed-2m-2'                    => '2m Ethernet cable rated to 1 Gbps for stable wired internet to routers, consoles and PCs. Buy at InstaTech, central London.',
	'ethernet-cable-1-gbps-speed-5m'                      => '5m Ethernet cable rated to 1 Gbps for stable wired internet to routers, consoles and PCs. Buy at InstaTech, central London.',
	'ethernet-cable-1-gbps-speed-5m-2'                    => '5m Ethernet cable rated to 1 Gbps for stable wired internet to routers, consoles and PCs. Buy at InstaTech, central London.',
	'ethernet-cable-10-gbps-speed-2m'                     => '2m Ethernet cable rated to 10 Gbps for fast, low-latency wired connections. Buy online or in store at InstaTech, central London.',
	'ethernet-cable-10-gbps-speed-2m-2'                   => '2m Ethernet cable rated to 10 Gbps for fast, low-latency wired connections. Buy online or in store at InstaTech, central London.',
	'ethernet-cable-10-gbps-speed-5m'                     => '5m Ethernet cable rated to 10 Gbps for fast, low-latency wired connections. Buy online or in store at InstaTech, central London.',
	'ethernet-cable-10-gbps-speed-5m-2'                   => '5m Ethernet cable rated to 10 Gbps for fast, low-latency wired connections. Buy online or in store at InstaTech, central London.',
	'ethernet-cable-40-gbps-speed'                        => 'Ethernet cable rated to 40 Gbps for high-speed networking and data-heavy setups. Buy online or in store at InstaTech, central London.',
	'k10-stylus-pen-for-ipad'                             => 'K10 stylus pen for iPad with palm rejection and fine tip for notes and drawing. Buy online or in store at InstaTech, central London.',
	'k503-universal-stylus-pen-for-ios-and-android-devices' => 'K503 universal stylus pen for iPhone, iPad and Android touchscreens. Buy online or in store at InstaTech, central London.',
	'cc25-dual-usb-car-charger-4-8-a'                     => 'CC25 dual USB car charger with 4.8A total output to charge two phones at once on the road. Buy at InstaTech, central London.',
	'45w-usb-c-pd-home-charger-uk'                        => '45W USB-C PD home charger with UK plug: fast charges iPhone, Samsung, iPad and many laptops. Buy at InstaTech, central London.',
	'world-traveller-to-uk'                               => 'World-to-UK travel adapter for using EU, US and other foreign plugs in UK sockets. Buy online or in store at InstaTech, central London.',
	'dj-boombox-wireless-speaker'                         => 'DJ-BoomBox wireless Bluetooth speaker with big sound for parties and outdoors. Buy online or in store at InstaTech, central London.',
	'me-08c-usb-c-wired-earphones'                        => 'ME-08C USB-C wired earphones with mic for phones without a headphone jack. Buy online or in store at InstaTech, central London.',
	'z-series-usb-c-to-3-5mm-audio-cable-1-2m'            => 'Z-series 1.2m USB-C to 3.5mm audio cable for connecting a USB-C phone to speakers or car AUX. Buy at InstaTech, central London.',
	'z-series-usb-c-to-3-5mm-audio-cable-1-2m-2'          => 'Z-series 1.2m USB-C to 3.5mm audio cable for connecting a USB-C phone to speakers or car AUX. Buy at InstaTech, central London.',
	'standard-pd-cable-lightning-to-usb-c-1-2m'           => '1.2m USB-C to Lightning PD cable for fast charging iPhone and iPad with a USB-C adapter. Buy at InstaTech, central London.',
	'z-series-lightning-to-usb-c-pd-cable-1-2m'           => 'Z-Series 1.2m Lightning to USB-C PD cable for fast charging iPhone and iPad. Buy online or in store at InstaTech, central London.',
);

add_filter(
	'rank_math/frontend/description',
	function ( $description ) {
		if ( '' !== trim( (string) $description ) ) {
			return $description;
		}
		if ( is_category() || ( function_exists( 'is_product_category' ) && is_product_category() ) ) {
			$slug = get_queried_object()->slug ?? '';
			return INSTATECH_TERM_DESCRIPTIONS[ $slug ] ?? $description;
		}
		if ( is_singular( 'product' ) ) {
			$slug = get_post_field( 'post_name', get_queried_object_id() );
			return INSTATECH_PRODUCT_DESCRIPTIONS[ $slug ] ?? $description;
		}
		return $description;
	}
);

/*
 * -------------------------------------------------------------------------
 * 3. Complete the Organization and author nodes in Rank Math's schema graph.
 * -------------------------------------------------------------------------
 */

add_filter(
	'rank_math/json_ld',
	function ( $data ) {
		foreach ( $data as $key => $node ) {
			if ( ! is_array( $node ) || empty( $node['@type'] ) ) {
				continue;
			}
			$types = (array) $node['@type'];

			if ( in_array( 'Organization', $types, true ) ) {
				$data[ $key ]['name']          = 'InstaTech';
				$data[ $key ]['alternateName'] = 'InstaTech London';
				$data[ $key ]['email']         = 'info@instatech.uk';
				$data[ $key ]['sameAs']        = array_values( array_unique( array_merge( (array) ( $node['sameAs'] ?? array() ), INSTATECH_SAME_AS ) ) );
				$data[ $key ]['contactPoint']  = array(
					array(
						'@type'             => 'ContactPoint',
						'contactType'       => 'customer service',
						'telephone'         => '+447377244454',
						'email'             => 'info@instatech.uk',
						'areaServed'        => 'GB',
						'availableLanguage' => 'en',
					),
				);
			}

			if ( in_array( 'Person', $types, true ) && '' === trim( (string) ( $node['name'] ?? '' ) ) ) {
				$data[ $key ]['name']     = INSTATECH_FALLBACK_AUTHOR;
				$data[ $key ]['worksFor'] = array( '@id' => 'https://instatech.uk/#organization' );
			}
		}
		return $data;
	},
	99
);
