#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from common.readconfig import ini
import random
import time

project = Element('project')


class PageProject(WebPage):
    """项目管理"""
    project_number = None

    def new_project(self, company_name, place, project_name, project_describe):
        """创建项目"""
        random_number = random.randint(1, 1000)
        self.is_click(project['order_project'])
        self.is_click(project['new_project'])
        self.is_clicks(project['input'], 0)
        self.input_drop(project['input'], company_name, 0)
        self.input_texts(project['input'], place, 1)
        self.select_data(project['input'], 3)
        self.input_texts(project['input'], project_name + str(random_number), 4)
        self.input_texts(project['input'], project_describe, 5)
        self.is_clicks(project['confirm'], 1)
        sleep(0.5)
        project_number = self.element_text(project['project_number'])
        split_text = project_number.split(":")
        self.project_number = split_text[1].strip() if len(split_text) > 1 else project_number
        self.__class__.project_number = split_text[1].strip() if len(split_text) > 1 else project_number
        self.is_click(project['copy_project_no'])

    def new_order(self, project_name, product_name, vendor, place1, place2, place3, place4, remark):
        """供应商下单"""
        self.is_click(project['order_project'])
        sleep(1)
        self.is_click(project['place_order'])
        sleep(0.5)
        self.is_click(project['hr_management'])
        self.is_clicks(project['input'], 0)
        try:
            self.input_texts(project['input'], self.__class__.project_number, 0)
        except:
            self.input_texts(project['input'], project_name, 0)
        self.is_clicks(project['search'], 0)
        self.is_click(project['new_order'], )
        self.is_click(project['select_goods'])
        self.is_clicks(project['input'], 4)
        self.is_clicks(project['product_name'], 1)
        self.input_texts(project['input'], product_name, 5)
        self.is_clicks(project['search'], 1)
        self.is_clicks(project['el_checkbox__inner'], 3)
        self.is_clicks(project['confirm'], 2)
        self.input_drop(project['placeholder'], vendor, 0)
        self.input_texts(project['input'], place1, 5)
        self.input_texts(project['input'], place2, 6)
        self.input_texts(project['input'], place3, 7)
        self.input_texts(project['input'], place4, 8)
        self.input_text(project['remake'], remark)
        self.is_clicks(project['confirm'], 1)
        sleep(1)
        self.is_click(project['确定'])

    def new_spu(self, project_number, product_name, sku_name, place1, vendor, place2, place3, place4, remake):
        """供应商自定义商品"""
        self.is_click(project['order_project'])
        sleep(1)
        self.is_click(project['place_order'])
        sleep(0.5)
        self.is_click(project['hr_management'])
        self.is_clicks(project['input'], 0)
        self.input_texts(project['input'], project_number, 0)
        self.is_clicks(project['search'], 0)
        self.is_click(project['new_order'], )
        self.is_click(project['select_goods'])
        self.is_click(project['customs_goods'])
        self.input_texts(project['input'], product_name + str(random.randint(1, 1000)), 4)
        self.input_texts(project['input'], sku_name, 5)
        self.input_texts(project['input'], self.generate_random(1, 100), 6)
        self.input_text(project['input_productionCost'], self.generate_random_float(1.0, 100))
        self.input_text(project['input_packagingCost'], self.generate_random_float(1.0, 100))
        self.input_text(project['input_shippingCost'], self.generate_random_float(1.0, 100))
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\1.jpg', 0)
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\2.jpg', 1)
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\3.jpg', 2)
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\4.jpg', 3)
        self.is_clicks(project['confirm'], 2)
        try:
            sleep(1)
            self.input_drop(project['placeholder'], vendor, 0)
        except:
            sleep(3)
            self.input_drop(project['placeholder'], vendor, 0)
        self.input_texts(project['input'], place2, 6)
        self.input_text(project['remake'], remake)
        self.is_clicks(project['confirm'], 1)
        sleep(0.5)
        self.is_click(project['确定'])

    def order_examine(self):
        """订单审核"""
        self.is_click(project['order_project'])
        self.is_click(project['order_exm'])
        try:
            self.input_texts(project['input'], self.__class__.project_number, 0)
        except:
            self.input_texts(project['input'], self.__class__.project_number, 0)
        self.is_clicks(project['search'], 0)

        for number in range(3):
            self.is_clicks(project['go_order_exm'], number)
            self.input_texts(project['contentInput'], round(random.uniform(0.01, 1000), 2), 4)
            self.is_click(project['confirm_sales'])

    def spu_examine(self, product_number):
        """自定义商品审核"""
        self.is_click(project['product_management'])
        self.is_click(project['pending_products'])
        self.is_click(project['linkage'])
        self.input_texts(project['input_product'], product_number, 1)
        self.is_clicks(project['search'], 1)
        self.is_click(project['assocProd'])

    def pay_approval(self):
        """一级审批"""
        self.is_click(project['finMgmt'])
        self.is_click(project['payApproval'])
        self.is_click(project['pass'])
        self.is_click(project['if_confirm'])

    def go_pay(self):
        """付款流程"""
        self.is_click(project['others'])
        self.is_click(project['payDoc'])
        self.is_clicks(project['pay'], 0)
        self.click_drop_n(project['payAccount'], 0, 0)
        self.is_clicks(project['confirm'], 1)

    def new_vendor_link(self, product_name, sku_name):
        self.is_click(project['order_project'])
        self.is_clicks(project['my_project'], 0)
        self.is_click(project['selct_please'])
        sleep(0.5)
        self.is_click(project['select2'])
        self.input_texts(project['input_product'], self.__class__.project_number, 0)
        self.is_click(project['search'])
        self.is_click(project['found_vendor_link'])
        self.is_click(project['select_goods'])
        self.is_clicks(project['down_button'], 2)
        self.is_clicks(project['product_name'], 0)
        self.input_texts(project['input_product'], product_name, 1)
        self.is_clicks(project['search'], 1)
        self.is_clicks(project['el_checkbox__inner'], 3)
        self.is_clicks(project['el_checkbox__inner'], 4)
        self.is_clicks(project['confirm'], 1)
        self.is_click(project['select_goods'])
        self.is_click(project['customs_goods'])
        self.input_texts(project['input_goods'], product_name + str(random.randint(1, 100000)), 0)
        self.input_texts(project['input_sku'], sku_name, 0)
        self.input_text(project['input_productionCost'], self.generate_random_float(1.0, 100))
        self.input_text(project['input_packagingCost'], self.generate_random_float(1.0, 100))
        self.input_text(project['input_shippingCost'], self.generate_random_float(1.0, 100))
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\1.jpg', 0)
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\2.jpg', 1)
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\3.jpg', 2)
        self.inset_image(project['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\4.jpg', 3)
        self.is_clicks(project['confirm'], 1)
        sleep(1.5)
        self.is_click(project['confirm_creation'])
        link = self.element_texts(project['link'], 2)
        ini._set('HOST', 'vendor_link', link)
        self.is_click(project['copy_link'])

    def new_vendor_order(self, phone):
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 0)
        self.input_texts(project['contentInput'], self.generate_random(1, 100), 1)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 2)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 3)
        self.input_texts(project['contentInput'], self.generate_random_chinese(5), 4)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 5)
        self.input_texts(project['contentInput'], self.generate_random(1, 100), 6)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 7)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 8)
        self.input_texts(project['contentInput'], self.generate_random_chinese(5), 9)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 10)
        self.input_texts(project['contentInput'], self.generate_random(1, 100), 11)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 12)
        self.input_texts(project['contentInput'], self.generate_random_float(1.0, 100), 13)
        self.input_texts(project['contentInput'], self.generate_random_chinese(5), 14)
        self.is_clicks(project['receivingInfoInput'], 0)
        self.input_text(project['receiverName'], self.generate_random_chinese(3))
        self.input_text(project['receiverPhoneNumber'], phone)
        self.select_address(project['input_town'], 0)
        self.input_texts(project['shippingAddress'], self.generate_random_chinese(10), 0)
        self.is_clicks(project['confirm'], 2)
        self.is_clicks(project['confirm'], 1)
        self.is_click(project['确定'])

    def additionalAddressInfo(self, phone):
        """补充收货地址"""
        self.is_click(project['order_project'])
        self.is_clicks(project['my_project'], 0)
        self.is_click(project['input'])
        sleep(0.5)
        self.is_click(project['select2'])
        self.input_texts(project['input_product'], self.__class__.project_number, 0)
        self.is_click(project['search'])
        self.is_click(project['project'])
        for _ in range(2):
            self.is_clicks(project['receivingInfoInput'], 0)
            self.input_text(project['receiverName'], self.generate_random_chinese(3))
            self.input_text(project['receiverPhoneNumber'], phone)
            self.select_address(project['input'], 6)
            self.is_click(project['receiverPhoneNumber'])
            self.input_texts(project['shippingAddress'], self.generate_random_chinese(10), 0)
            self.is_clicks(project['confirm'],1)








