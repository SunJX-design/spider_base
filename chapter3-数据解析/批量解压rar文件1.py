# coding=utf-8
import rarfile

rarfile.UNRAR_TOOL = 'D:\\Program Files\\WinRAR\\WinRAR.exe'  # 请将'path_to_unrar'替换为unrar的实际路径，例如"C:/Program Files/unrar/unrar.exe"（Windows）或"/usr/bin/unrar"（Linux）
path = "/chapter3-数据解析\\简历模板\\压缩文件\\1年经验游戏运营个人简历模板.rar"
path2 = "D:\\project\\spider_base\\chapter3-数据解析\\简历模板\\解压文件"

rf = rarfile.RarFile(path)      # 待解压文件
rf.extractall(path2)            # 解压指定文件路径
rf.close()
