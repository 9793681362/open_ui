#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from common.readconfig import ini
import random


vendor = Element('vendor')
element = Element('element')


class PageRpa(WebPage):
    """RPA下单"""

    def order_builder(self):
        """
        构造订单
        :return:
        """
        self.is_click(element['others'])
        self.is_click(element['订单调整'])
        sleep(1)
        self.is_clicks(element['el_checkbox__inner'],1)
        self.is_click(element['new_order_details'])
        sleep(1)
        self.input_texts(element['input'],'此处为下单人',3)
        self.select_address(element['input'],4)
        self.input_texts(element['shippingAddress'],'此处为详细地址',0)
        self.input_texts(element['remake'],'此处为备注信息',0)
        self.input_texts(element['请输入采购申请人'],'此处为采购申请人',0)
        self.is_click(element['添加商品'])
        self.input_texts(element['contentInput'],20240458,0)
        self.input_texts(element['input'],'10',8)
        self.is_click(element['添加商品'])
        self.input_texts(element['contentInput'],20240451,1)
        self.input_texts(element['input'],'10',10)
        self.is_click(element['提交'])
        sleep(5)


