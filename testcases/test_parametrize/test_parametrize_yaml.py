import pytest

from utils.read_data import get_data


# 单参数
# @pytest.mark.parametrize("name", get_data["heros_name"])
# def test_parametrize_yaml(name):
#     print(name)

# 多参数
@pytest.mark.parametrize("name, word", get_data["hero_name_word"])
def test_parametrize_yaml(name, word):
    print(f'{name}的台词是{word}')
