#! /usr/bin/env python3
# 11.10.1_CommandLineMailer.py - コマンドライン電子メーラー

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def send_email(address, text):
    browser = webdriver.Chrome()
    browser.get('https://sute.jp/')

    MAIL_ADDRESS = 'c0l9tcja2q'
    input_text = browser.find_element(By.NAME, 'user[login]')
    input_text.send_keys(MAIL_ADDRESS)
    time.sleep(0.1)
    
    make_address = browser.find_element(By.CLASS_NAME, 'btn-warning')
    make_address.click()
    time.sleep(1)

    make_mail = browser.find_element(By.CLASS_NAME, 'btn-success')
    make_mail.click()
    time.sleep(1)

    input_address = browser.find_element(By.NAME, 'draft[to]')
    input_address.send_keys(address)
    time.sleep(0.1)

    input_text = browser.find_element(By.NAME, 'draft[body]')
    input_text.send_keys(text)
    time.sleep(3)

    send_mail = browser.find_element(By.NAME, 'button')
    send_mail.click()
    time.sleep(5)

    send_mail = browser.find_element(By.CLASS_NAME, 'confirm')
    send_mail.click()
    time.sleep(5)

if len(sys.argv) < 3:
    print('使い方：python3 11.10.1_CommandLineMailer.py 電子メールアドレス 本文テキスト')
else:
    send_email(sys.argv[1], ' '.join(sys.argv[2:]))