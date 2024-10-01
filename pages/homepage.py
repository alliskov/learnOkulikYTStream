from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')
        assert self.driver.title == "STORE"

    def click_sgs6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitors(self):
        monitors_link = self.driver.find_element(By.XPATH, '//a[@id="itemc"][text()="Monitors"]')
        monitors_link.click()

    def check_monitors_amount(self, count):
        monitors = self.driver.find_elements(By.XPATH, '//div[@id="tbodyid"]/div/div[contains(@class,"card")]')
        assert monitors.__len__() == count
