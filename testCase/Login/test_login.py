import unittest

import parameterized
import paramunittest

import readConfig
from Common import Log
from Common import common, configHttp

LoginInfo_xls = common.get_xls("testLogin.xlsx", "login")
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

# parameterized 需要第一行用例信息作为参数名
@paramunittest.parametrized(*LoginInfo_xls)
class TestLogin(unittest.TestCase):

    def setParameters(self, case_name, method, username, password, errorCode, state, note):
        self.case_name = str(case_name)
        self.method = str(method)
        self.username = str(username)
        self.password = str(password)
        self.errorCode = str(errorCode)
        self.state = str(state)
        self.note = str(note)
        self.return_json = None
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name + "测试开始前准备")

    def testLogin(self):
        self._testMethodDoc = self.case_name
        self.url = common.get_url_from_xml("login")
        configHttp.set_url(self.url)
        print("1.设置url")

        header = {
            'unEncryptToken': 'true',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        configHttp.set_headers(header)
        print("2.设置header")

        data = {
            'username': self.username,
            'password': self.password
        }
        configHttp.set_data(data)
        print("3.设置发送参数")
        if self.case_name == 'login_fail_five time':
            self.return_json = configHttp.post()
            self.return_json = configHttp.post()
            self.return_json = configHttp.post()
            self.return_json = configHttp.post()
        else:
            self.return_json = configHttp.post()
        method = str(self.return_json.request)[
                    int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("4.发送请求\n\t\t请求方法:" + method)

        self.checkResult()
        print("5.检查结果")

    def tearDown(self):
        self.log.build_case_line(self.case_name, self.note)

    def checkResult(self):
        self.info = self.return_json.json()
        print(self.info)
        # common.show_return_msg()
        self.assertEqual(self.info['state'], self.state)
        if self.note == None:
            self.assertEqual(self.info['note'], self.note)


if __name__ == "__main__":
    ProductInfo1 = TestLogin()
