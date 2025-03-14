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
click_groups = [[0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14]]


class PageDesign(WebPage):
    """项目管理"""
    project_number = None

    def new_design(self):
        """新增设计需求"""
        self.is_click(element['supply_chain'])
        self.is_click(element['设计需求'])
        self.is_click(element['新增设计需求'])
        self.input_drop(element['请输入项目编码'],'CSJC01121008',0)
        self.input_texts(element['input'],555,1)
        # 初稿截至时间：
        self.choose_time(element['初稿截止时间'],0,element['今天'],0)
        self.is_click(element['选择日期确定'])
        self.choose_time(element['终稿截止时间'],0,element['今天'],0)
        self.is_clicks(element['选择日期确定'],1)
        #设计类型
        self.click_for(element['请选择设计内容'],element['印刷物料'],element['海报'])
        #设计师类型
        self.click_for(element['请选择设计师类型'],element['骚客门'])
        self.is_clicks(element['+'],0)
        self.is_clicks(element['+'],1)
        self.is_click(element['el_checkbox__inner'])
        self.inset_image(element['type_file'], r'D:\app\open_ui\images\1.jpg', 0)
        self.is_clicks(element['el_radio_inner'],1)
        self.click_for(element['selct_please'],element['默认'])
        self.is_clicks(element['el_radio_inner'],3)
        self.input_texts(element['input'],'风格',10)
        self.input_texts(element['input'],'色系',11)
        self.is_clicks(element['selct_please'],1)
        self.is_clicks(element['JPG'],0)
        self.input_text(element['请输入设计要求'],'请输入设计要求')
        self.input_text(element['input_comment'],'请输入备注')
        self.is_click(element['设计确认'])




        sleep(1000)




        


















































