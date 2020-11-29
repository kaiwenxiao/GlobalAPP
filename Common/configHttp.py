import requests

import readConfig as readConfig
from Common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global scheme, host, timeout, unEncryptToken
        scheme = localReadConfig.get_http("scheme")
        host = localReadConfig.get_http("baseurl")
        timeout = localReadConfig.get_http("timeout")
        unEncryptToken = localReadConfig.get_headers("unEncryptToken")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.file = {}
        self.state = 0

    # 设置url
    def set_url(self, url):
        self.url = scheme + '://' + host + url

    def get_url(self):
        return self.url

    def set_headers(self, header):
        self.headers = header

    def get_headers(self):
        return self.headers

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_files(self, filename):
        pass

    # get请求
    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")


if __name__ == "__main__":
    ConfigHttp1 = ConfigHttp()
    print(ConfigHttp1.url)
