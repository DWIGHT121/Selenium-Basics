# searches specific items in google

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


search_item = input("Enter your topic you want to search in google")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://www.google.com")

search = driver.find_element_by_name("q")
search.send_keys("{}".format(search_item))
search.send_keys(Keys.RETURN)

time.sleep(15)

driver.close()
