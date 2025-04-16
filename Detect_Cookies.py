import requests

# response = requests.get(url)
# print(response.status_code)
# cookies = {"session_id": "123abc", "token": "xyz456"}
# response = requests.get(url, cookies=cookies)
# print(response.status_code)

# s = requests.Session()
# s.headers.update({"User-Agent": "Mozilla/5.0"})
# s.cookies.update({"session": "123"})
# response = s.get(url)
# print(response.status_code)

import requests
response = requests.get("http://httpbin.org/cookies", cookies={"test": "123"})
print(response.text)

'''
I Really Don't have Understanding in Terms of Cookies Huh 

Practice
(Easy) http://httpbin.org/cookies
import requests
response = requests.get("http://httpbin.org/cookies", cookies={"test": "123"})
print(response.text)  # Output: {"cookies": {"test": "123"}}
(Intermediate) https://httpbin.org/headers
response = requests.get("https://httpbin.org/headers", cookies={"user": "scraper"})
print(response.json())  # Check "headers" and "Cookie" field.
(Advanced) https://httpbin.org/cookies/set/name/value
session = requests.Session()
response = session.get("https://httpbin.org/cookies/set/test_cookie/12345")
print(session.cookies)  # Output: <Cookies[<Cookie test_cookie=12345 for httpbin.org/>]>

Real World Sites
https://httpbin.org/
https://drdobbs.com/

session = requests.Session()
response = session.get("https://httpbin.org/cookies/set/test_cookie/12345")
print(session.cookies)  # Output: <Cookies[<Cookie test_cookie=12345 for httpbin.org/>]>

'''