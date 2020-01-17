from selenium import webdriver
import os


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

# current_dir = os.path.abspath(os.path.dirname(__file__))
# my_file = os.path.join(current_dir, 'file.txt')

my_name = browser.find_element_by_name('firstname')
my_name.send_keys("Sveta")
my_surname = browser.find_element_by_name('lastname')
my_surname.send_keys("B")
email = browser.find_element_by_name('email')
email.send_keys("a@b")
file = browser.find_element_by_id('file')
file.send_keys(r'C:\Users\sbalzitova\Documents\learning\selenium_course\selenium_env\file.txt')
button = browser.find_element_by_class_name('btn.btn-primary')
button.click()

browser.quit()
