import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_design import PageDesign
from utils.times import sleep
from common.read_excel import load_test_cases_from_excel
from common.mysql import Mysql


class TestDesign:



    test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', 'product')

    @pytest.fixture(scope='function', autouse=True)
    def setup_product_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        project = PageDesign(drivers)
        return project  # 返回 PageProject 实例


    def test_001(self, drivers, setup_product_url):
        """新增设计需求"""
        setup_product_url.get_url(ini.url)
        Login(drivers).login("bd", "a111111")
        setup_product_url.new_design()
