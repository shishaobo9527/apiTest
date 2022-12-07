import yaml


f = open("../config/data.yaml", encoding="gb18030")
data = yaml.safe_load(f)
# print(data)
# print(data["hero"])
# print(data["heros_name"])
# print(data["heros"])
# print(data["hero_name_list"])
print(data["mobile_belong"])
print(data["mobile_belong_post"])
