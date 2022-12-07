import pytest
import requests

from utils.read_data import get_data


def test_mobile():
    param = get_data["mobile_belong"]
    print("测试手机归属地get请求")
    params = {
        "shouji": param["shouji"],
        "appkey": param["appkey"]
    }
    r = requests.get("https://api.binstd.com/shouji/query", params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == '13456755448'
    assert result['result']['province'] == '浙江'
    assert result['result']['city'] == '杭州'
    assert result['result']['company'] == '中国移动'
    assert result['result']['cardtype'] is None
    assert result['result']['areacode'] == '0571'


@pytest.mark.parametrize("shouji,appkey", get_data["mobile_belong_get"])
def test_mobile_get(shouji, appkey):
    print("测试手机归属地get请求")
    params = {
        "shouji": shouji,
        "appkey": appkey
    }
    r = requests.get("https://api.binstd.com/shouji/query", params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == '13456755448'
    assert result['result']['province'] == '浙江'
    assert result['result']['city'] == '杭州'
    assert result['result']['company'] == '中国移动'
    assert result['result']['cardtype'] is None
    assert result['result']['areacode'] == '0571'


@pytest.mark.parametrize("shouji, appkey", get_data["mobile_belong_post"])
def test_mobile_post(shouji, appkey):
    print("测试手机归属地post请求")
    params = {
        "shouji": shouji,
        "appkey": appkey
    }
    r = requests.post("https://api.binstd.com/shouji/query", params=params)
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == '13456755448'
    assert result['result']['province'] == '浙江'
    assert result['result']['city'] == '杭州'
    assert result['result']['company'] == '中国移动'
    assert result['result']['cardtype'] is None
    assert result['result']['areacode'] == '0571'


if __name__ == '__main__':
    pytest.main()
