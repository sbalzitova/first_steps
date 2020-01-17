from selenium import webdriver
import math


def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    return y

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

first_button = browser.find_element_by_class_name('trollface.btn.btn-primary')
first_button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

submit = browser.find_element_by_class_name('btn.btn-primary')
submit.click()

browser.quit()
