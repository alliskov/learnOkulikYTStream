from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_product_title_is(self, title):
        product_title = self.driver.find_element(By.XPATH, '//div[@id="tbodyid"]/h2[@class="name"]')
        assert product_title.text == title
