from Testdata import constant as dataval
class Newuser:
    def __init__(self,driver):
        self.driver = driver
        self.user_list = "//a[@class='content users']//div[@class='img']"
        self.click_add_btn = "//div[@class='buttonText']"
        self.fname_txt_box = "firstName"
        self.lname_txt_box = "lastName"
        self.email_txt_box = "email"
        self.uname_txt_box = "username"
        self.pwd_txt_box = "password"
        self.repwd_txt_box = "passwordCopy"
        self.hire_date = "//tr[@id='ext-gen155']//td[@class='x-btn-right']"
        self.select_date = "//span[contains(text(),'29')]"
        self.scroll_bottom = "scrollBy(0,250)"
        self.create_new_user1 = "//div[@id='userDataLightBox_commitBtn']"
        self.cancel_btn = "//div[@id='userDataLightBox_cancelBtn']"

    def click_user_btn(self):
        while True:
            try:
                self.driver.find_element_by_xpath(self.user_list).click()
                break
            except:
                print("wait till element found")
    def click_add_user_btn(self):
        self.driver.find_element_by_xpath(self.click_add_btn).click()
    def enter_fname(self):
        self.driver.find_element_by_name(self.fname_txt_box).send_keys(dataval.FIRST_NAME)
    def enter_lname(self):
        self.driver.find_element_by_name(self.lname_txt_box).send_keys(dataval.LAST_NAME)
    def enter_email(self):
        self.driver.find_element_by_name(self.email_txt_box).send_keys(dataval.EMAIL)
    def enter_username(self):
        self.driver.find_element_by_name(self.uname_txt_box).send_keys(dataval.UNAME)
    def enter_password(self):
        self.driver.find_element_by_name(self.pwd_txt_box).send_keys(dataval.PASS)
    def enter_repassword(self):
        self.driver.find_element_by_name(self.repwd_txt_box).send_keys(dataval.REPASS)
    def hire_date_drop(self):
        self.driver.find_element_by_xpath(self.hire_date).click()
    def select_date_drop(self):
        self.driver.find_element_by_xpath(self.select_date).click()
    def scroll_bottom_page(self):
        self.driver.execute_script(self.scroll_bottom)
    def click_cerate_new_user1(self):
        self.driver.find_element_by_xpath(self.create_new_user1).click()
    def click_cancel_btn(self):
        self.driver.find_element_by_xpath(self.click_user_btn).click()





