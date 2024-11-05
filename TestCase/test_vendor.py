import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_vendor import PageVendor
from utils.times import sleep

class TestVendor:

    @pytest.fixture(scope='function', autouse=True)
    def setup_vendor_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        vendor = PageVendor(drivers)
        return vendor  # 返回 PageProject 实例

    def test_new_vendor(self, setup_vendor_url, drivers):
        # 在测试用例中使用 setup_project_url 夹具函数返回的 PageProject 实例
        setup_vendor_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        setup_vendor_url.new_vendor()
        sleep(10000)


    def test_invite_vendor(self, drivers, setup_vendor_url):
        setup_vendor_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        setup_vendor_url.invite_vendor()
        Login(drivers).login_out2()
        setup_vendor_url.get_url(ini._get('HOST', 'host2'))
        sleep(3.5)
        setup_vendor_url.input_invite_vendor()
        sleep(1000)

    def test_design_oder(self, drivers, setup_vendor_url):
        setup_vendor_url.get_url(ini.url)
        Login(drivers).login("DV1710222892825", "a111111")
        setup_vendor_url.design_order()


if __name__ == '__main__':
    pytest.main(['TestCase/test_vendor.py'])
