from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.switch_to.window(browser.window_handles[1]) #переключаемся на глвую вкладку

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print (x)
    y = calc(x)

    browser.find_element_by_id ("answer").send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
