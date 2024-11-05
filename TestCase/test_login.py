#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
from common.readconfig import ini
from page_object.page_login import Login
from page_object.page_project import PageProject
from utils.logger import log


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_open(self, drivers):
        """打开开放平台"""
        self.login = Login(drivers)
        self.login.login()
        self.login.get_url(ini.url)

    def test001_login(self, drivers,username,password):
        """登录"""
        self.login.login(username,password)

    def test002_login_out(self,username,password):
        """登出"""
        self.login.login_out(username,password)







if __name__ == '__main__':
    pytest.main(['TestCase/test001_login.py'])

