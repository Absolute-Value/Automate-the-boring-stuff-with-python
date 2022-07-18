#! /usr/bin/env python3
# 11.10.3_2048.py - 2048

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://play2048.co/')
html_elem = browser.find_element(By.TAG_NAME, 'html')
for i in range(100):
    html_elem.send_keys(Keys.UP)
    time.sleep(0.2)
    html_elem.send_keys(Keys.RIGHT)
    time.sleep(0.2)
    html_elem.send_keys(Keys.DOWN)
    time.sleep(0.2)
    html_elem.send_keys(Keys.LEFT)
    time.sleep(0.2)

browser.quit()