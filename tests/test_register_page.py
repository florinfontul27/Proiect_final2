from pages.register_page import RegisterPage
from time import sleep
def test_ceate_account_succesfully(browser):
    register_page = RegisterPage(browser)
    register_page.load_page()
    register_page.type_email("floringabi3@gmail.com")
    register_page.type_firstname("florin")
    register_page.type_lastname("fontul")
    register_page.type_password("ceamaitareparola")
    register_page.click_create_account_button()
    sleep(15)

def test_create_account_without_email(browser):
    register_page = RegisterPage(browser)
    register_page.load_page()
    register_page.type_firstname("florin")
    register_page.type_lastname("fontul")
    register_page.type_password("ceamaitareparola")
    register_page.click_create_account_button()
    assert "Acest câmp este obligatoriu" in register_page.get_error_message_text()
    sleep(15)