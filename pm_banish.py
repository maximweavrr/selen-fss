from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_loginUser1():
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

def test_BanishImageButton():
    # IDENTIFY AND CHECK IF PM DISCUSSION PAGE EXISTS
    driver.implicitly_wait(1)
    pm_discussion = driver.find_element(By.XPATH,"//button[@id='pm-discussion page']//div[@class='title']")
    assert "PM Discussion Page" == pm_discussion.text
    pm_discussion.click()

    # IDENTIFY BANISH IMAGE BUTTON
    time.sleep(1)
    canvas = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//canvas")))
    if canvas:
        time.sleep(0.3)
        banish_button = driver.find_element(By.XPATH,"//button[@id='BANISH_BUTTON']")
        banish_button.click()
        time.sleep(0.3)
    else:
        print("Canvas not visible")
    # banish_button = driver.find_element(By.XPATH,"//button[@id='BANISH_BUTTON']")
    # banish_button.click()
    # time.sleep(5)

    # IDENTIFY BANISH IMAGE POP-UP
def test_BanishPopUp():
    # time.sleep(5)
    banishment_popup = driver.find_element(By.XPATH,"//div[@class='overlay-popup-content']/div[@id='banishment-card']")
    banish_isdisplay = banishment_popup.is_displayed()
    assert True == banish_isdisplay

    # display_block = "display: block;"
    # assert display_block == banishment_popup.get_attribute("style")

    # CHECK DISCARD CHANGES
    discard_title = driver.find_element(By.XPATH,"//div[@id='banishment-card']//b")
    assert "Discard Change" == discard_title.text


def test_CancelBanish():
    # IDENTIFY CANCEL BUTTON 
    cancelbutton = driver.find_element(By.XPATH,"//div[@id='banishment-card']//button[@class='card-cancel-btn']")
    
    #CLICK CANCEL BUTTON
    cancelbutton.click()
    
    # IDENTIFY BANISHMENT POPUP STYLE STATUS
    banishment_popup = driver.find_element(By.XPATH,"//div[@class='overlay-popup-content']/div[@id='banishment-card']")
    banish_isdisplay = banishment_popup.is_displayed()
    assert False == banish_isdisplay


def test_BanishImage():
    # IDENTIFY BANISH IMAGE BUTTON
    time.sleep(2)
    banish_button = driver.find_element(By.ID,"BANISH_BUTTON")
    banish_button.click()

    # IDENTIFY BANISH IMAGE POP-UP
    time.sleep(3)
    banishment_popup = driver.find_element(By.XPATH,"//div[@class='overlay-popup-content']/div[@id='banishment-card']")
    banish_isdisplay = banishment_popup.is_displayed()
    assert True == banish_isdisplay

    # IDENTIFY PROCEED BUTTON
    proceedbutton = driver.find_element(By.XPATH,"//button[@class='card-proceed-btn']")
    proceedbutton.click()


# TEST DISPLAY IF THERE IS NO IMAGE LEFT, ONCE ALL IMAGES ARE SCORED
def test_noImageLeft():
    time.sleep(5)
    # IDENTIFY ELEMENT AND CHECK
    warningtext = driver.find_element(By.XPATH,"//div[@class='row warningText']")
    assert "There's no drop images for this status" == warningtext.text


def test_BanishButtonDisabled():
    warning_present = driver.find_element(By.XPATH,"//div[@class='row warningText']").is_displayed()
    if warning_present == True:
        banish_button = driver.find_element(By.ID,"BANISH_BUTTON")
        isdisabled = banish_button.is_enabled()
        assert False == isdisabled


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