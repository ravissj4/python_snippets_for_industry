import os
import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.instagram.com'

browser.get(url)

"""
<button class="sqdOP L3NKy y3zKF " type="button">
    <span class="coreSpriteFacebookIconInverted cneKx"></span>
    Log in with Facebook
</button>
"""
time.sleep(2)

login_via_facebook_btn_xpath = "//*[contains(text(), 'Log in with Facebook')]"
login_via_facebook_btn = browser.find_elements_by_xpath(login_via_facebook_btn_xpath)
login_btn = login_via_facebook_btn[0]
login_btn.click()


