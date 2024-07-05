from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.a)   # soup.tagName 返回的是html中第一次出现的tagName对应的标签
    # print(soup.div)

    # soup.find(tagName)=soup.tagName
    # print(soup.find('div'))  # print(soup.div)
    # ----------
    # print(soup.find('div', class_='song'))  # 属性定位
    # print(soup.find('div', class_='song').string)
    # ----------
    # print(soup.find_all('a'))     # 返回的是列表

    # print(soup.select('.tang'))     # 返回的是列表

    # ----------
    print(soup.select('.tang > ul > li > a'))       # 层级选择器
    # > 表示一个层级 空格表示多个层级
    # print(soup.select('.tang > ul > li > a')[0])    # 返回第一个li标签
    # print(soup.select('.tang > ul  a')[0])          # 返回第一个li标签
    # print(soup.select('.tang > ul  a')[0]['href'])

    # ----------





