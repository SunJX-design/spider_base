import requests

if __name__ == '__main__':
    # 如何爬取图片数据
    url = 'https://vcg01.cfp.cn/creative/vcg/800/new/VCG211394359895.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    # content返回的是二进制形式的图片数据
    # text(字符串) content(二进制) json()(对象)
    img_data = requests.get(url, headers=headers).content
    with open('./大树/大树绿色草坪.jpg', 'wb') as file:
        file.write(img_data)
    print('over')
