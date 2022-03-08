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

# buka browser
driver = webdriver.Chrome(options=chrome_options)

# maximize window
driver.maximize_window()
driver.get("http://10.200.0.153:11000/")
assert "Login - Formulatrix Score Server" in driver.title

def test_loginUser():
    username = "pmscorer1"
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

def test_ScoringImage():
    # IDENTIFY AND CHECK IF FSS SCORE MENU EXISTS
    driver.implicitly_wait(1)
    scoring_image = driver.find_element(By.XPATH,"//button[@id='scoring-image']//div[@class='title']")
    assert "Scoring Image" == scoring_image.text
    scoring_image.click()

    # SCORES FIRST 2 IMAGES AS PRECIPITATE, SCORES THE REST AS CLEAR
    i = 0
    while i < 2:
        time.sleep(2)
        # CLICK CLEAR BUTTON
        driver.find_element(By.XPATH,"//button[@id='P']").click()
        i = i + 1
        time.sleep(1)
        print("Current Drop Scored: " + str(i) + "\n")
        # totalscored = driver.find_element(By.XPATH,"//p[@class='score-note-header']")

    while 2 <= i <= 3:
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@id='C']").click()
        i = i + 1
        time.sleep(1)
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