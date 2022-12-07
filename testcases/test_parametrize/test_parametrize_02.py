import pytest

# 数组的形式
# @pytest.mark.parametrize("name, word", [["阿木木", "我还以为你从来不会选我呢"], ["安妮", "火焰是我最喜欢的玩具"], ["易", "好好看好好学"]])
# def test_parametrize_02(name, word):
#     print(f"{name}的台词是{word}")
#
# 元组的形式
# @pytest.mark.parametrize("name, word", [("阿木木", "我还以为你从来不会选我呢"), ("安妮", "火焰是我最喜欢的玩具"), ("易", "好好看好好学")])
# def test_parametrize_02(name, word):
#     print(f"{name}的台词是{word}")


@pytest.mark.parametrize("name, word", [["阿木木", "我还以为你从来不会选我呢"]])
def test_parametrize_02(name, word):
    print(f"{name}的台词是{word}")
