from fake_useragent import UserAgent

if __name__ == '__main__':
    ua = UserAgent()
    for i in range(10):
        print(ua.random)
