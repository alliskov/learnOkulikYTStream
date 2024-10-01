import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_sgs6_page(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_sgs6()
    product_page = ProductPage(driver)
    product_page.check_product_title_is("Samsung galaxy s6")


def test_count_monitor_models(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitors()
    time.sleep(1)
    homepage.check_monitors_amount(2)

