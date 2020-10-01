'''
Description: 
Author: sunwang
Date: 2020-09-30 23:28:01
LastEditTime: 2020-10-01 12:02:09
LastEditors: sunwang
'''
from logging.handlers import RotatingFileHandler
from com_func.confread import config
from com_func.basepath import testpath
import logging
import os


def logger_create():
    # 创建logger日志收集器
    logger= logging.getLogger(__name__)
    # 设置输入日志等级
    logger.setLevel(config.get("LOG", "input_level"))
    # 设置日志输出格式
    mat = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    logger_mat = logging.Formatter(mat)
    # 输出日志到文件
    handler_file  = RotatingFileHandler(os.path.join(os.sep, testpath.LogDirPath, "log.txt"), maxBytes = 1*1024,backupCount = 3)
    handler_file.setLevel(config.get("LOG", "output_level"))
    handler_file.setFormatter(logger_mat)
    # 输出日志到控制台
    handler_sh = logging.StreamHandler()
    handler_sh.setLevel(config.get("LOG", "output_level"))
    handler_sh.setFormatter(logger_mat)
    # 加载logging
    logger.addHandler(handler_file)
    logger.addHandler(handler_sh)
    # 返回日志收集器
    return logger

logger = logger_create()