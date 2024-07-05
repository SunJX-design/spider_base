import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://www.shicimingju.com/book/sanguoyanyi/1.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text,'lxml')

    content_list = soup.select('.chapter_content > p')
    print(content_list)
