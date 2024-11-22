import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_product import PageProduct
from utils.times import sleep
from common.read_excel import load_test_cases_from_excel
from common.mysql import Mysql


class TestProduct:
    test_cases = load_test_cases_from_excel('../data/excel/test_case.xlsx', 'product')

    @pytest.fixture(scope='function', autouse=True)
    def setup_product_url(self, drivers):
        """实例化并打开浏览器并导航到项目 URL"""
        project = PageProduct(drivers)
        return project  # 返回 PageProject 实例

    def test_001(self, drivers, setup_product_url):
        setup_product_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")

        for test_case in self.test_cases:
            # try:
                setup_product_url.new_proposal(test_case['company_name'])
            #
            # except Exception as e:
            #     print(f"Test case failed: {str(e)}")
            #     continue  # 跳过当前用例，执行下一个用例

    def test_002(self, drivers, setup_product_url):
        setup_product_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")

        for test_case in self.test_cases:
            try:
                setup_product_url.product_link()
                Login(drivers).login_out2()
                setup_product_url.get_url(ini._get('HOST', 'product_link'))
                Login(drivers).login('供应商','a111111')
                setup_product_url.new_product(test_case['new_or_amend'])
                Login(drivers).login_out('admin','111111')
                setup_product_url.spu_check(test_case['check'])
            except Exception as e:
                print(f"Test case failed: {str(e)}")
                continue  # 跳过当前用例，执行下一个用例


    def test_003(self, drivers, setup_product_url):
        setup_product_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        for test_case in self.test_cases:
            # try:
                setup_product_url.spu_count_link()
                Login(drivers).login_out2()
                setup_product_url.get_url(ini._get('HOST', 'product_link'))
                Login(drivers).login('供应商', 'a111111')
                setup_product_url.new_product(0)
                Login(drivers).login_out('admin', '111111')
                setup_product_url.spu_check(test_case['check'])
                if  test_case['check'] == 1:
                    setup_product_url.get_url(ini._get('HOST', 'product_link'))
                    Login(drivers).login('供应商', 'a111111')
                    setup_product_url.new_product(test_case['new_or_amend'])
            # except Exception as e:
            #     print(f"Test case failed: {str(e)}")
            #     continue  # 跳过当前用例，执行下一个用例

    """
    新产品上架流程
    """
    def test_004(self, drivers, setup_product_url):
        setup_product_url.get_url(ini.url)
        Login(drivers).login("admin", "111111")
        for i in range(10):
            setup_product_url.new_product_listing_process()
            setup_product_url.new_sku_to_company()
            setup_product_url.product_details()
            sleep(1)

if __name__ == '__main__':
    pytest.main(['TestCase/test_product.py'])

