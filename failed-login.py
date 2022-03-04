from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()

# TUPLES OF LOGIN INPUT SCENARIOS
logins = [("regscorer1", "fmlx124"), #correct username, invalid password
          ("regscorer5", "fmlx123"), #invalid username, correct password
          ("regscore22", "fmlx1234")] #invalid username, invalid password

# DECORATOR FOR INPUT LOGIN USING PARAMETER
@pytest.mark.parametrize("acc, password",logins)
def test_InputLogin(acc,password):
    #GO TO FSS DEV URL
    driver.get("http://10.200.0.153:9090/")
    assert "Login - Formulatrix Score Server" in driver.title

    #IDENTIFY FORMS 
    input_acc = driver.find_element(By.ID,"formHorizontalEmail")
    input_pass = driver.find_element(By.ID,"formHorizontalPassword")
    
    #CLEAR FORMS
    input_pass.clear()
    input_acc.clear()

    # INPUT KEYS TO FORMS USING PARAMETER FROM TUPLES
    input_acc.send_keys(acc)
    driver.implicitly_wait(0.5)
    input_pass.send_keys(password)
    driver.implicitly_wait(0.5)

    #CHECK USER INPUTS OF FORMS
    assert acc == input_acc.get_attribute("value")
    assert password == input_pass.get_attribute("value")

    #SUBMIT BUTTON
    submit = driver.find_element(By.XPATH,"//button[@class='submit-button btn btn-default']")
    submit.click()
    driver.implicitly_wait(5)
    
    #CHECK ELEMENTS EXIST IF INVALID LOGIN == TRUE
    invalidlogin = driver.find_element(By.XPATH,"//div[@class='failed-login']/strong")
    driver.implicitly_wait(1)
    time.sleep(0.5)
    assert "User/password invalid" in invalidlogin.text
    print(acc + " + " + password + " = " + invalidlogin.text)

def test_tearDown():
    driver.quit()



