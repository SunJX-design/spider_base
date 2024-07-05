import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
from fake_useragent import UserAgent
import time
import re

if __name__ == "__main__":
    # 房子单价总数
    house_unit_price_sum = 0

    # 房子套数
    house_num = 0

    if not os.path.exists("./安居客二手房/北京"):
        os.makedirs("./安居客二手房/北京")

    base_url = 'https://beijing.anjuke.com/sale/'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    max_page_num = int(input('enter max page num: '))

    fp = open('./安居客二手房/北京/前' + str(max_page_num) + '页.txt', 'w', encoding='utf-8')
    fp.write('标题\t' + '面积\t' + '单价\t' + '总价\n')
    for i in range(1, max_page_num + 1):
        url = base_url + 'p' + str(i)

        page_text = requests.get(url=url, headers=headers).text

        soup = BeautifulSoup(page_text, 'lxml')
        tree = etree.HTML(page_text)

        div_property_content_list = tree.xpath('//div[@class="property-content"]')
        print(div_property_content_list)

        for div_property_content in div_property_content_list:
            title = div_property_content.xpath('.//h3/text()')[0]
            area = div_property_content.xpath('.//p[@class="property-content-info-text"]/text()')[0].strip()
            unit_price = div_property_content.xpath('.//p[@class="property-price-average"]/text()')[0].strip()
            unit_price_number = int(re.search(r'\d+', unit_price).group())  # 提取数字并转换为整数
            # re.search(r'\d+', raw_unit_price)是用来查找字符串中的数字序列，\d+匹配一个或多个数字字符。
            # .group()方法用来获取匹配到的第一个数字序列。如果单价可能是带有小数点的数值，
            total_price = div_property_content.xpath('.//span[@class="property-price-total-num"]/text()')[0]
            print('标题:' + title)
            print('面积:' + area)
            # print('单价:' + repr(unit_price))
            print('单价:' + str(unit_price_number) + '元/㎡')
            print('总价:' + total_price + '万元')
            fp.write(title + '\t' + area + '\t' + str(unit_price_number) + '元/㎡\t' + total_price + '万元\n')
            house_num += 1
            house_unit_price_sum += unit_price_number

        print('第' + str(i) + '页over')
        time.sleep(5)
    print('over!!!')
    print('总计' + str(house_num) + '套，均价' + str(house_unit_price_sum // house_num) + '元/㎡')
