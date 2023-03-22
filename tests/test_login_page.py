from pages.login_page import LoginPage


def test_login_succesfully(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.type_email("floryn_11_98@yahoo.com")
    login_page.type_password("ceamaitareparola")
    login_page.click_on_login_button()

def test_login_with_invalid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.type_email("sadsd@test.com")
    login_page.type_password("ceamaislabaparola")
    login_page.click_on_login_button()
    assert "Logare sau parolă nevalidă." in login_page.get_error_message_text()

def test_login_without_email(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.type_password("ceamaitareparola")
    login_page.click_on_login_button()
    assert "Acest câmp este obligatoriu" in login_page.get_error_message_text_2()

def test_forgot_my_password(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.click_on_forgot_my_password_button()
    login_page.type_email_to_recover_the_password("floryn_11_98@yahoo.com")
    login_page.click_on_sent_button()



