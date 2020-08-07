# takes you to the Youtube channel specified

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

search1 = input("Enter the channel name you want to view")


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://www.youtube.com")

search = driver.find_element_by_xpath(
    "/html/body/ytd-app/div[@id='content']/div[@id='masthead-container']/ytd-masthead[@id='masthead']/div[@id='container']/div[@id='center']/ytd-searchbox[@id='search']/form[@id='search-form']/div[@id='container']/div[@id='search-input']/input[@id='search']")
search.send_keys("{}".format(search1))
search.send_keys(Keys.RETURN)

search3 = driver.find_element_by_xpath("/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@class='style-scope ytd-page-manager']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-channel-renderer[@class='style-scope ytd-item-section-renderer']/div[@id='content-section']/div[@id='info-section']/a[@id='main-link']/div[@id='info']/ytd-channel-name[@id='channel-title']/div[@id='container']/div[@id='text-container']/yt-formatted-string[@id='text']").click()


search4 = driver.find_element_by_xpath("/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-browse[@class='style-scope ytd-page-manager'][2]/ytd-two-column-browse-results-renderer[@class='style-scope ytd-browse grid grid-5-columns']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-browse-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer'][2]/div[@id='contents']/ytd-shelf-renderer[@class='style-scope ytd-item-section-renderer']/div[@id='dismissable']/div[@id='contents']/yt-horizontal-list-renderer[@class='style-scope ytd-shelf-renderer']/div[@id='scroll-container']/div[@id='items']/ytd-grid-video-renderer[@class='style-scope yt-horizontal-list-renderer'][1]/div[@id='dismissable']/div[@id='details']/div[@id='meta']/h3[@class='style-scope ytd-grid-video-renderer']/a[@id='video-title']")
search4.click()

time.sleep(20)
driver.close()
