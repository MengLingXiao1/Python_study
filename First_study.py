# -*- coding: utf-8 -*-
# @Author  : Mlx
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
print driver.name
print driver.title
