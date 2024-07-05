# import os
# import rarfile
#
# def unrar_files(directory_path):
#     # 指定unrar工具的路径，如果你的系统PATH中已经包含了unrar，则不需要这一步
#     rarfile.UNRAR_TOOL = "D:\\Program Files\\WinRAR\\WinRAR.exe"  # 或者提供完整路径，例如 "C:/Program Files/unrar/unrar.exe"
#
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith(".rar"):  # 检查文件是否为RAR文件
#                 rar_path = os.path.join(root, file)
#                 print(f"正在解压: {rar_path}")
#                 try:
#                     with rarfile.RarFile(rar_path) as rf:
#                         # 解压到当前文件所在的目录
#                         rf.extractall(path=os.path.dirname(rar_path))
#                         print(f"{file} 解压完成")
#                 except Exception as e:
#                     print(f"解压{rar_path}时出错: {e}")
#
#
# # 指定包含RAR文件的目录路径
# directory_to_unrar = "D:\\project\\spider_base\\chapter3-数据解析\\简历模板"
# unrar_files(directory_to_unrar)



