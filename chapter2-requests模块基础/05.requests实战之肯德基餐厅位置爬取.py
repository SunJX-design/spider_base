import requests
import json
import math

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    param = {
        'cname': '北京',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    response = requests.post(url, data=param, headers=headers)

    list_data = response.json()
    print(list_data)

    # 爬取全部数据
    row_count = list_data["Table"][0]["rowcount"]
    print(row_count)
    page = math.ceil(row_count / 10)
    print(page)

    merged_data = []  # 初始化一个空列表来存放合并的数据

    for i in range(1, page + 1):
        url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
        param = {
            'cname': '北京',
            'pid': '',
            'keyword': '北京',
            'pageIndex': i,
            'pageSize': '10',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        }
        response = requests.post(url, data=param, headers=headers)

        list_data = response.json()
        print(list_data)

        fileName = './KFC/BeijingKFC' + str(i) + '.json'
        fp = open(fileName, 'w', encoding='utf-8')
        json.dump(list_data, fp=fp, ensure_ascii=False, indent=4)
        try:
            # 读取每个文件的内容
            with open(fileName, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    print(f"警告:文件{fileName}的内容不是预期的列表格式，跳过该文件")
        except FileNotFoundError:
            print(f"错误:文件{fileName}未找到。")
        except json.decoder.JSONDecodeError as e:
            print(f"错误:文件{fileName}解析为json时出错:{e}")

    # 将合并后的数据写入到新的json文件
    outputFileName = './KFC/0BeijingKFC.json'
    with open(outputFileName, 'w', encoding='utf') as outputFileName:
        json.dump(merged_data, outputFileName, ensure_ascii=False, indent=4)

    print(f"合并完成，结果已保存至{outputFileName}")
