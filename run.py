import HTMLTestRunner
import os
import unittest

import readConfig
from Common.Log import MyLog as Log

proDir = readConfig.proDir


class AllTest:
    def __init__(self):
        global log, logger, reportPath
        log = Log.get_log()
        logger = log.get_logger()
        reportPath = log.get_report_path()
        self.caseListFile = os.path.join(proDir, "testFile", "caseList.txt")
        # 测试用例文件夹
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        print(self.caseFile)
        # 测试用例名称
        self.caseList = []

    # 通过#控制需要执行的测试用例集
    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    # 设置测试用例套件
    def set_case_suit(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_moudle = []
        for case in self.caseList:
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=''+case_name+'.py', top_level_dir=None)
            suite_moudle.append(discover)
        if len(suite_moudle) > 0:
            for suit in suite_moudle:
                for test_name in suit:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        fp = open(reportPath, 'wb')
        try:
            suit = self.set_case_suit()
            if suit is not None:
                logger.info("******Test Start******")
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
                logger.info(runner)
            else:
                logger.info("Have no case for testing.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("******Test End******")
            fp.close()


if __name__ == "__main__":
    Runner = AllTest()
    Runner.run()
