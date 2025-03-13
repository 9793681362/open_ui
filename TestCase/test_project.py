import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_project import PageProject
from utils.times import sleep
from common.read_excel import load_test_cases_from_excel
from common.mysql import Mysql


class TestProject:
    test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', '项目下单')

    @pytest.fixture(scope='function', autouse=True)
    def setup_project_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        project = PageProject(drivers)
        return project  # 返回 PageProject 实例

    def test_001(self, drivers, setup_project_url):
        test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', '项目下单')
        setup_project_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")

        for test_case in test_cases:
            try:
                setup_project_url.new_project(test_case['company_name'], test_case['place'], test_case['project_name'],
                                              test_case['project_describe'])
                setup_project_url.new_order(test_case['project_name'],test_case['product_name'], test_case['vendor'], test_case['place1'],
                                            test_case['place2'], test_case['place3'], test_case['place4'],
                                            test_case['remark'])
                setup_project_url.order_examine(test_case['sales_price'])

            except Exception as e:
                print(f"Test case failed: {str(e)}")
                continue  # 跳过当前用例，执行下一个用例




    def test_002(self, drivers, setup_project_url):
        test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', '项目下单')
        setup_project_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        for test_case in test_cases:
            try:
                setup_project_url.new_spu(test_case['project_number'],test_case['product_name'], test_case['vendor'], test_case['place1'],test_case['vendor'],
                                            test_case['place2'], test_case['place3'], test_case['place4'],
                                            test_case['remark'])
                setup_project_url.order_examine(test_case['sales_price'],test_case['project_number'])
                setup_project_url.spu_examine(test_case['product_number'])
            except Exception as e:
                print(f"Test case failed: {str(e)}")
                continue  # 跳过当前用例，执行下一个用例



    def test_003(self, drivers, setup_project_url):
        # test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', '项目下单')
        setup_project_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        for test_case in self.test_cases:
            try:
                setup_project_url.new_spu(test_case['project_number'],test_case['product_name'], test_case['sku_name'], test_case['place1'],test_case['vendor'],
                                            test_case['place2'], test_case['place3'], test_case['place4'],
                                            test_case['remark'])
                setup_project_url.order_examine(test_case['sales_price'],test_case['project_number'])
                Login(drivers).login_out("一级审批", "111111")
                setup_project_url.pay_approval()
                Login(drivers).login_out("admin", "111111")
                setup_project_url.go_pay()
            except Exception as e:
                print(f"Test case failed: {str(e)}")
                continue  # 跳过当前用例，执行下一个用例


    def test_004(self, drivers, setup_project_url):
        setup_project_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        for test_case in self.test_cases:
            try:
                setup_project_url.new_project(test_case['company_name'], test_case['place'], test_case['project_name'],
                                              test_case['project_describe'])
                setup_project_url.new_vendor_link(test_case['product_name'],test_case['sku_name'])
                Login(drivers).login_out2()
                setup_project_url.get_url(ini._get('HOST', 'vendor_link'))
                Login(drivers).login("供应商", "a111111")
                setup_project_url.new_vendor_order(test_case['phone'])
                # Login(drivers).login_out("admin", "111111")
                # setup_project_url.order_examine()
                # setup_project_url.additionalAddressInfo(test_case['phone'])
            except Exception as e:
                print(f"Test case failed: {str(e)}")
                continue  # 跳过当前用例，执行下一个用例






if __name__ == '__main__':
    pytest.main(['TestCase/test_project.py'])

