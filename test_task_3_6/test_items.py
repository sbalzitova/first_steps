import time


def test_add_to_basket_button_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    try:
        add_button = browser.find_element_by_class_name('btn-add-to-basket')
    except:
        add_button = None
    assert add_button is not None, 'There is no "Add to button" button on the page'
