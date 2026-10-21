# Google Maps & reviews playbook — Best Tech, Piccadilly Circus

Prepared 21 October 2026 from a live Google Maps scan (Apify, 14 listings around Piccadilly Circus).

## Where Best Tech stands

| Listing | Rating | Reviews | Photos | Distance |
|---|---|---|---|---|
| **Best Tech (Inside Piccadilly Circus Underground Station)** | **5.0** | **135** | **13** | — |
| tSmart, 33 Coventry St | 4.9 | 5,216 | 246 | ~2 min walk |
| Covent Garden Tech Repairs | 4.8 | 427 | 234 | ~8 min |
| iMagic, Charing Cross Rd | 4.7 | 224 | 98 | ~6 min |
| CMLink, Shaftesbury Ave | 4.8 | 213 | 366 | ~4 min |
| Mayfair Mobile Repair Centre | 4.8 | 40 | 21 | ~6 min |

**Key finding:** in the scan for "phone repair near Piccadilly Circus London", Best Tech did
not appear in the first 13 results. It only appeared when searched by name. (Maps results vary
with the searcher's exact location; a phone held inside the station will see a different order,
but the gap is real.)

Why: Google ranks local results on **relevance, distance and prominence**. Best Tech wins on
distance and rating, but loses heavily on prominence — review volume (135 vs 5,216 next door),
photos (13 vs 230+) and category coverage.

## Fixes for the owner to make in Google Business Profile (≈30 minutes)

1. **Categories** — primary stays *Mobile phone repair shop*. Add: *Phone repair service*,
   *Screen repair service*, *Electronics repair shop*, *Data recovery service*,
   *Laptop repair service* (if offered as a category). **Remove "Currency exchange service"** —
   it dilutes relevance and does not describe the business.
2. **Photos** — upload 30+ real photos over the next fortnight: shopfront from the concourse,
   the counter, technicians at work, before/after repairs, the station entrance signs.
   Add 3–5 new photos every week thereafter.
3. **Services list** — add each repair as a named service with a one-line description:
   iPhone screen repair, Samsung screen repair, phone battery replacement, charging port repair,
   water damage repair, MacBook repair, iPad repair, data recovery, trade-ins.
4. **Products** — add accessories, refurbished phones and trade-ins with photos.
5. **Q&A** — seed 5 questions and answer them as the owner (Do I need an appointment? How long
   does a screen take? Do you fix iPhone 17? Are you inside the station? No fix no fee?).
6. **Attributes** — confirm "Walk-ins welcome", accessibility, payment types.
7. **Posts** — keep the weekly posts already running (good practice, keep going).
8. **Booking link** — already set to /contact#book with UTM tags. Keep.

## Review engine (the single biggest lever)

Target: **+25 reviews a month** (≈1 per working day). At that pace Best Tech passes 400 reviews
within a year — enough to compete for the local pack while keeping the 5.0 average.

**Rules:** ask every customer, at the counter, at the moment they see the repaired device.
Never offer anything in exchange for a review and never ask only happy customers — both breach
Google policy and UK consumer law (DMCC Act 2024).

**Short review link:** in Google Business Profile → *Ask for reviews* → copy the link and put it
in a QR code on the counter and in the WhatsApp template below.

### WhatsApp / SMS after collection (send same day)
> Hi {first name}, thanks for choosing Best Tech today — hope your {device} is working perfectly.
> If you have a moment, a quick Google review really helps a small shop inside the station:
> {review link}
> Any problem at all, just reply here. — Best Tech, Unit 4, Piccadilly Circus

### At the counter (staff script)
> "You're all set. If you're happy with it, a Google review helps us a lot — this QR code takes
> you straight there."

### Reply templates (reply to every review within 48 hours)
- **5★:** "Thank you, {name}. Glad we got your {device} sorted the same day — see you if you ever
  need us again at Unit 4, Piccadilly Circus."
- **4★:** "Thanks, {name}. Appreciate the feedback — if there's anything we could have done
  better, reply here or call 020 3417 7090."
- **1–3★:** "Sorry to hear this, {name}. We'd like to put it right — please call 020 3417 7090 or
  WhatsApp 07423 230703 and ask for the manager."

## How to measure it

- Monthly: review count, average rating, photo count (re-run the Maps scan).
- Google Business Profile → Performance: calls, direction requests, website clicks.
- GA4: `booking_cta_click`, `phone_call_click`, `whatsapp_click` from `utm_source=google&utm_medium=organic&utm_campaign=gbp-piccadilly`.
