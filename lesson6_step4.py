from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Sveta")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Bal")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Saint Petersburg")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
