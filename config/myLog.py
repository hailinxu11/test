'''
日志文件类
主要用于把出现错误的地方捕捉后存放到./result/logs文件夹下面
这里也存放了report的路径./result/report文件夹下面
'''

import logging.config
import os
import time
from logging.handlers import RotatingFileHandler
from config import myFig


class MyLog:
    def __init__(self):
        # 声明全局变量
        global format1, max_bytes, backup_count, log_level, report_path, log_path
        # 日志内容格式
        format1 = myFig.getLog('format').replace('@', '%')
        # 日志大小和树木
        backup_count = int(myFig.getLog('backupCount'))
        max_bytes = int(myFig.getLog('maxBytes'))
        # 日志级别
        log_level = int(myFig.getLog('level'))
        # 文件的日期格式
        rq = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
        # log文件的存放路径
        log_path = os.path.dirname(os.path.dirname(__file__)) + '/testReport/logs/' + rq + '.log'
        # report文件的存放路径
        now = time.strftime('%Y-%m-%d_%H:%M:%S')
        report_path = os.path.dirname(os.path.dirname(__file__)) + '/testReport/report/' + now + '.html'

    # 保存日志到文件的函数
    # 日志存放路径
    @staticmethod
    def getLogPath():
        return log_path

    # 测试报告存放路径
    @staticmethod
    def getReportPath():
        return report_path

    @staticmethod
    def logger():
        # 创建一个logger
        logger1 = logging.getLogger()
        logger1.setLevel(log_level)
        if not logger1.handlers:
            # 创建一个handler,用于写入文件
            Rthandler = RotatingFileHandler(MyLog().getLogPath(), maxBytes=max_bytes, backupCount=backup_count,
                                            encoding='utf-8')
            # 这里来设置日志的级别
            # CRITICAl    50
            # ERROR    40
            # WARNING    30
            # INFO    20
            # DEBUG    10
            # NOSET    0

            # 定义handler的输出格式
            logFormat = logging.Formatter(format1)
            # 给handler添加formatter
            Rthandler.setFormatter(logFormat)
            logger1.removeHandler(Rthandler)
            # 给logger添加handler
            logger1.addHandler(Rthandler)
        return logger1
