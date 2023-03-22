
from selenium.webdriver.common.by import By

class LoginPage:

    URL = "https://www.reserved.com/ro/ro/customer/account/login/#login"
    EMAIL_FIELD = (By.CSS_SELECTOR, '[id="login[username]_id"]')
    PASS_FIELD = (By.CSS_SELECTOR, '[id="login[password]_id"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-selen="login-submit"]')
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, '[class="sc-dlfnuX XGRlC"]')
    ERROR_MESSAGE_TEXT_2 = (By.CSS_SELECTOR, '[class="text-field__ErrorMessage-sc-1vll61a-4 WGIUj"]')
    FORGOT_MY_PASSWORD_BUTTON = (By.CSS_SELECTOR, '[data-selen="forgot-password"]')
    EMAIL_FIELD_2 = (By.CSS_SELECTOR, '[id="email_id"]')
    SENT_BUTTON = (By.CSS_SELECTOR, 'body > div.popover-container > div > div.popover__PopoverContent-sc-1qk2upz-2.lgciYF > form > button')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def type_email(self, email):
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)

    def type_password(self, password):
        self.browser.find_element(*self.PASS_FIELD).send_keys(password)

    def click_on_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message_text(self):
        return self.browser.find_element(*self.ERROR_MESSAGE_TEXT).text

    def get_error_message_text_2(self):
        return self.browser.find_element(*self.ERROR_MESSAGE_TEXT_2).text

    def click_on_forgot_my_password_button(self):
        self.browser.find_element(*self.FORGOT_MY_PASSWORD_BUTTON).click()

    def type_email_to_recover_the_password(self,email_2):
        self.browser.find_element(*self.EMAIL_FIELD_2).send_keys(email_2)

    def click_on_sent_button(self):
        self.browser.find_element(*self.SENT_BUTTON).click()







