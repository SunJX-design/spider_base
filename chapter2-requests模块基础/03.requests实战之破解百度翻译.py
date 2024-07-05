import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    word = input('enter a word:')
    # post请求参数处理(同get请求一致)
    data = {
        'kw': word
    }
    # 请求发送
    response = requests.post(post_url, data=data, headers=headers)
    # 获取响应数据:json()方法返回的是obj(如果确认响应数据是json类型的，才能使用json())
    dic_obj = response.json()

    # 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('over')
