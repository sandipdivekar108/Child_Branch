from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_Login(self):
        log = self.test_getlogger()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        headertext = self.driver.find_element(By.CLASS_NAME, "title").text
        log.debug(headertext)
        assert "Products" in headertext  # To make sure user lands on Products page

    def test_AddToCart(self):
        log = self.test_getlogger()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "btn_primary").click()
        # self.driver.find_element(By.ID, "shopping_cart_container").click()
        ExpectedText = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        log.info(ExpectedText)
        assert ExpectedText == '2'  # Since I have selected 2 items on products page

    def test_CheckOut(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.driver.find_element(By.CLASS_NAME, "btn_primary").click()
        self.driver.find_element(By.CLASS_NAME, "btn_primary").click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("sandip")
        self.driver.find_element(By.ID, "last-name").send_keys("divekar")
        self.driver.find_element(By.ID, "postal-code").send_keys("411048")
        self.driver.find_element(By.ID, "continue").click()