from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_item = browser.find_element_by_id("num1")
    x = x_item.text
    y_item = browser.find_element_by_id("num2")
    y = y_item.text
    
    sum1 = str(int(x) + int(y))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum1)
    
    input3 = browser.find_element_by_css_selector(".btn");
    input3.click();
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()