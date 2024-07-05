import requests
from lxml import etree
import os
from fake_useragent import UserAgent


if __name__ == "__main__":

    base_url = 'https://luohe.58.com/ershoufang/'

    if not os.path.exists('./58二手房/漯河'):
        os.makedirs('./58二手房/漯河')
    if not os.path.exists('./58二手房/北京'):
        os.makedirs('./58二手房/北京')

    max_page_num = int(input('input max page num(max is 50):'))

    for i in range(1, max_page_num + 1):
        # UA伪装
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        print(headers)
        url = base_url + 'p' + str(max_page_num)
        page_text = requests.get(url=base_url, headers=headers).text
        # 数据解析
        tree = etree.HTML(page_text)
        div_property_content_list = tree.xpath('//div[@class="property-content"]')
        print(div_property_content_list)
    #     for div_property_content in div_property_content_list:
    #         title = div_property_content.xpath('.//div[@class="property-content-title"]//h3/text()')
    #         price = div_property_content.xpath('.//div[@class="property-price"]//span['
    #                                            '@class="property-price-total-num"]/text()')
    #         print(title)
    #         print(price)
    #
    #     print('page' + str(i) + ' over')
    #
    # print('over!!!')
