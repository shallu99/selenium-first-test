from selenium import webdriver
import time

driver = webdriver.chrome(" C:\\driver\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("UTH UK Limited")
driver.find_element_by_name("btnk").click()
time.sleep(5)
var = driver.quit
