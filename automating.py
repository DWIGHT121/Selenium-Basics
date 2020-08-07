# logs in facebook using email and password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

var = input("Your email")
var2 = input("Your password")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.facebook.com/")
print(driver.title)

search = driver.find_element_by_id("email")
search.send_keys("{}".format(var))
search.send_keys(Keys.TAB)

search = driver.find_element_by_id("pass")
search.send_keys("{}".format(var2))
search.send_keys(Keys.RETURN)


time.sleep(35)

driver.close()
