import logging
import sys

import requests
# 禁止弹出警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from logginghandler import MultiprocessHandler

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def loggerDefine(loggerFile):
    # 定义日志输出格式
    formattler = '%(asctime)s|%(processName)s|%(threadName)s|%(levelname)s|%(filename)s:%(lineno)d|%(funcName)s|%(message)s'
    fmt = logging.Formatter(formattler)

    # 获得logger，默认获得root logger对象
    # 设置logger级别 debug
    # root logger默认的级别是warning级别。
    # 不设置的话 只能发送 >= warning级别的日志
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置handleer日志处理器，日志具体怎么处理都在日志处理器里面定义
    # SteamHandler 流处理器，输出到控制台,输出方式为stdout
    # StreamHandler默认输出到sys.stderr
    # 设置handler所处理的日志级别。
    # 只能处理 >= 所设置handler级别的日志
    # 设置日志输出格式
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(fmt)

    # 使用我们写的多进程版Handler理器，定义日志输出到mylog.log文件内
    #   文件打开方式默认为 a
    #   按分钟进行日志切割
    file_handler = MultiprocessHandler(loggerFile)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fmt)

    # 对logger增加handler日志处理器
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    pass
