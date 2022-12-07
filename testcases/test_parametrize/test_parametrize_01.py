import pytest


# @pytest.mark.parametrize("key", "value")
# @pytest.mark.parametrize("name", ["阿木木"])
# def test_parametrize_01(name):
#     print("我是" + name)

# 单次
# @pytest.mark.parametrize("name", ["阿木木"])
# def test_parametrize_01(name):
#     assert name == "阿木木"

# 一个参数，多个值：每个值会依次赋值给参数，执行测试用例，有几个值就执行几条测试用例
# @pytest.mark.parametrize("name", ["阿木木", "易", "安妮"])
# def test_parametrize_01(name):
#     assert name == "阿木木"

# @pytest.mark.parametrize("hero", [{"name": "阿木木"}, {"name": "易"}, {"name": "安妮"}])
# def test_parametrize_01(hero):
#     print(hero["name"])

@pytest.mark.parametrize("hero", [{"name": "阿木木", "word": "来和我玩吧"}])
def test_parametrize_01(hero):
    print(hero["name"])
    print(hero["word"])
