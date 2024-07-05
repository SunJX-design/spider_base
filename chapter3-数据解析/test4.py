# https://sc.chinaz.com/jianli/240112113120.htm
# 下载文件

import requests
from lxml import etree


url = "https://downsc.chinaz.net/Files/DownLoad/jianli/202401/zjianli2338.rar"
file_name = "zjianli2338.rar"  # 指定保存的文件名

# 发送GET请求获取数据
# response = requests.get(url, stream=True)
# if response.status_code == 200:
#     # 使用with语句打开文件，以二进制写模式 ('wb')
#     with open('./简历模板/'+file_name, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=1024):  # 分块写入文件
#             if chunk:  # 过滤掉keep-alive新行
#                 file.write(chunk)
#     print(f"文件 {file_name} 下载完成。")
# else:
#     print("下载失败，状态码：", response.status_code)

response = requests.get(url)
with open(file_name, 'wb') as f:
    f.write(response.content)
