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
class PageMerchatOrder(WebPage):
    """项目管理"""
    project_number = None


    def page_merchat_order(self):
        """
        商户下单列表 下单
        :return:
        """
        self.is_click(element['其他'])
        self.is_click(element['商户下单列表'])

