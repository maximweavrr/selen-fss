from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

#buka browser
driver = webdriver.Chrome(options=chrome_options)

#maximize window
driver.minimize_window()
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
    #ELEMENT EXISTENCE ASSERTION

def test_checkElementsHome():
    driver.implicitly_wait(5)
    fssmenu = driver.find_elements(By.XPATH,"//button[@class='card center']")
    fsslen = len(fssmenu)
    uname = driver.find_element(By.XPATH,"//div[@class='col-md-2 usernameLogout']//span[@class='']")
    assert "regscorer1" == uname.text
    #PRINTS RESULT COMMENTS
    # print(fsslen, uname.text)
    if str(fsslen) == "3" and uname.text == "regscorer1":
        print("Count of Menus: " + str(fsslen), "\nUsername marker is: " +uname.text)
    else:
        print("No menus")
    fss_score = driver.find_element(By.XPATH,"//button[@id='fss-score']//div[@class='title']")
    assert "FSS Score" == fss_score.text
    fss_disagreed = driver.find_element(By.XPATH,"//button[@id='fss-score disagreed']//div[@class='title']")
    assert "FSS Score Disagreed" == fss_disagreed.text
    fss_training = driver.find_element(By.XPATH,"//button[@id='training-image']//div[@class='title']")
    assert "Training Image" == fss_training.text
    
def test_tearDown():
    driver.quit()