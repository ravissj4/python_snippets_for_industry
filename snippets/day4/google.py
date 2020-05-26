import time
from selenium import webdriver

browser = webdriver.Chrome() # Firefox()

url = 'https://google.com'
browser.get(url)

"""
<input type='text' class='' id='' name='??' />
Note: class and id are mostly used for how the content is displayed, 
        but in the backend, for functional purposes, generally name is 
        the one which is used and hence likely to not change and hence more 
        reliable. 

<textarea name='??'><textarea>

Got from inspecting the searchbox element :-
<input name="q" type="text">
"""
time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name("q")
# print(search_el)
# search_el = browser.find_elements_by_css_selector("h1")
search_el.send_keys("selenium python")

"""
<input type='submit' />
<button type='submit' />
<form></form>
Note : in case of submit button, the type is the one which is reliable 
        because here even the name is not that important because what matters 
        is whether the button was clicked or not. 

Got from inspecting the submit button element :-
<input type="submit">
"""
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()