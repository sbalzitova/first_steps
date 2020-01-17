from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    return y

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = browser.find_element_by_id('book')

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer_field = browser.find_element_by_id('answer')
answer_field.send_keys(y)

submit = browser.find_element_by_id('solve')
submit.click()

browser.quit()
