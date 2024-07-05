import requests
from lxml import etree

if __name__ == '__main__':
    # 爬取到页面源码数据
    url = 'https://cn.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)

    # 数据解析
    tree = etree.HTML(page_text)
    div_property_content_list = tree.xpath('//div[@class="property-content"]')
    print(div_property_content_list)
    fp = open('58.txt', 'w', encoding='utf-8')
    fp.write('title\t'+'price\n')
    for div_property_content in div_property_content_list:
        title = div_property_content.xpath('.//h3/text()')[0]
        print(title)
        price = div_property_content.xpath('.//span[@class="property-price-total-num"]/text()')[0]
        print(price)
        fp.write(title + '\t' + price + '\n')

    print('over!')

