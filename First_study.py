# -*- coding: utf-8 -*-
# @Author  : Mlx
from selenium import webdriver
import time
driver=webdriver.Chrome()
try:
    driver.get("https://www.baidu.com")
except:
    print driver.name
    print driver.title
finally:
    print time.ctime()
#测试何如dev分支