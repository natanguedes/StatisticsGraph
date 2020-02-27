from selenium import  webdriver

driver=webdriver.Chrome("E:\\chrome\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")
driver.maximize_window()
search = driver.find_element_by_name("email")
search.send_keys("ngsneto@gmail.com")
passw = driver.find_element_by_name("pass")
passw.send_keys("1")
driver.find_element_by_name("submit").click()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("Facebook.png")
driver.quit()