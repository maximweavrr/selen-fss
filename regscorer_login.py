from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
from db_clear import *

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

# buka browser
driver = webdriver.Chrome(options=chrome_options)

# maximize window
driver.maximize_window()
driver.get("http://10.200.0.153:11000/")
assert "Login - Formulatrix Score Server" in driver.title

def test_loginUser1():
    username = "regscorer1"
    password = "fmlx123"
    # IDENTIFY & INPUT EMAIL AND PASSWORD FORMS
    input_acc = driver.find_element(By.ID,"formHorizontalEmail")
    input_acc.send_keys(username)
    input_pass = driver.find_element(By.ID,"formHorizontalPassword")
    input_pass.send_keys(password)
    
    # CHECK USER INPUT AGAINST THE FORMS VALUE
    assert username == input_acc.get_attribute("value")
    assert password == input_pass.get_attribute("value")
    
    # SUBMIT LOGINS
    submit = driver.find_element(By.XPATH,"//button[@class='submit-button btn btn-default']")
    submit.click()