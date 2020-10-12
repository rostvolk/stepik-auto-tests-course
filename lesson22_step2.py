from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/selects1.html")

    num1=browser.find_element_by_id("num1").text
    num2=browser.find_element_by_id("num2").text
    print ("num1=",num1,"num2=",num2,"sum=",int(num1)+int(num2))
    select = Select(browser.find_element_by_tag_name("select.custom-select"))
    sum1=int(num1)+int(num2)
    select.select_by_value(str(sum1)) # ищем элемент с суммой

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
