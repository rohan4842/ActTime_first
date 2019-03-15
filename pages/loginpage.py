from selenium import webdriver
from Testdata import constant as dataval

class Login:
    def __init__(self,driver):
        self.driver = driver
        self.un_text_box = "username"
        self.pwd_text_box = "pwd"
        self.Login_btn = "//a[@id='loginButton']//div[contains(text(),'Login')]"

    def enter_un(self):
        self.driver.find_element_by_name(self.un_text_box).send_keys(dataval.USERNAME)

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_text_box).send_keys(dataval.PASSWORD)

    def click_on_login(self):
        self.driver.find_element_by_xpath(self.Login_btn).click()




