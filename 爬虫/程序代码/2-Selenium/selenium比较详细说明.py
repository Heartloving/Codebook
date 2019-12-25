
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()

#2--访问页面
from selenium import webdriver

browser = webdriver.Chrome()     #定义浏览器对象
browser.get("https://www.taobao.com")
#print(browser.page_source)
#browser.close()

#3--查找元素
#--单个元素
from selenium import webdriver
browser = webdriver.Chrome()     #定义浏览器对象
browser.get("https://www.taobao.com")
#input_first = browser.find_element_by_id('q') #找到输入搜索物品名称的对话框的对象  
input_first = browser.find_element_by_id('q').send_keys("1111")  #在上述对话框中输入要搜索的物品
#input_second = browser.find_element_by_css_selector('#q').send_keys("1111")
#input_third = browser.find_element_by_xpath('//*[@id="q"]')
#input_third = browser.find_element_by_xpath('//*[@id="q"]').send_keys("1111")
#上述三种选择的完全一样


#browser.close()



#3--查找元素
#--多个元素
from selenium import webdriver
browser = webdriver.Chrome()     #定义浏览器对象
browser.get("https://www.taobao.com")
#lis = browser.find_elements_by_css_selector('.service-bd li')
lis = browser.find_elements_by_css_selector('.service-bd li a')

print(len(lis))
print(lis)
#browser.close()


#======================================
#4--元素交互操作

from selenium import webdriver
import time


browser = webdriver.Chrome()     #定义浏览器对象
browser.get("https://www.taobao.com")
input = browser.find_element_by_id('q')

input.send_keys('IPhone')
time.sleep(2)
input.clear()
input.send_keys('IPad')
button = browser.find_element_by_class_name('btn-search')
#btn-search是搜索框的类名
button.click()


#==================================
#7-----异常处理

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.find_element_by_id("hello")  #查找不存在的元素
'''
#下面进行捕获该异常
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
except TimeoutException:
    print("Time Out")
try:
    browser.find_element_by_id("hello")
except NoSuchElementException:
    print("No Element")
finally:
    browser.close()























