from selenium import webdriver
import math


def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    return y


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id('treasure')
x = treasure.get_attribute('valuex')
y = calc(x)

answer_field = browser.find_element_by_id('answer')
answer_field.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

button = browser.find_element_by_css_selector('button.btn')
button.click()

browser.quit()
