# 全国城市名 https://www.aqistudy.cn/historydata/

import requests
from lxml import etree
from fake_useragent import UserAgent
import os

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)

    tree = etree.HTML(page_text)
    hot_li_list = tree.xpath('//div[@class="hot"]//div[@class="bottom"]/ul/li')
    all_hot_list = []
    for li in hot_li_list:
        hot_name = li.xpath('./a/text()')[0]
        all_hot_list.append(hot_name)
    # print(all_hot_list)

    fp = open('中国城市目录.txt', 'w', encoding='utf-8')
    fp.write("首字母+城市名\n")

    all_bottom_ul_list = tree.xpath('//div[@class="all"]//div[@class="bottom"]/ul')
    # print(all_bottom_ul_list)
    for div_li_list in all_bottom_ul_list:
        capital = div_li_list.xpath('.//div[1]/b/text()')[0]
        print(capital)
        fp.write(capital + '\n')
        li_list = div_li_list.xpath('.//div[2]/li')
        for li in li_list:
            name = li.xpath('./a/text()')[0]
            print(name)
            fp.write(name + '\n')

    print('over!')

