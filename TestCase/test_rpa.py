import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_vendor import PageVendor
from page_object.page_rpa import PageRpa
from utils.times import sleep

class TestVendor:

    @pytest.fixture(scope='function', autouse=True)
    def setup_rpa_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        rpa = PageRpa(drivers)
        return rpa  # 返回 PageProject 实例


    def test_order_builder(self,drivers,setup_rpa_url):
        setup_rpa_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        sleep(1)
        setup_rpa_url.order_builder()



if __name__ == '__main__':
    pytest.main(['TestCase/test_vendor.py'])
