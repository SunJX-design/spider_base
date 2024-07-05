import requests

# UA:User-Agent (请求载体的身份标识)
# UA检测:门户网站的服务器会检测对应请求的载体身份标识，如果检测到
# 请求的载体是某一款浏览器则正常请求，反之表示是爬虫，服务器端很有可能拒绝请求。

# UA伪装:让爬虫对应的请求载体身份标识伪装成某一浏览器
if __name__ == "__main__":
    # UA伪装:将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('保存成功!')
