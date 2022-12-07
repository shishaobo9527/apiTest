import logging
import os
import time

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(ROOT_PATH, "log")


class Logger:
    def __init__(self):
        # 定义日志位置和文件名
        self.log_name = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y-%m-%d-%H-%M-%S")))
        # 定义一个日志容器
        self.logger = logging.getLogger("log")
        # 设置日志打印级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输出格式
        self.formatter = logging.Formatter("[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:%(message)s")
        # 创建日志处理器，用来存放日志文件
        self.file_logger = logging.FileHandler(self.log_name, mode="a", encoding="utf8")
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台日志打印级别
        self.console.setLevel(logging.DEBUG)
        # 设置文件存放的日志级别
        self.file_logger.setLevel(logging.DEBUG)
        # 文件存放的日志格式
        self.file_logger.setFormatter(self.formatter)
        # 控制台日志打印格式
        self.console.setFormatter(self.formatter)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.file_logger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.debug("我打印的是debug日志")
    logger.warning("我打印的是warning日志")
    logger.info("我打印的是info日志")
    logger.error("我打印的是error日志")
