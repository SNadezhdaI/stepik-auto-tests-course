from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    
    x_item = browser.find_element_by_id("input_value")
    x = x_item.text
    y = calc(x)
    
    input4 = browser.find_element_by_id("answer");
    input4.send_keys(y);
    
    input1 = browser.find_element_by_id("robotCheckbox");
    input1.click();
    input2 = browser.find_element_by_id("robotsRule");
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click();
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()