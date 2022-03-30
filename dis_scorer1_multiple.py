from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
# from db_clear import *
# from regscorer_login import *
# from regscorer_menu import *

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

def test_DisagreedScore():
    # IDENTIFY AND CHECK IF FSS SCORE MENU EXISTS
    driver.implicitly_wait(1)
    fss_disagreed = driver.find_element(By.XPATH,"//button[@id='fss-score disagreed']//div[@class='title']")
    assert "FSS Score Disagreed" == fss_disagreed.text
    fss_disagreed.click()

    # SCORES FIRST 1 IMAGES AS PRECIPITATE, SCORES AS CLEAR FOR THE REST
    i = 0
    while i < 1:
        canvas = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//canvas"))) 
        if canvas:
            time.sleep(0.3)
            scorebutton1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='1']")))
            scorebutton1.click()
            scorebutton2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='3']")))
            scorebutton2.click()
            submitbutton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"SUBMIT_BUTTON")))
            submitbutton.click()
            time.sleep(0.3)
        else:
            print("Canvas not visible")
        i = i + 1
        print("Current Drop Scored: " + str(i) + "\n")

    while 0 < i <= 4:
        canvas = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//canvas"))) 
        if canvas:
            time.sleep(0.3)
            scorebutton3 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='6']")))
            scorebutton3.click()
            scorebutton4 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='0']")))
            scorebutton4.click()
            submitbutton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"SUBMIT_BUTTON")))
            submitbutton.click()
            time.sleep(0.3)
        else:
            print("Canvas not visible")
        i = i + 1
        print("Current Drop Scored: " + str(i) + "\n")
       
        # CHECK IF TOTAL SCORED INFORMATION == "i" VALUE
        totalscored = driver.find_element(By.XPATH,"//p[@class='score-note-header']")
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
    assert "dist/246617079a1a4836cced134fae1f05f8.png" in img_home.get_attribute("src")

def test_tearDown():
    driver.quit()
