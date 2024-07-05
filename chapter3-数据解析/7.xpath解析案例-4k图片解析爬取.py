# http://pic.netbian.com/4kfengjing/

import requests
from lxml import etree
from fake_useragent import UserAgent
import os

if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kfengjing/'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    page_text = requests.get(url=url, headers=headers)
    # 手动设定相应数据的编码格式
    page_text.encoding = 'gbk'
    # print(page_text.text)

    tree = etree.HTML(page_text.text)
    img_list = tree.xpath('//ul[@class="clearfix"]/li')
    # print(picture_list)

    if not os.path.exists('./风景照片'):
        os.makedirs('./风景照片')

    for img in img_list:
        img_url = img.xpath('.//img/@src')[0]
        img_url = 'http://pic.netbian.com' + img_url
        img_name = img.xpath('.//img/@alt')[0] + '.jpg'
        # 文件名不能包含\ / : * ? " < > |
        self_img_name = img_name.replace('*', 'x')
        print(self_img_name)
        print(img_url)

        img_data = requests.get(url=img_url, headers=headers).content
        img_path = './风景照片/' + self_img_name
        # print(img_data)
        # print(img_path)
        with open(img_path, 'wb') as file:
            file.write(img_data)
            print(img_name+'下载成功!')
    print('over!')
