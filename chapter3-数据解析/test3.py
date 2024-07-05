import time

price_str = '6630元/㎡'
# 假设数字是字符串的第一个字符直到遇到非数字字符
price_num = price_str.split('元')
print(price_num)  # 输出：6630
time.sleep(2)
print('lll')