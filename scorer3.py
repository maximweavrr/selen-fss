from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
# from db_clear import *

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

# buka browser
driver = webdriver.Chrome(options=chrome_options)

# maximize window
driver.maximize_window()
driver.get("http://10.200.0.153:9090/")
assert "Login - Formulatrix Score Server" in driver.title

def test_loginUser2():
    username = "regscorer3"
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

def test_FSSScore():
    # IDENTIFY AND CHECK IF FSS SCORE MENU EXISTS
    driver.implicitly_wait(1)
    fss_score = driver.find_element(By.XPATH,"//button[@id='fss-score']//div[@class='title']")
    assert "FSS Score" == fss_score.text
    fss_score.click()

    # SCORES 10 TEST DATA IMAGES UNTIL NO IMAGE LEFT
    i = 0
    while i < 10:
        time.sleep(2)
        # CLICK OTHERS BUTTON
        driver.find_element(By.XPATH,"//button[@id='O']").click()
        i = i + 1
        time.sleep(1)
        print("Current Drop Scored: " + str(i) + "\n")
        totalscored = driver.find_element(By.XPATH,"//p[@class='score-note-header']")
        
        # CHECK IF TOTAL SCORED INFORMATION == "i" VALUE
        assert str(i) in  totalscored.text

# TEST DISPLAY IF THERE IS NO IMAGE LEFT, ONCE ALL IMAGES ARE SCORED
def test_noImageLeft():
    # IDENTIFY ELEMENT AND CHECK
    warningtext = driver.find_element(By.XPATH,"//div[@class='row warningText']")
    assert "There's no drop images for this status" == warningtext.text

def test_logOut():
    # IDENTIFY LOGOUT BUTTON AND ACTION
    logout_button = driver.find_element(By.ID,"LogOut")
    logout_button.click()
    
    #DELAY
    time.sleep(1)

    # IDENTIFY AND CHECK IMAGE IF IT REDIRECTS TO HOME PAGE AFTER LOGOUT
    img_home = driver.find_element(By.XPATH,"//div[@class='login']/img")
    assert "http://10.200.0.153:9090/dist/246617079a1a4836cced134fae1f05f8.png" == img_home.get_attribute("src")

def test_tearDown():
    driver.quit()