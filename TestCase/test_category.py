import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_category import PageCategory
from utils.times import sleep
from common.read_excel import load_test_cases_from_excel
from common.mysql import Mysql


class TestCategory:
    test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', 'product')

    @pytest.fixture(scope='function', autouse=True)
    def setup_category_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        project = PageCategory(drivers)
        return project  # 返回 PageProject 实例

    def test_001(self, drivers, setup_category_url):
        setup_category_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        setup_category_url.create_category()
        sleep(10)