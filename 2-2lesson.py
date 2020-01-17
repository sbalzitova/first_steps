from selenium import webdriver
import math


def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    return y

link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

button = browser.find_element_by_css_selector('button.btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radio = browser.find_element_by_id('robotsRule')
radio.click()


button.click()

browser.quit()
