from configparser import ConfigParser
import os

# 创建对象
config = ConfigParser()
# 指定路径
path = os.path.join(os.sep, os.getcwd(), "conf", "conf.ini")
# 读取文件
config.read(path, encoding="utf-8")
