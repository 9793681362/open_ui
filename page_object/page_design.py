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



        


















































