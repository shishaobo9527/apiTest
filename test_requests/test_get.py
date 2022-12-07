import requests

r = requests.get("http://api.github.com/events")
print(r.status_code)  # 返回状态码
print(r.text)  # 返回文本
print(r.json())  # 返回json数据
