# Checking the Rate Limit 
import requests
import time

# testing the Github thing :https://api.github.com/users/octocat
# 
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
for i in range(30):  # Rapid requests
    response = requests.get(url)
    print(f"Request {i+1}: Status {response.status_code}")
    print(response.headers)
    if response.status_code == 429:
        print("🔥 Rate limit hit! Wait 5 mins.")
        break
    time.sleep(0.5)

'''
I try in Github:
After roughly 50+ It Breaks man 
Request 1: Status 200
Request 2: Status 200
Request 3: Status 200
Request 4: Status 200
Request 5: Status 200
Request 6: Status 200
Request 7: Status 200
Request 8: Status 200
Request 9: Status 200
Request 10: Status 200
Request 11: Status 200
Request 12: Status 200
Request 13: Status 200
Request 14: Status 200
Request 15: Status 200
Request 16: Status 200
Request 17: Status 200
Request 18: Status 200
Request 19: Status 200
Request 20: Status 200
Request 21: Status 200
Request 22: Status 200
Request 23: Status 200
Request 24: Status 200
Request 25: Status 403
Request 26: Status 403
Request 27: Status 403
Request 28: Status 403
Request 29: Status 403
Request 30: Status 403
'''


# I have a Questions Regarding of this and Deepseek Answer it 
# Questions: When i request in python How did the github Knows when i open the browser im blocked too ?

'''
Great question! When you get rate-limited (HTTP 429) while making requests in Python (using requests), 
and then you open the same website in your browser and also get blocked, 
it’s likely because GitHub (or any site) tracks your public IP address and 
applies rate limits across all traffic from that IP—whether it’s from a script or a browser.

1. Rate Limiting by IP Address
GitHub (and many other sites) tracks requests per IP address, not per tool (browser vs. script).
If your Python script sends too many requests too quickly, GitHub will temporarily block your entire IP (affecting all devices/apps using that IP).

2. No Distinction Between Scripts and Browsers
Unless you’re using authentication (API keys, OAuth), GitHub treats all traffic from your IP the same way.
* Example:
    * You send 15 rapid requests in Python → GitHub bans your IP for 1 hour.
    * You open github.com in Chrome → Still blocked because the ban is on your IP, not just your script.
3. Browser vs. Python Requests
    * Browser requests usually include cookies, session data, and a standard User-Agent.
    * Python requests (without custom headers) looks like a basic bot.
    * But if the IP is blocked, it doesn’t matter how "human-like" your browser looks.

Avoid this by 
    1. Slow Down Request ( Adding Delay)
    2. Use Authentication (API Keys / Tokens)
    3. Rotate IPs (Proxies / VPN)
        If you’re testing rate limits, use proxies to avoid your main IP getting banned:
    4. Check response.headers for Rate Limits
        GitHub sends headers like:
            X-RateLimit-Limit → Max allowed requests.
            X-RateLimit-Remaining → Requests left.
            X-RateLimit-Reset → When limits refresh (UTC epoch time).
'''

'''
Few hacks 
1. Mobile Hotspot & IP Ban
Yes! If you use mobile data (hotspot), your phone gets a different public IP from your carrier.
If your script hits a rate limit, only your phone’s IP gets banned (not your home Wi-Fi).
Once you disconnect, the ban won’t affect other devices (since the IP changes).
'''

# My Questions Wether a Website have XrateLimit-Limit
'''
No because that is for Developer Friendly Case 
'''

'''
Inspecting Headers 
import requests
r = requests.get("https://api.github.com/users/octocat")
print(r.headers)  # Look for "X-RateLimit-" or "Retry-After"
'''

# There are many Advance Tips
'''
By Passing Rate Limits 
    1. Rotate User Agents 
    2. Use Proxies/VPN 
    3. Sessions 
    4. Retry-after Header 
    5. Exponential Backoff 
1. Does Rotating User Agents/VPNs/Proxies Change Rate Limits?
Short answer: Sometimes, but not always. It depends on how the site tracks you.

How Sites Track Limits
Method	    Works Against IP Rotation?	    Works Against User-Agent Rotation?
IP-Based	❌ (VPN/Proxy works)	        ✅ (IP change bypasses)
User-Agent	✅ (IP still same)	        ❌ (Rotating UA helps)
Cookies	    ✅ (Persists sessions)	    ✅ (Needs session clearing)
API Keys	❌ (Hard limit per key)	    ❌ (Key = hard limit)

Example:

If a site tracks only by IP, a VPN/proxy will reset your limits.
If it tracks IP + User-Agent + cookies, you’d need to rotate all three.
Warning: Some sites (e.g., Cloudflare) fingerprint browsers (JavaScript checks), making it harder to bypass with just UA/IP changes.

2. Why Use requests.Session() for Rate Limiting?
Sessions help in two key ways:
    A. Connection Reuse (Performance)
        Without sessions: Each requests.get() opens/closes a new TCP connection (slow).
        With sessions: Reuses the same connection (faster, fewer resources).

    B. Persistent Headers/Cookies
        Sites often track sessions via cookies. A Session() object retains them:
        Rate limit bonus: Some sites count requests per session, so a new session may reset counts.

3. Why Are Retry-After + Exponential Backoff "Pro Moves"?
    A. Retry-After Header (Smart Waiting)
        Normal: You guess how long to wait (e.g., time.sleep(60)).
        Pro: You read the server’s exact Retry-After value (no wasted time):
    B. Exponential Backoff (Adaptive Scaling)
        Normal: Fixed delays (e.g., time.sleep(5)). Fails if the site is still busy.
        Pro: Delay doubles each retry (smarter recovery):
        Why this rocks:
            Starts aggressively (1s delay), backs off if bans persist.
    Prevents overwhelming the server and your script.
Key Takeaways
Rotating IPs/User-Agents can bypass limits, but not if the site uses advanced tracking.
Sessions make your scraper faster + mimic real users better.
Retry-After + Exponential Backoff = Respectful, efficient, and avoids permanent bans.
'''

'''
Scaling the Complexity of a Website so i don't over Engineer Things 

How to Scale up in terms of Protections 
Basics first (headers, delays, sessions).
Advanced tricks later (proxies, CAPTCHA solvers) only if needed.

First is just Basic Delay 
Step 2: Add Rate Limit Handling
Step 3 Nuclear Options (Last Resort)
    Proxies/VPNs (for IP bans).
    Selenium (for JS-heavy sites).
    CAPTCHA solvers (e.g., 2Captcha API).
'''

