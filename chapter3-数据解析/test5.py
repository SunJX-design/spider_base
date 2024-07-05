import requests
from lxml import etree
from fake_useragent import UserAgent

if __name__ == '__main__':
    url = 'https://sc.chinaz.com/jianli/240624496761.htm'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'utf-8'
    print(page_text.text)

    tree = etree.HTML(page_text.text)
    download_url = tree.xpath('//div[@class="down_wrap" and @id="down"]//ul[@class="clearfix"]/li[1]/a/@href')
    title = tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')
    print(download_url)
    print(title)
