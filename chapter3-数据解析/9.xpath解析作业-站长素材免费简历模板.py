# https://sc.chinaz.com/jianli/free.html
# https://sc.chinaz.com/jianli/free_2.html
import os
import requests
from lxml import etree
from fake_useragent import UserAgent
import time


def page_download():
    for doc_detail_url in doc_detail_url_list:
        detail_page_url = doc_detail_url

        detail_page_text = requests.get(url=detail_page_url, headers=headers)
        detail_page_text.encoding = 'utf-8'

        detail_tree = etree.HTML(detail_page_text.text)
        title = detail_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
        download_url = \
            detail_tree.xpath('//div[@class="down_wrap" and @id="down"]//ul[@class="clearfix"]/li[1]/a/@href')[0]
        print(download_url)
        print(title)

        # 下载到./简历模板 目录下
        # 发送GET请求获取数据
        # file_name = './简历模板/' + title + '.rar'
        # response = requests.get(url, stream=True)
        # if response.status_code == 200:
        #     # 使用with语句打开文件，以二进制写模式 ('wb')
        #     with open(file_name, 'wb') as file:
        #         for chunk in response.iter_content(chunk_size=1024):  # 分块写入文件
        #             if chunk:  # 过滤掉keep-alive新行
        #                 file.write(chunk)
        #     print(f"文件 {title} 下载完成。")
        # else:
        #     print("下载失败，状态码：", response.status_code)

        file_name = './简历模板/压缩文件/' + title + '.rar'
        response = requests.get(download_url)
        with open(file_name, 'wb') as f:
            f.write(response.content)

        # time.sleep(2)


if __name__ == '__main__':
    max_page_num = int(input('enter max page num(max is 964): '))

    if not os.path.exists('./简历模板/压缩文件'):
        os.makedirs('./简历模板/压缩文件')
    if not os.path.exists('./简历模板/解压文件'):
        os.makedirs('./简历模板/解压文件')

    url = 'https://sc.chinaz.com/jianli/free.html'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        # 'Cookie': 'cz_statistics_visitor=e714468a-15e5-f69e-15de-41c046c64319; _clck=1vxalyd%7C2%7Cfn7%7C0%7C1647; '
        #           'ASP.NET_SessionId=pop0i0ji5ndotv0ewgirpb1r; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1720150432,'
        #           '1720150841,1720160978; HMACCOUNT=BA85F6AFA9E0465B; '
        #           'qHistory=aHR0cDovL3Rvb2wuY2hpbmF6LmNvbV/nq5nplb/lt6Xlhbc=; '
        #           'Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1720164897; '
        #           '_clsk=1x8buic%7C1720164898136%7C26%7C1%7Cz.clarity.ms%2Fcollect'
    }
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'utf-8'
    # print(page_text.text)

    tree = etree.HTML(page_text.text)
    doc_detail_url_list = tree.xpath(
        '//div[@id="main"]/div[@class="main_list jl_main" and @id="container"]/div/a/@href')
    # print(doc_detail_url_list)

    page_download()

    for i in range(2, max_page_num + 1):
        url = 'https://sc.chinaz.com/jianli/free_' + str(i) + '.html'
        page_text = requests.get(url=url, headers=headers)
        page_text.encoding = 'utf-8'
        # print(page_text.text)

        tree = etree.HTML(page_text.text)
        doc_detail_url_list = tree.xpath(
            '//div[@id="main"]/div[@class="main_list jl_main" and @id="container"]/div/a/@href')
        # print(doc_detail_url_list)

        page_download()

    print('over!')
