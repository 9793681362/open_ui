#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from common.readconfig import ini
from datetime import datetime
import random
import time
from page_object.page_login import Login
element = Element('element')

class PageProduct(WebPage):
    """项目管理"""
    project_number = None

    def new_proposal(self, company):
        """新增提案"""
        self.is_click(element['product_management'])
        self.is_click(element['proosal_requirement'])
        self.is_click(element['new_proosal_requirement'])
        self.is_clicks(element['confirm'], 1)
        self.is_click(element['new_proosal_requirement'])
        self.is_clicks(element['confirm'], 1)
        self.input_drop(element['input_company_name'], company, 0)
        self.input_text(element['input_project_name'], "测试提案需求项目" + str(self.generate_random_float(10, 10000)))
        self.input_text(element['input_project_budget'], self.generate_random_float(10, 1000))
        self.is_click(element['plan_give_time'])
        self.is_click(element['确定2'])
        self.input_text(element['input_profit'], self.generate_random(1, 99))
        self.select_data(element['delivery_schedule_selection'], 0)
        self.input_text(element['请输入项目描述'], self.generate_random_chinese(30))
        self.input_text(element['请输入项目应用场景'], self.generate_random_chinese(30))
        self.input_text(element['请输入产品受众人群'], self.generate_random_chinese(10))
        self.input_text(element['请输入提案产品数量'], self.generate_random_float(1, 1000))
        self.input_text(element['请输入项目产品数量'], self.generate_random_float(1, 1000))
        # self.inset_image(element['type_file'],r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\抟力数智PPT提案.pptx',0)
        self.is_clicks(element['confirm'], 1)

    def product_link(self):
        """资源库创建商品链接"""
        self.is_click(element['product_management'])
        self.is_click(element['资源库'])
        self.mouse_hover(element['ppt'],self.generate_random(0,12))
        self.is_click(element['choose'])
        self.is_click(element['创建上架商品链接'])
        link = self.element_text(element['product_link'])
        ini._set('HOST', 'product_link',link)
        sleep(0.2)
        self.is_click(element['copy_link'])


    def new_product(self,new_or_amend):
        """供应商新增商品"""
        sleep(0.5)
        if new_or_amend == 0:
            self.is_click(element['去创建'])
        elif new_or_amend == 1:
            self.is_click(element['去修改'])
        self.product_name = '新建上架商品' + str(self.generate_random(0,1000))
        self.input_texts(element['input_goods'],self.product_name,0)
        self.inset_image(element['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\1.jpg', 0)
        self.inset_image(element['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\1.jpg', 1)
        self.inset_image(element['type_file'], r'C:\Users\admin\Desktop\daima\pytest_handopen_ui\images\1.jpg', 2)
        if new_or_amend == 0:
            self.is_clicks(element['selct_please'],0)
            self.is_click(element['测试1'])
            self.is_clicks(element['selct_please'],1)
            self.is_clicks(element['el_checkbox__inner'],1)
            self.input_texts(element['请输入工艺'], self.generate_random_chinese(6), 0)
        self.input_texts(element['请输入产品描述'],self.generate_random_chinese(20),0)
        self.click_drop_n(element['请选择一件代发'],self.generate_random(0,1),0)
        self.click_drop_n(element['selct_please'], 0, 2)
        self.click_drop_n(element['selct_please'], self.generate_random(0,1), 3)
        self.input_text(element['请输入包装形式'],self.generate_random_chinese(6))
        self.input_text(element['请输入税率'],self.generate_random_float(0,99))
        self.input_text(element['请输入包装起订量'],self.generate_random_float(0,99))
        self.click_drop_n(element['selct_please'], self.generate_random(0, 1), 4)
        self.is_click(element['保存'])

    def spu_check(self,check):
        """审核流程"""
        self.is_click(element['product_management'])
        self.is_click(element['待审核产品'])
        sleep(0.5)
        self.is_click(element['新品上架产品'])
        self.input_text(element['input_goods'],self.product_name)
        self.is_click(element['search'])
        if check == 0:
            self.is_clicks(element['审核通过'],1)
        elif check == 1:
            self.is_clicks(element['审核驳回'], 1)
            self.input_text(element['remake'],self.generate_random_chinese(30))
            self.is_click(element['确定'])




    def spu_count_link(self):
        """商品库创建商品链接"""
        self.is_click(element['product_management'])
        self.is_clicks(element['商品库'],2)
        self.choose_page(element['第1页'],0,1154)
        sleep(1.5)
        self.is_clicks(element['el_checkbox__inner'],self.generate_random_odd(1,9))
        self.is_click(element['创建上架商品链接'])
        link = self.element_text(element['product_link'])
        ini._set('HOST', 'product_link', link)
        self.is_click(element['copy_link'])



    """
    新商品上架流程 新增商品（2024/11/22）
    """
    def new_product_listing_process(self):
        self.is_click(element['product_management'])
        sleep(0.5)
        self.is_click(element['all_product'])
        self.is_click(element['单个新增商品'])
        self.input_drop(element['contentInput'],'827新增供应商',0)
        self.input_texts(element['input_goods'],'商品' + ' ' + str(self.generate_random(0, 1000))+ '  ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),0)
        self.is_click(element['selct_please'])
        self.is_click(element['箱包类'])
        self.is_click(element['精选箱包'])
        self.is_click(element['胸包'])
        self.inset_image(element['type_file'], 'C:/Users/admin/Desktop/Rick_blunt/open_ui/images/' + str(int(self.generate_random(1, 9))) + '.jpg', 0)
        self.inset_image(element['type_file'], 'C:/Users/admin/Desktop/Rick_blunt/open_ui/images/' + str(int(self.generate_random(1, 9))) + '.jpg', 1)
        self.inset_image(element['type_file'], 'C:/Users/admin/Desktop/Rick_blunt/open_ui/images/' + str(int(self.generate_random(1, 9))) + '.jpg', 2)
        self.input_text(element['发货时间'],'7天内发货')
        self.input_text(element['产品尺寸'],'150*300cm')
        self.input_texts(element['请输入'],'10kg',0)
        self.input_texts(element['请输入'],'99',1)
        self.input_drop(element['contentInput'],'全国包邮',1)
        self.input_texts(element['input'],'100张',11)
        self.is_click(element['提交'])


    """
    新产品上架流程  上架至商户商品
    """
    def new_sku_to_company(self):
        #self.is_click(element['product_management'])
        #sleep(0.5)
        #self.is_click(element['all_product'])
        sleep(1)
        self.is_click(element['选择商品'])
        self.is_clicks(element['el_radio_inner'],0)
        self.is_clicks(element['el_radio_inner'],5)
        self.is_clicks(element['el_radio_inner'],9)
        self.is_click(element['生成规格'])
        self.is_clicks(element['el_checkbox__inner'],13)
        self.input_drop(element['请选择商户'],'测试基础版小程序商户',0)
        self.is_click(element['上架至商户'])




    """
    新商品上架流程  所属商品详情页
    """
    def product_details(self):
        sleep(2)
        self.is_click(element['请选择商品分类'])
        self.is_clicks(element['el_checkbox__inner'],0)
        self.input_text(element['请输入商品描述'],'此处为商品描述')
        self.inset_image(element['type_file'], 'C:/Users/admin/Desktop/Rick_blunt/open_ui/images/' + str(
            int(self.generate_random(1, 9))) + '.jpg', 3)
        self.input_texts(element['input'],'10',2)
        self.is_click(element['未设置'])
        self.is_clicks(element['el_checkbox__inner'],0)
        self.is_clicks(element['el_checkbox__inner'],1)
        self.is_clicks(element['confirm'],1)
        self.is_click(element['上架'])
        self.is_click(element['提交'])
















































    
    
    
    
    
    
    
    
    
    
    
    
    
    
