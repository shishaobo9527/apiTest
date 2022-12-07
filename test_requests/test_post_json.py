import requests

from utils.log_util import logger


def test_post():
    logger.info("开始执行test_post方法")
    json_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.post(url=url, json=json_data)
    assert r.status_code == 201
    print(r.status_code)
    print(r.json())
    logger.info("用例执行完毕")
