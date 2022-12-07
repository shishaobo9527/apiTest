import requests

params = {
    "type": "movie",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 0
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
}
r = requests.get("https://movie.douban.com/j/search_subjects", params=params, headers=headers)
print(r.status_code)
print(r.json())
