import requests

url = "https://www.yellow-pages.ph/category/photographic-services/page-1"

# Try without User-Agent
response = requests.get(url)
print(response.status_code)  # 200 = OK, 403/429 = Blocked

# Try with a fake User-Agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(url, headers=headers)
print(response.status_code)  # If 200 now, User-Agent was needed!

'''
Output
403
200
'''

'''
In Terms of Inspection i have some Vague Idea on this 
'''