<?php
// Stubbed-WordPress tests for v1.2.0 (Google Maps links pointed at each shop's listing).
// Run: php instatech/wp/tests/harness-v12.php instatech/wp/mu-plugins/instatech-seo-fixes.php
define( 'ABSPATH', '/x/' );
function add_filter( $h, $cb, $p = 10, $n = 1 ) {}
function add_action( $h, $cb, $p = 10, $n = 1 ) {}
require $argv[1];

$fail = 0;
function check( $label, $cond ) { global $fail; echo ( $cond ? 'PASS ' : 'FAIL ' ), $label, "\n"; if ( ! $cond ) { $fail++; } }

$b = 'https://maps.google.com/?cid=10641785332690239296';
$m = 'https://maps.google.com/?cid=8404697699929828128';

$home = '<a href="https://www.google.com/maps/place/instaTech+-+(Bloomsbury)/">Find us</a>'
	. '<script type="application/ld+json">{"hasMap":"https://www.google.com/maps/place/instaTech+-+Moorgate/","sameAs":["https://www.google.com/maps/place/instaTech+-+(Bloomsbury)/"]}</script>';
$o    = instatech_seo_maps_links( $home );
check( 'homepage name-search links -> cid', 2 === substr_count( $o, $b ) && 1 === substr_count( $o, $m ) );
check( 'no name-search links left', false === strpos( $o, '/maps/place/instaTech' ) );

$loc = '<a href="https://www.google.com/maps?q=67+Marchmont+Street,+London+WC1N+1AP">Open in Maps</a>'
	. '<iframe src="https://www.google.com/maps?q=67+Marchmont+Street,+London+WC1N+1AP&amp;output=embed"></iframe>'
	. '<div data-s="{&quot;hasMap&quot;:&quot;https://www.google.com/maps?q=67+Marchmont+Street,+London+WC1N+1AP&quot;}"></div>'
	. '<script>{"hasMap":"https://www.google.com/maps?q=16+City+Road,+London+EC1Y+2AA"}</script>'
	. '<a href="https://www.google.com/maps/dir/?api=1&amp;destination=67+Marchmont+Street+London+WC1N+1AP">Directions</a>'
	. '<a href="https://www.google.com/maps/dir/?api=1&amp;destination=16+City+Road+London+EC1Y+2AA">Directions</a>';
$o   = instatech_seo_maps_links( $loc );
check( 'address link -> cid', false !== strpos( $o, 'href="' . $b . '">Open in Maps' ) );
check( 'embed iframe untouched', false !== strpos( $o, 'maps?q=67+Marchmont+Street,+London+WC1N+1AP&amp;output=embed' ) );
check( 'entity-encoded schema -> cid', false !== strpos( $o, '&quot;' . $b . '&quot;' ) );
check( 'Moorgate schema -> cid', false !== strpos( $o, '"hasMap":"' . $m . '"' ) );
check( 'Bloomsbury directions pinned', false !== strpos( $o, 'WC1N+1AP&amp;destination_place_id=ChIJg5Ii0NUbdkgRQL_2omA3r5M"' ) );
check( 'Moorgate directions pinned', false !== strpos( $o, 'EC1Y+2AA&amp;destination_place_id=ChIJm5ZiHwAddkgRICvcMAd8o3Q"' ) );
check( 'idempotent', $o === instatech_seo_maps_links( $o ) );

$oc = '<a href="https://www.google.com/maps/search/?api=1&amp;query=22+Great+Castle+Street+London+W1G+0HY">Map</a>';
check( 'Oxford Circus untouched (no listing yet)', $oc === instatech_seo_maps_links( $oc ) );
check( 'pages without Google links untouched', '<p>hello</p>' === instatech_seo_maps_links( '<p>hello</p>' ) );

exit( $fail ? 1 : 0 );
