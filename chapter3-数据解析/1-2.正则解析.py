import requests
import re
import os

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    # 进入搜索页面的url
    url = 'https://www.vcg.com/creative-image/'
    target_search_photo_name = input('enter a photo name:')
    # 创建一个文件夹，保存搜索内容前max_page_num页所有的图片
    if not os.path.exists('./视觉中国/' + str(target_search_photo_name)):
        os.mkdir('./视觉中国/' + str(target_search_photo_name))
    # 设置搜索内容的url
    new_url = url + target_search_photo_name + '/?page=%d'
    # 设置爬取页面张数
    max_page_num = int(input('enter max page num:'))

    for page_num in range(1, max_page_num + 1):
        # 每个页面的url
        page_url = format(new_url % page_num)

        # 使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text

        # 使用聚焦爬虫将页面所有的图进行解析/提取
        ex = '<a class="imgWaper" target="_blank" rel="opener".*?data-src="(.*?)" data-min.*?</a>'
        img_src_list = re.findall(ex, page_text, re.S)
        print(img_src_list)
        for src in img_src_list:
            # 拼接成一个完成是url
            src = 'https:' + src
            # 请求到了图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            imgPath = './视觉中国/' + target_search_photo_name + '/' + img_name
            with open(imgPath, 'wb') as file:
                file.write(img_data)
                print(img_name + "下载成功!!!")
print('over!')
