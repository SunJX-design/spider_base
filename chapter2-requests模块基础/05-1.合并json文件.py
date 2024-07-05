import json

# 文件名的前缀和后缀，以及范围
prefix = "./KFC/BeijingKFC"
suffix = ".json"
start_num = 1
end_num = 21

# with open("./KFC/BeijingKFC1.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     print(data["Table1"])


# 初始化最终合并的列表
merged_data = []

for i in range(start_num, end_num + 1):
    # 构建当前文件名
    fileName = prefix + str(i) + suffix

    # 打开并读取json文件
    with open(fileName, 'r', encoding='utf-8') as file:
        data = json.load(file)
        merged_data.append(data["Table1"])

print(merged_data)

# 读取原json文件
with open('KFC/0BeijingKFC.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 更新Table1的数据
data['Table1'] = merged_data

# 写回json文件
with open('KFC/0BeijingKFC.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
