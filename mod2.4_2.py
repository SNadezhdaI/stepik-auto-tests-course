from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    price_item = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    
    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click();

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    
    x_item = browser.find_element_by_id("input_value")
    x = x_item.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer");
    input1.send_keys(y);
    
    button1 = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button1.click();  
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()