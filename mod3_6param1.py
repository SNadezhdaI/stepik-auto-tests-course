import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id_links = [
    236895,
    236896,
    236897,
    236898,
    236899,
    236903,
    236904,
    236905
    ]

     
    
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    
    yield browser
    print("\nquit browser..")
    time.sleep(10)
    browser.quit()

@pytest.mark.parametrize('id_link', id_links)
class TestSession():
    def test_parameter(self, browser, id_link):
        
        link = f"https://stepik.org/lesson/{id_link}/step/1"
        browser.get(link) 
        
        answer = str(math.log(int(time.time()+0.7)))
        
        input1 = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        input1.send_keys(answer);
        
        input2 = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        input2.click()
        
        input3 = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
        )
        feedback = input3.text
        assert feedback == "Correct!", f"{feedback}."
        