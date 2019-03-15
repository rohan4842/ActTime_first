from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://azure.microsoft.com/en-in/")
driver.maximize_window()

# scrollby pixel
# https://github.com/atinfo/awesome-test-automation(github)
# driver.execute_script("window.scrollBy(0,2000)","")

#scroll_by particular element
ele = driver.find_element_by_xpath("//h3[contains(text(),'DevOps')]")

# driver.execute_script("arguments[0].scrollIntoView();", ele)

#scroll end of page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")