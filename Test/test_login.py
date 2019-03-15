from selenium import webdriver
import pytest
from pages.loginpage import Login
from pages.adduserpage import Newuser

@pytest.mark.usefixtures("test_setup")
class Test_Acttime:
    def test_login(self):
        driver = self.driver
        lp = Login(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_on_login()

    def test_user_reg(self):
        driver = self.driver
        nu = Newuser(driver)
        nu.click_user_btn()
        nu.click_add_user_btn()
        nu.enter_fname()
        nu.enter_lname()
        nu.enter_email()
        nu.enter_username()
        nu.enter_password()
        nu.enter_repassword()
        nu.hire_date_drop()
        nu.scroll_bottom_page()
        nu.click_cerate_new_user1()














