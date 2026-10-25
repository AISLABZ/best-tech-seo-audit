"""Assemble an InstaTech service page block and a one-shot WordPress creator plugin.

The page reuses the screen-repair template's stylesheet and script (instatech/pages/assets/) so the design matches
exactly. The JSON-LD FAQ is generated from the visible FAQ so the two can never drift apart.

Usage: python3 instatech/tools/build_service_page.py battery-replacement
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "battery-replacement": {
        "title": "Battery Replacement",
        "parent_id": 75806,
        "parent_path": "mobile-repair-services",
        "seo_title": "Phone Battery Replacement London – Same Day | InstaTech",
        "seo_description": (
            "New phone battery fitted in 20–40 minutes at our Bloomsbury and Moorgate shops. "
            "Free diagnostic, no fix no fee. Walk in 7 days a week, open until 9pm."
        ),
        "focus_keyword": "phone battery replacement london",
        "service_name": "Phone battery replacement",
        "service_type": "Mobile phone battery replacement",
        "service_description": (
            "Phone battery replacement in central London for iPhone, Samsung, Google Pixel and other Android "
            "phones, usually in 20 to 40 minutes, with a free diagnostic and no fix, no fee."
        ),
        "journey_step_3": "Battery replaced",
        "approved": "approved by the owner on 21 Oct 2026",
    },
    "charging-port-repair": {
        "title": "Charging Port Repair",
        "parent_id": 75806,
        "parent_path": "mobile-repair-services",
        "seo_title": "Phone Charging Port Repair London | InstaTech",
        "seo_description": (
            "Phone charging only at an angle or not at all? Port cleaned or replaced at our Bloomsbury and Moorgate "
            "shops. Free diagnostic, no fix no fee. Walk in 7 days."
        ),
        "focus_keyword": "phone charging port repair london",
        "service_name": "Phone charging port repair",
        "service_type": "Mobile phone charging port repair",
        "service_description": (
            "Phone charging port cleaning, repair and replacement in central London for iPhone, Samsung, Google Pixel "
            "and other phones, with a free diagnostic and no fix, no fee."
        ),
        "journey_step_3": "Port cleaned or replaced",
        "approved": "approved by the owner",
    },
    "water-damage-repair": {
        "title": "Water Damage Repair",
        "parent_id": 75806,
        "parent_path": "mobile-repair-services",
        "seo_title": "Water Damaged Phone Repair London | InstaTech",
        "seo_description": (
            "Dropped your phone in water or spilled a drink on it? Switch it off and bring it to Bloomsbury or "
            "Moorgate. Free diagnostic, no fix no fee. Open 7 days."
        ),
        "focus_keyword": "water damaged phone repair london",
        "service_name": "Water damaged phone repair",
        "service_type": "Mobile phone liquid damage repair",
        "service_description": (
            "Water and liquid damaged phone repair in central London for iPhone, Samsung, Google Pixel and other "
            "phones: opened, cleaned of liquid and corrosion, and tested, with a free diagnostic and no fix, no fee."
        ),
        "journey_step_3": "Cleaned and repaired",
        "approved": "approved by the owner",
    },
}

SHOPS = [
    {
        "@type": ["MobilePhoneStore", "LocalBusiness"],
        "name": "InstaTech Bloomsbury",
        "telephone": "+447377244454",
        "address": {"@type": "PostalAddress", "streetAddress": "67 Marchmont Street", "addressLocality": "London",
                    "postalCode": "WC1N 1AP", "addressCountry": "GB"},
        "hasMap": "https://maps.google.com/?cid=10641785332690239296",
    },
    {
        "@type": ["MobilePhoneStore", "LocalBusiness"],
        "name": "InstaTech Moorgate",
        "telephone": "+447508088898",
        "address": {"@type": "PostalAddress", "streetAddress": "16 City Road", "addressLocality": "London",
                    "postalCode": "EC1Y 2AA", "addressCountry": "GB"},
        "hasMap": "https://maps.google.com/?cid=8404697699929828128",
    },
]


def text(fragment):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def faq_from_body(body):
    items = re.findall(
        r'<div class="q"><button[^>]*>(.*?)<svg.*?</button>\s*<div class="a"><div>(.*?)</div></div>', body, re.S
    )
    if not items:
        sys.exit("no FAQ items found in body")
    return [{"@type": "Question", "name": text(q), "acceptedAnswer": {"@type": "Answer", "text": text(a)}}
            for q, a in items]


def build(slug):
    cfg = PAGES[slug]
    url = f"https://instatech.uk/{cfg['parent_path']}/{slug}/"
    body = (ROOT / "pages" / f"{slug}.body.html").read_text()
    css = (ROOT / "pages" / "assets" / "itx-service.css").read_text()
    js = (ROOT / "pages" / "assets" / "itx-service.js").read_text()
    if "'Screen replaced'" not in js:
        sys.exit("template script changed: journey label not found")
    js = js.replace("'Screen replaced'", json.dumps(cfg["journey_step_3"]).replace('"', "'"))

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "@id": url + "#service", "name": cfg["service_name"],
             "serviceType": cfg["service_type"], "description": cfg["service_description"],
             "areaServed": {"@type": "City", "name": "London"}, "provider": SHOPS, "url": url},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://instatech.uk/"},
                {"@type": "ListItem", "position": 2, "name": "Mobile Repair Services",
                 "item": f"https://instatech.uk/{cfg['parent_path']}/"},
                {"@type": "ListItem", "position": 3, "name": cfg["title"], "item": url}]},
            {"@type": "FAQPage", "mainEntity": faq_from_body(body)},
        ],
    }

    # Programme rule: no prices in new content.
    visible = text(body) + json.dumps(schema)
    if re.search(r"£\s?\d|\bfrom £|priceSpecification|\"offers\"", visible):
        sys.exit("price found in page content: programme rule violated")

    block = (
        "<!-- wp:html -->\n<style>" + css + "</style>\n" + body
        + '\n<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>\n"
        + "<script>" + js + "</script>\n<!-- /wp:html -->\n"
    )
    if "INSTATECH_PAGE_HTML" in block:
        sys.exit("heredoc terminator collides with content")
    (ROOT / "pages" / f"{slug}.block.html").write_text(block)

    php = f"""<?php
/**
 * Plugin Name: InstaTech page creator: {cfg['title']}
 * Description: One-shot. Creates /{cfg['parent_path']}/{slug}/ once ({cfg['approved']}) and sets its
 *              Rank Math title, description and focus keyword. Does nothing once the page exists. Generated by
 *              instatech/tools/build_service_page.py. Safe to leave in place; replace with an empty file to retire it.
 */

defined( 'ABSPATH' ) || exit;

add_action(
	'init',
	function () {{
		if ( get_option( 'instatech_page_created_{slug}' ) ) {{
			return;
		}}
		if ( get_page_by_path( '{cfg['parent_path']}/{slug}', OBJECT, 'page' ) ) {{
			update_option( 'instatech_page_created_{slug}', 'exists', false );
			return;
		}}
		// add_option fails if the key exists, so only one request can claim the creation.
		if ( ! add_option( 'instatech_page_creating_{slug}', time(), '', false ) ) {{
			return;
		}}

		$content = <<<'INSTATECH_PAGE_HTML'
{block}INSTATECH_PAGE_HTML;

		$kses = has_filter( 'content_save_pre', 'wp_filter_post_kses' );
		if ( $kses ) {{
			kses_remove_filters();
		}}
		$id = wp_insert_post(
			array(
				'post_type'      => 'page',
				'post_status'    => 'publish',
				'post_title'     => {json.dumps(cfg['title'])},
				'post_name'      => '{slug}',
				'post_parent'    => {cfg['parent_id']},
				// wp_insert_post() unslashes its input, which would strip the backslashes in the page's script.
				'post_content'   => wp_slash( $content ),
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			),
			true
		);
		if ( $kses ) {{
			kses_init_filters();
		}}

		if ( is_wp_error( $id ) ) {{
			delete_option( 'instatech_page_creating_{slug}' );
			update_option( 'instatech_page_error_{slug}', $id->get_error_message(), false );
			return;
		}}

		update_post_meta( $id, 'rank_math_title', {json.dumps(cfg['seo_title'], ensure_ascii=False)} );
		update_post_meta( $id, 'rank_math_description', {json.dumps(cfg['seo_description'], ensure_ascii=False)} );
		update_post_meta( $id, 'rank_math_focus_keyword', {json.dumps(cfg['focus_keyword'])} );
		update_option( 'instatech_page_created_{slug}', (string) $id, false );
		delete_option( 'instatech_page_creating_{slug}' );
	}},
	20
);
"""
    out = ROOT / "wp" / "mu-plugins" / f"instatech-create-{slug}.php"
    out.write_text(php)
    print(f"block {len(block)} bytes, faq {len(schema['@graph'][2]['mainEntity'])} items -> {out.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    build(sys.argv[1])
