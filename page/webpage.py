#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from common.readelement import Element
from config.conf import cm
from utils.times import sleep
from utils.logger import log
import random
import time

vendor = Element('vendor')
element = Element('element')


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        try:
            return WebPage.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), locator)
        except:
            print('寻找单个元素失败')

    def find_elements(self, locator, number):
        """查找多个相同的元素"""
        try:
            return WebPage.element_locator(lambda *args: self.wait.until(
                EC.presence_of_all_elements_located(args)), locator)[number]
        except:
            print('寻找多个元素失败')

    # def find_element(self, locator):
    #     """寻找单个元素"""
    #     try:
    #         return WebPage.element_locator(lambda *args: self.wait.until(
    #             EC.presence_of_element_located(args)), locator)
    #     except TimeoutException:
    #         print(f"寻找单个元素超时: {locator}")
    #     except NoSuchElementException:
    #         print(f"未找到元素: {locator}")
    #     except Exception as e:
    #         print(f"寻找单个元素失败: {e}")
    #
    # def find_elements(self, locator, number):
    #     """查找多个相同的元素"""
    #     try:
    #         elements = WebPage.element_locator(lambda *args: self.wait.until(
    #             EC.presence_of_all_elements_located(args)), locator)
    #         return elements[number]  # 返回第 `number` 个元素
    #     except TimeoutException:
    #         print(f"寻找多个元素超时: {locator}")
    #     except IndexError:
    #         print(f"未找到第 {number} 个元素: {locator}")
    #     except Exception as e:
    #         print(f"寻找多个元素失败: {e}")

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    # 输入多个元素
    def input_texts(self, locator, txt, number):
        ele = self.find_elements(locator, number)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def is_clicks(self, locator, number):
        """点击"""
        self.find_elements(locator, number).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    def element_texts(self, locator, number):
        """获取当前的text"""
        _text = self.find_elements(locator, number).text
        log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    # 多元素 点击 下拉框
    def click_drop_n(self, locator, circulate, number):
        el = self.find_elements(locator, number)
        el.click()
        i = 0
        while i <= circulate:
            sleep(0.01)
            log.info("[webpage]:正在对{}多个元素实行下拉框操作，下拉{}位数".format(locator, circulate))
            el.send_keys(Keys.DOWN)
            i += 1
        log.info("[webpage]:正在对{}多个元素实行回车操作".format(locator))
        el.send_keys(Keys.ENTER)

    # 选择输入框内收货地址
    def select_address(self, locator, number):
        """"选择输入框内收货地址"""
        el = self.find_elements(locator, number)
        el.click()
        log.info("正在选择地址")
        self.find_element(Element('vendor')['beijing']).click()
        self.find_element(Element('vendor')['shixiaqu']).click()
        self.find_element(Element('vendor')['dongchengqu']).click()
        self.find_element(Element('vendor')['donghuamenjiedao']).click()

    def inset_image(self, locator, image, number):
        """插入图片"""
        el = self.find_elements(locator, number)
        log.info("[base]:正在对{}多个元素插入图片，图片为{}".format(locator, number))
        el.send_keys(image)

    # 输入下拉框
    def input_drop(self, locator, value, number):
        el = self.find_elements(locator, number)
        log.info("[webpage]:正在对{}单个元素实行点击事件".format(locator))
        el.click()
        sleep(1)
        log.info("[webpage]:正在对{}单个元素实行清空操作".format(locator))
        el.clear()
        log.info("[webpage]:正在对{}单个元素输入操作,输入的值为{}".format(locator, value))
        el.send_keys(value)
        sleep(0.5)
        log.info("[webpage]:正在对{}单个元素进行下拉操作".format(locator))
        el.send_keys(Keys.DOWN)
        log.info("[webpage]:正在对{}单个元素进行回车操作".format(locator))
        el.send_keys(Keys.ENTER)

    def select_data(self, locator, number):
        """选择日期今天"""
        el = self.find_elements(locator, number)
        el.click()
        sleep(0.5)
        ls = self.find_elements(Element('project')['today'], 0)
        ls.click()

    def generate_random(self, start, end):
        "随机数，不包含小数点"
        random_number = random.randint(start, end)
        return random_number

    def generate_random_even(self, start, end):
        random_number = random.randint(start, end)
        # 将随机数调整为偶数
        return random_number if random_number % 2 == 0 else random_number + 1

    def generate_random_odd(self, start, end):
        random_number = random.randint(start, end)
        # 将随机数调整为奇数
        return random_number if random_number % 2 != 0 else random_number + 1

    def generate_random_float(self, start, end):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise ValueError("Both start and end must be numbers")
        # 生成范围内保留两位小数的随机浮点数
        random_float = round(random.uniform(start, end), 2)
        return random_float

    def generate_random_chinese(self, num_chars):
        chinese_chars = ''
        for _ in range(num_chars):
            chinese_char = chr(random.randint(0x4e00, 0x9fa5))
            chinese_chars += chinese_char
        return chinese_chars

    def mouse_hover(self, locator, number):
        el = self.find_elements(locator, number)
        actions = ActionChains(self.driver)
        actions.move_to_element(el).perform()

    def choose_page(self, locator, start, end):
        el = self.find_element(locator)
        el.clear()
        el.send_keys(self.generate_random(start, end))
        el.send_keys(Keys.ENTER)

    # 点击小园钮
    def batch_click_actions(self, click_groups, action_element):
        """
        批量对一组元素执行点击操作，并在每组操作后点击指定动作元素。
        :param element:
        :param click_groups:
        :param action_element:
        :return:
        """
        for group in click_groups:
            for index in group:
                self.is_clicks(element['el_radio_inner'], index)
            self.is_click(action_element)