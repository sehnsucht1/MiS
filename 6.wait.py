# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:16:20 2020

@author: sehnsucht.
"""

from selenium import webdriver
url = 'https://www.baidu.com'
driver = webdriver.Chrome()
#设置位置之后的所有元素定位操作都有定位等待时间10秒
driver.implicitly_wait(10)
driver.get(url)
el = driver.find_element_by_xpath('//*[@id="s_lg_img"]')
print(el)