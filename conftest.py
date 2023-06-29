import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    obj = Service("C:/Users/Agiliad/Desktop/Selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=obj)
    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()