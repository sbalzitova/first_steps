from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration1.html'
browser = webdriver.Chrome()
browser.get(link)

try:

    first_name_field = browser.find_element_by_class_name('first:required')
    first_name_field.send_keys('А')

    last_name_field = browser.find_element_by_class_name('second:required')
    last_name_field.send_keys('B')

    email_field = browser.find_element_by_class_name('third:required')
    email_field.send_keys('a@m.ru')
    # input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    # input1.send_keys("Sveta")
    # input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    # input2.send_keys("Bal")
    # input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    # input3.send_keys("a@m.ru")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()