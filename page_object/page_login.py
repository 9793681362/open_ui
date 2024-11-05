#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class Login(WebPage):
    """搜索类"""

    def login(self,username,password):
        self.input_text(login['username'],username)
        self.input_text(login['password'],password)
        self.is_click(login['Verify_button'])
        self.is_click(login['login_link'])


    def login_out(self,username,password):
        self.is_click(login['quit_but'])
        self.is_click(login['quit'])
        self.input_text(login['username'],username)
        self.input_text(login['password'],password)
        self.is_click(login['Verify_button'])
        self.is_click(login['login_link'])


    def login_out2(self):
        self.is_click(login['quit_but'])
        self.is_click(login['quit'])