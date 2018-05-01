from selenium import webdriver
import time

# driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver = webdriver.Chrome(executable_path='../driverchrome/chromedriver.exe')
driver.get("b" )
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()

# import requests
#
#
# r = requests.post("http://pythonscraping.com/pages/javascript/ajaxDemo.html" )
# print(r.text)
