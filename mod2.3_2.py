from selenium import webdriver
import time
import math
import os 

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
    button = browser.find_element_by_tag_name("button")
    button.click();
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    
    x_item = browser.find_element_by_id("input_value")
    x = x_item.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer");
    input1.send_keys(y);
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click();  
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()