#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from common.readconfig import ini
import random
import time
from page_object.page_login import Login
element = Element('element')


class PageCategory(WebPage):

    def create_category(self):
        self.is_click(element['product_management'])
