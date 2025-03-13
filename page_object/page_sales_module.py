#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from common.readconfig import ini
import random

vendor = Element('vendor')
element = Element('element')


class PageSalesModule(WebPage):
    """
    销售模块；新增备案
    """
    def add_record(self):
        self.is_click(element['销售管理'])
        self.is_click(element['新备案'])
        self.input_text(element['请输入客户企业/组织全称'],'新增备案/2025/3/5')
        self.click_input(element['添加'], '品牌1')
        self.is_click(element['展开更多'])
        self.input_dorp_click(element['请选择行业类型'],element['连锁加盟'],element['餐饮连锁'])
        self.inset_image(element['type_file'], 'C:/Users/Administrator/Desktop/open_ui/images/' + str(
            int(self.generate_random(1, 100))) + '.jpg', 0)
        self.inset_image(element['type_file'], 'C:/Users/Administrator/Desktop/open_ui/images/' + str(
            int(self.generate_random(1, 100))) + '.jpg', 1)
        self.input_text(element['请输入公司地址'],'公司地址')
        self.input_text(element['请输入官网地址'],'官网地址')
        self.input_text(element['请输入年销售额'],'1000')
        # sleep(3)
        self.wait_for_overlay_to_disappear()
        self.input_drop(element['el-select__input'],'测试销售',0)
        self.is_clicks(element['请输入客户企业/组织全称'],0)
        self.input_drop(element['请输入销售名称'],'员工2',0)
        self.is_click(element['开店'])
        self.input_texts(element['input'],'客户姓名',10)
        self.input_texts(element['input'],'17317795711',12)
        self.click_drop_n(element['请选择职位'],3,0)
        self.click_drop_n(element['请选择客户角色'],3,0)
        self.input_text(element['remake'],'此处是备注')
        self.is_click(element['确定按钮'])
        sleep(10)


    def add_daily_plan(self):
        self.is_click(element['销售管理'])
        self.is_click(element['销售日常管理'])
        self.is_click(element['新增日报'])
        self.input_drop(element['请输入公司名或品牌名'],'华泰人寿保险1602',0)
        self.is_click(element['新增任务'])
        self.input_text(element['remake'],'此处是任务计划')
        self.is_click(element['确定'])
        self.is_click(element['确定按钮'])
        sleep(10)

