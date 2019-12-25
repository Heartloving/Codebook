from selenium import webdriver  
import os

browser = webdriver.Chrome()  

url = "http://www.baidu.com"  
browser.get(url)

input= browser.find_element_by_id("kw")
input.send_keys("python")

browser.find_element_by_id("su").click()

#关闭浏览器
#browser.quit()
