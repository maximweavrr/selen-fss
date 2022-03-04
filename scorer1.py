from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
# from scorer1_login import *

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

#buka browser
driver = webdriver.Chrome(options=chrome_options)

#maximize window
driver.maximize_window()
driver.get("http://10.200.0.153:9090/")
assert "Login - Formulatrix Score Server" in driver.title

def test_loginUser1():
    input_acc = driver.find_element(By.ID,"formHorizontalEmail")
    input_acc.send_keys("regscorer1")
    assert "regscorer1" == input_acc.get_attribute("value")
    input_pass = driver.find_element(By.ID,"formHorizontalPassword")
    input_pass.send_keys("fmlx123")
    assert "fmlx123" == input_pass.get_attribute("value")
    submit = driver.find_element(By.XPATH,"//button[@class='submit-button btn btn-default']")
    submit.click()

def test_FSSScore():
    time.sleep(2)
    fss_score = driver.find_element(By.XPATH,"//button[@id='fss-score']//div[@class='title']")
    assert "FSS Score" == fss_score.text
    fss_score.click()
    i = 0
    while i < 10:
        driver.find_element(By.XPATH,"//button[@id='C']").click()
        i = i + 1
        time.sleep(2)
        print(str(i))
        totalscored = driver.find_element(By.XPATH,"//p[@class='score-note-header']")
        assert str(i) in  totalscored.text

def test_tearDown():
    driver.quit()