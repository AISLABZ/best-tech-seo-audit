You are editing the live WordPress site https://instatech.uk in wp-admin. Its structured data lives in WPCode snippets
(WPCode → Code Snippets, admin.php?page=wpcode); most are PHP snippets that build arrays and print JSON-LD.
Work carefully: this is a live shop. Never delete a snippet; deactivate instead. Before editing any snippet, copy its
full code into a text note so it can be restored.

GOAL
Replace the two shop entities that use the old IDs
  https://instatech.uk/locations/#bloomsbury
  https://instatech.uk/locations/#moorgate
with the new IDs
  https://instatech.uk/locations/bloomsbury/#store
  https://instatech.uk/locations/moorgate/#store
so that each shop is defined once, site-wide, and every other snippet points to it.

STEPS
1. Search all WPCode snippets for "locations/#bloomsbury". List every match with its snippet title, then sort them into:
   (a) the snippet that DEFINES both shops as ["MobilePhoneStore","LocalBusiness"] (shown on the homepage, About, the
       service pages, Buy & Sell, Currency exchange);
   (b) the snippet on /locations/ that defines both shops again as "Store";
   (c) every snippet that only REFERENCES the shops (Service "provider", the booking page #16 "about", etc.).
2. Snippet (a): DEACTIVATE it. Do not edit or delete it.
3. Create ONE new snippet: title "InstaTech LocalBusiness schema v2 (21 Oct 2026)", Code Type "HTML Snippet",
   Insert Method "Auto Insert", Location "Site Wide Header", Active. Paste exactly the code at the end of this prompt.
   Do not add an Oxford Circus shop; it is not open.
4. Snippet (b): change only the two "@id" values to the new IDs above. Change nothing else.
5. Every snippet in (c): replace only the ID strings:
     https://instatech.uk/locations/#bloomsbury → https://instatech.uk/locations/bloomsbury/#store
     https://instatech.uk/locations/#moorgate   → https://instatech.uk/locations/moorgate/#store
   Keep PHP syntax intact (quotes, commas, array(...)). Save each one and make sure WPCode reports no error.
6. LiteSpeed Cache → Toolbox → Purge All.
7. Also: Posts → Categories → Uncategorized → Edit → Rank Math → Advanced → tick "No Index" → Update.

CHECK (report the results)
- View the page source of /, /about-us/, /locations/, /book-an-appointment/, /mobile-repair-services/,
  /mobile-repair-services/screen-repair/, /shop/ and /cart/. Each page loads normally.
- No page source contains "locations/#bloomsbury" or "locations/#moorgate".
- The homepage has exactly one node with "@id":"https://instatech.uk/locations/bloomsbury/#store" of type
  MobilePhoneStore, and one for moorgate.
- Run https://search.google.com/test/rich-results on the homepage: two LocalBusiness items, no errors.
- If anything breaks, reactivate snippet (a), deactivate the new v2 snippet, restore edited snippets from your notes.

CODE FOR STEP 3
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":["MobilePhoneStore","ElectronicsStore"],"@id":"https://instatech.uk/locations/bloomsbury/#store","name":"InstaTech Bloomsbury","description":"Walk-in phone, tablet, laptop and smartwatch repair shop in Bloomsbury, minutes from Russell Square and King's Cross. Free diagnostic, no fix no fee, most repairs done while you wait.","url":"https://instatech.uk/locations/bloomsbury/","image":"https://instatech.uk/wp-content/uploads/2026/10/instatech-bloomsbury-shopfront.jpg","logo":"https://instatech.uk/wp-content/uploads/2026/05/WhatsApp-Image-2026-05-07-at-21.04.38-1.png","telephone":"+447377244454","email":"info@instatech.uk","priceRange":"££","currenciesAccepted":"GBP","paymentAccepted":"Cash, Credit Card, Debit Card","address":{"@type":"PostalAddress","streetAddress":"67 Marchmont Street","addressLocality":"London","addressRegion":"Greater London","postalCode":"WC1N 1AP","addressCountry":"GB"},"geo":{"@type":"GeoCoordinates","latitude":51.5253,"longitude":-0.1255},"hasMap":"https://share.google/tBOjmKNlewpVjXnjD","areaServed":[{"@type":"City","name":"London"},{"@type":"Place","name":"Bloomsbury"},{"@type":"Place","name":"King's Cross"}],"parentOrganization":{"@id":"https://instatech.uk/#organization"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"09:30","closes":"21:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"20:00"}],"makesOffer":{"@id":"https://instatech.uk/#repair-catalog"},"sameAs":["https://www.tiktok.com/@instatechlondon"]},{"@type":["MobilePhoneStore","ElectronicsStore"],"@id":"https://instatech.uk/locations/moorgate/#store","name":"InstaTech Moorgate","description":"Walk-in phone, tablet, laptop and smartwatch repair shop on City Road, between Old Street and Moorgate. Free diagnostic, no fix no fee, most repairs done while you wait.","url":"https://instatech.uk/locations/moorgate/","image":"https://instatech.uk/wp-content/uploads/2026/10/instatech-moorgate-shopfront.jpg","logo":"https://instatech.uk/wp-content/uploads/2026/05/WhatsApp-Image-2026-05-07-at-21.04.38-1.png","telephone":"+447508088898","email":"info@instatech.uk","priceRange":"££","currenciesAccepted":"GBP","paymentAccepted":"Cash, Credit Card, Debit Card","address":{"@type":"PostalAddress","streetAddress":"16 City Road","addressLocality":"London","addressRegion":"Greater London","postalCode":"EC1Y 2AA","addressCountry":"GB"},"geo":{"@type":"GeoCoordinates","latitude":51.5222,"longitude":-0.0874},"hasMap":"https://share.google/wKZhs6fusdxbbLy9P","areaServed":[{"@type":"City","name":"London"},{"@type":"Place","name":"Moorgate"},{"@type":"Place","name":"Old Street"},{"@type":"Place","name":"City of London"}],"parentOrganization":{"@id":"https://instatech.uk/#organization"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"09:00","closes":"21:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"20:00"}],"makesOffer":{"@id":"https://instatech.uk/#repair-catalog"},"sameAs":["https://www.tiktok.com/@instatechlondon"]},{"@type":"OfferCatalog","@id":"https://instatech.uk/#repair-catalog","name":"InstaTech repair prices (starting from)","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":"Phone screen replacement","url":"https://instatech.uk/mobile-repair-services/screen-repair/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":49,"priceCurrency":"GBP"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Phone battery replacement","url":"https://instatech.uk/mobile-repair-services/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":29,"priceCurrency":"GBP"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Phone charging port repair","url":"https://instatech.uk/mobile-repair-services/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":35,"priceCurrency":"GBP"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Tablet and iPad screen replacement","url":"https://instatech.uk/tablet-repairs/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":59,"priceCurrency":"GBP"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Laptop and MacBook screen replacement","url":"https://instatech.uk/laptop-desktop-repair/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":79,"priceCurrency":"GBP"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Laptop battery replacement","url":"https://instatech.uk/laptop-desktop-repair/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":49,"priceCurrency":"GBP"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Smartwatch and Apple Watch screen replacement","url":"https://instatech.uk/smartwatch-repair-service/"},"priceSpecification":{"@type":"PriceSpecification","minPrice":49,"priceCurrency":"GBP"}}]}]}</script>
