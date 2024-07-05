import requests

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi/1.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text

    with open('第一回.html', 'w', encoding='utf-8') as file:
        file.write(page_text)
    print('over!')
