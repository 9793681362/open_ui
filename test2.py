from selenium import webdriver
from page.webpage import WebPage, sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 初始化WebDriver，假设使用Chrome
driver = webdriver.Chrome()

# 打开目标网页
driver.get("https://open-t.handyprint.cn/admin")

driver.maximize_window()

# 输入用户名
username_element = driver.find_element(By.NAME, "username")
username_element.send_keys("admin")  # 替换为你的用户名

# 输入密码
password_element = driver.find_element(By.NAME, "password")
password_element.send_keys("111111")  # 替换为你的密码

sleep(4)

# 点击验证按钮
verify_button = driver.find_element(By.XPATH, '//span[text()="点击按钮进行验证"]')
verify_button.click()

# 等待验证完成（根据页面情况调整等待时间）

sleep(1)

# 点击登录按钮
login_button = driver.find_element(By.CSS_SELECTOR, '[type="button"]')
login_button.click()





# 等待登录完成（根据页面情况调整等待时间）
time.sleep(2)

button_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/ul/div[15]/li/div')

# 点击按钮
button_element.click()



elements = driver.find_elements(By.XPATH, "//*")


sleep(100)


# 退出登录
quit_button = driver.find_element(By.CSS_SELECTOR, '.el-icon-caret-bottom')
quit_button.click()

# 点击登出
logout_button = driver.find_element(By.XPATH, '//span[text()="登出"]')
logout_button.click()

# 等待登出完成（根据页面情况调整等待时间）
time.sleep(3)

# 关闭浏览器
driver.quit()
