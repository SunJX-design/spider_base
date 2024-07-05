from lxml import etree

if __name__ == "__main__":
    # 实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('./test.html')
    # r = tree.xpath('/html/body/div')  # /表示单个层级
    # r = tree.xpath('/html//div')        # //表示多个层级
    # r = tree.xpath('//div')  # //表示多个层级
    # r = tree.xpath('//div[@class="song"]')  # 属性定位
    # r = tree.xpath('//div[@class="song"]/p[3]')  # 索引定位，索引从1开始
    # r = tree.xpath('//div[@class="tang"]/ul/li[5]/a/text()')[0]
    # r = tree.xpath('//div[@class="tang"]/ul/li[7]/i/text()')[0]
    # r = tree.xpath('//div[@class="tang"]/text()')
    r = tree.xpath('//div[@class="song"]/img/@src')     # 取属性
    print(r)
