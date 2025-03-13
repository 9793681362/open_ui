import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_sales_module import PageSalesModule
from page_object.page_rpa import PageRpa
from utils.times import sleep

class TestVendor:

    @pytest.fixture(scope='function', autouse=True)
    def setup_sales_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        rpa = PageSalesModule(drivers)
        return rpa  # 返回 PageProject 实例


    def test_order_builder(self,drivers,setup_sales_url):
        """
        新增备案
        :param drivers:
        :param setup_sales_url:
        :return:
        """
        try:
            setup_sales_url.get_url(ini.url)
            Login(drivers).login("admin", "111111")
            setup_sales_url.add_record()
        except:
            pass


    def test_daily_plan_week_plan(self,drivers,setup_sales_url):
        setup_sales_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        setup_sales_url.add_daily_plan()


if __name__ == '__main__':
    pytest.main(['TestCase/test_vendor.py'])
