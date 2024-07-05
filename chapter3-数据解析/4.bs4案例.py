# 需求：爬取三国演义小说所有的章节标题和章节内容
# https://www.shicimingju.com/book/sanguoyanyi.html
import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    # 对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'utf-8'

    # 在首页中解析出章节的标题和详情页url
    # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text.text, 'lxml')
    # 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    print(li_list)
    if not os.path.exists('./三国演义'):
        os.makedirs('./三国演义')
    file = open('./三国演义.txt', 'w', encoding='utf-8')

    for li in li_list:
        title = li.a.string
        print(title)
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        print(detail_url)
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(detail_url, headers=headers)
        detail_page_text.encoding = 'utf-8'
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text.text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节的内容
        content = div_tag.text
        # 写文本
        # 分开写
        with open('./三国演义/'+str(title)+'.txt', 'w', encoding='utf-8') as f:
            f.write(title + '\n' + content + '\n')

        # 写一个总的
        file.write(title + '\n' + content + '\n')
        print(title, '爬取成功')

print('over')

