import os
import time
import requests
import urlparse

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

url = 'https://www.instagram.com/therock/'
browser.get(url)

# need to get a post 
post_link_xpath = "//a[contains(@href, '/p/')]"
post_els = browser.find_elements_by_xpath(post_link_xpath)

if len(post_els) > 0:
    post_elem = post_els[0]

if post_elem != None:
    post_link = post_elem.get_attribute("href")
    browser.get(post_link)

videos_xpath = "//video"
imgs_xpath = "//img"
video_els = browser.find_elements_by_xpath(videos_xpath)
img_els = browser.find_elements_by_xpath(imgs_xpath)

base_dir = os.path.dirname(os.path.abspath(__file__))
imgs_dir = os.path.join(base_dir, "images")
videos_dir = os.path.join(base_dir, "videos")
os.makedirs(imgs_dir, exist_ok=True)
os.makedirs(videos_dir, exist_ok=True)

def scrape_and_save(elements, filetype=None):
    for el in elements:
        link = el.get_attribute("src")
        filename = urlparse(link).path
        if filetype == 'videos':
            filepath = os.path.join(videos_dir, filename)
        else:
            filepath = os.path.join(imgs_dir, filename)

        with requests.get(link, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192)
                    f.write(chunk)

scrape_and_save(video_els, "videos")
scrape_and_save(imgs_els, "imgs")

