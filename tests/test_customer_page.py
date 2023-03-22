from pages.customer_page import CustomerPage
from time import sleep

def test_search_for_a_product(browser):
    customer_page = CustomerPage(browser)
    customer_page.load_page()
    customer_page.search_for_a_product()
    customer_page.make_a_search("veste")
    sleep(10)

def test_invalid_search(browser):
    customer_page = CustomerPage(browser)
    customer_page.load_page()
    customer_page.search_for_a_product()
    customer_page.make_a_search("sdsdsd")
    assert "Niciun rezultat" in customer_page.get_error_message()


def test_search_for_a_product2(browser):
    customer_page = CustomerPage(browser)
    customer_page.load_page()
    customer_page.search_for_a_product()
    customer_page.make_a_search("vesta cu adaos de lana")
    customer_page.click_on_a_product()


 def test_choose_a_category(browser):
     customer_page = CustomerPage(browser)
     customer_page.load_page()
     customer_page.click_on_wommen_button()
     sleep(5)




