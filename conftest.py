import pytest
from Testdata import constant as dataval
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser", default ="chrome",action = "store", help ="enter name")
@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    driver.get(dataval.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    #yield
    #driver.quit()