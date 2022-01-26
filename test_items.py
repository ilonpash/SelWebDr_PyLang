from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    add_to_basket_button = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert add_to_basket_button >0, "'Add to basket' button is not exist"