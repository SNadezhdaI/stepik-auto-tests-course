from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    
    x_item = browser.find_element_by_id("treasure")
    x_element = x_item.get_attribute("valuex")
    x = x_element
    y = calc(x)
    
    input4 = browser.find_element_by_id("answer");
    input4.send_keys(y);
    
    
    
    
    input1 = browser.find_element_by_id("robotCheckbox");
    input1.click();
    input2 = browser.find_element_by_id("robotsRule");
    input2.click();
    input3 = browser.find_element_by_css_selector(".btn");
    input3.click();
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()