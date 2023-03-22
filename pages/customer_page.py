from selenium.webdriver.common.by import By

class CustomerPage:

    URL = 'https://www.reserved.com/ro/ro/'
    SEARCH_INPUT_BUTTON = (By.CSS_SELECTOR, '[class="input__InputText-sc-1mxde2b-0 ipFxa"]')
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[type="search"]')
    ERROR_MESAGE_TEXT = (By.CSS_SELECTOR, '#algoliaContainer > div.search-panel-wrapper__StyledAlgoliaCatalogSearch-sc-1b3pij6-0.gVlFNH > div > div.search-results-wrapper__SearchResultsWrapper-lnm8aj-0.cjGUeD > div:nth-child(1)')
    PRODUCT_TEXT =(By.CSS_SELECTOR, '[class="hit-item__Title-cz15ax-4 dLJesq"]')
    PRODUCT = (By.CSS_SELECTOR, '[src="https://static.reserved.com/media/catalog/product/cache/850/a4e40ebdc3e371adff845072e1c73f37/4/7/4716U-MLC-001-1-602521.jpg"]')
    WOMEN_BUTTON = (By.CSS_SELECTOR, '[href="https://www.reserved.com/ro/ro/femei"]')


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def search_for_a_product(self):
        self.browser.find_element(*self.SEARCH_INPUT_BUTTON).click()

    def make_a_search(self,product):
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(product)

    def get_error_message(self):
        return self.browser.find_element(*self.ERROR_MESAGE_TEXT).text

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_TEXT).text

    def click_on_a_product(self):
        self.browser.find_element(*self.PRODUCT).click()

    def click_on_wommen_button(self):
        self.browser.find_element(*self.WOMEN_BUTTON).click()


