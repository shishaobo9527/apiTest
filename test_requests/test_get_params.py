import requests

params = {"mobile": "13227293721",
          "app_id": "rgihdrm0kslojqvm",
          "app_secret": "WnhrK251TWlUUThqaVFWbG5OeGQwdz09"
          }
r = requests.get("https://www.mxnzp.com/api/mobile_location/aim_mobile", params=params)
print(r.status_code)
print(r.json())
