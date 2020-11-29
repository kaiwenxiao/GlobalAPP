from datetime import datetime
import logging
import os
import threading
import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # 创建result目录
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 创建result目录下的日志目录
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 定义日志文件，输出时间格式
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

    def get_report_path(self):
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_resultDic_path(self):
        return logPath

    def build_case_line(self, case_name, note):
        self.logger.info(case_name + " - note:" + note)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __int__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log


if __name__ == "__main__":
    a = MyLog.get_log()
    print(a)
