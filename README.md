
# How to Properly Inspect a Website (For Scraping)

## 1. Static vs. Dynamic Content

- **HTML Structure**
- **Network Requests** (XHR/Fetch for APIs)
- **Disable JavaScript** – Check if content still loads to identify if it's static

## 2. Identify Data Sources

- **Static**: Scrape directly from HTML
- **Dynamic**: Look for hidden APIs (Network tab → JSON responses)
- **Pagination**: Check for URL patterns or "Load More" buttons

## 3. Anti-Scraping Measures

- Look for CAPTCHAs, rate limits, or IP blocking
- Check for required headers (User-Agent, Cookies)

---

# Manual Inspection Techniques

## Static vs. Dynamic Content

### 1. URL Examinations

- Static: `.html`, `.css`, `.js`, `.png`, etc.
- Dynamic: `?`, `&`, `=`, `.php`, `.aspx`, `.jsp`

### 2. View Source

- Static: Full HTML content visible
- Dynamic: Placeholders like `${variable}` or minimal HTML

---

# Experimentation

### Websites:

- [Books to Scrape](https://books.toscrape.com/)
- [Lamudi Philippines](https://www.lamudi.com.ph/)

## Books to Scrape

- URL: Ends with `.html`
- Static content is fully present in the HTML source
- No query parameters
- Content is the same every time

## Lamudi

- URL: `?q=t` — has query parameters
- Minimal initial HTML (skeleton)
- JavaScript loads content after page load
- Often uses APIs and databases

---

# How to Confirm Static vs. Dynamic

- **Disable JavaScript** → No content = Dynamic
- **Network Tab** → Look for XHR/Fetch requests
- **Compare Source vs. Rendered HTML**

---

# XHR and Fetch Explained

## XHR (XMLHttpRequest)

- Old, used by jQuery
- Callback-based
- Still widely used

## Fetch API

- Modern, promise-based
- Cleaner syntax
- Used for JSON & streaming

| Feature       | XHR Requests         | Fetch Requests         |
|--------------|----------------------|------------------------|
| Filter Tab    | "XHR"                | "Fetch/XHR"            |
| Example URL   | `api/search?q=term`  | `graphql` endpoints    |
| Payload       | FormData             | JSON                   |

---

# Bypassing APIs

Some APIs reject scraping—bypassing that is a scraping skill.

---

# Anti-Bot Inspection Checklist

## 1. CAPTCHAs

- Visit site normally or incognito
- Frequent refreshes may trigger CAPTCHAs
- Tips:
  - Slow down requests
  - Use rotating proxies
  - Use Selenium/Playwright stealth mode

## 2. IP Blocking

- Use VPN/proxy to test
- Blocked after a few requests → IP-based
- Tips:
  - Residential proxies
  - Delay requests

## 3. Rate Limiting

- Refresh rapidly (10+ times)
- Watch for:
  - `429 Too Many Requests`
  - Cloudflare checks
- Tips:
  - Use `time.sleep()`
  - Use exponential backoff

## 4. Required Headers & Cookies

- DevTools → Network tab → Reload
- Inspect request headers:
  - User-Agent, Referer, Authorization
  - Cookies like `session_id`, `token`

---

# Manual vs. Systematic Testing

## Manual Inspection (Quick Pass)

### A. DevTools – Network Tab

- Watch for:
  - `429 Too Many Requests` → Rate limiting
  - `403 Forbidden` → IP/User-Agent blocking
  - Cloudflare checks
  - Tokens like:
    - `csrf_token`
    - `__cf_bm`
    - `ak_bmsc`

### B. Disable JavaScript

- If site breaks → Client-side rendering
- If CAPTCHA appears → Bot detection triggered

### C. User-Agent Switching

- Use browser extensions
- Test different devices/browsers

---

# Why I Built This Website

To test whether I can handle scraping complex websites. Many sites are hard to scrape, and I needed a practical way to learn and test my skills because time is precious—I don’t want to waste it on unproductive efforts.

---
