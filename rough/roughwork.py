# from selenium import webdriver
# import os
# print(os.getcwd())
# driver_loc = os.getcwd().replace("ActTime","")+"/drivers"
# driver = webdriver.Chrome(executable_path=driver_loc + "/chromedriver.exe")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.get("http://localhost/login.do")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_xpath("//a[@id='loginButton']//div[contains(text(),'Login')]").click()
driver.implicitly_wait(10)


#driver.find_element_by_xpath("//div[contains(text(),'USERS')]").click()
#ele = driver.find_element_by_xpath("//a[@class='content users']//div[@class='img']")
#action = ActionChains(driver)
#action.move_to_element(ele).click().perform()
#action.move_by_offset(871,17).click().perform()

while True:
    try:
        driver.find_element_by_xpath("//a[@class='content users']//div[@class='img']").click()
        break
    except:
        print("waiting for element")


# wait = WebDriverWait(driver,20)
# element =wait.until(EC.element_to_be_clickable(By.XPATH("//a[@class='content users']//div[@class='img']")))
#element.click()


add_user= driver.find_element_by_xpath("//div[@class='buttonText']").click()
fname = driver.find_element_by_name("firstName").send_keys("rohn")
lname = driver.find_element_by_name("lastName").send_keys("k")
email = driver.find_element_by_name("email").send_keys("test@test.com")
uname = driver.find_element_by_name("username").send_keys("rohan7111")
pwd = driver.find_element_by_name("password").send_keys("manager")
re_pwd = driver.find_element_by_name("passwordCopy").send_keys("manager")


hire_date = driver.find_element_by_xpath("//tr[@id='ext-gen155']//td[@class='x-btn-right']").click()
select_date = driver.find_element_by_xpath("//span[contains(text(),'29')]").click()

driver.execute_script("scrollBy(0,250)")
#driver.find_element_by_xpath("//div[@id='userDataLightBox_cancelBtn']").click()
driver.find_element_by_xpath("//span[contains(text(),'Create User')]").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Create User')]")))