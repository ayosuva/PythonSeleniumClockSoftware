import os

import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):

    driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.abspath(__file__))+"\\src\\libs\\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

