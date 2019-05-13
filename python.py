from loggerDefine import loggerDefine

logger = loggerDefine("mylog.log")


def main():
    logger.info("开始输出日志")


if __name__ == '__main__':
    main()
