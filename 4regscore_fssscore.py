from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
from db_clear import *
from regscorer_login import *
from regscorer_menu import *


def test_FSSScoreTitle():
    # OPEN FSS SCORE MENU
    fss_score = driver.find_element(By.XPATH,"//button[@id='fss-score']//div[@class='title']")
    fss_score.click()

    # CHECK MEN TITLE
    driver.implicitly_wait(2)
    menu_title = driver.find_element(By.XPATH,"//div[@class='col-md-6 page-title']//b")
    assert "FSS SCORE" == menu_title.text


def test_countOfScores():
    # IDENTIFY SCORE PADS
    scorebuttons = driver.find_elements(By.XPATH,"//span[@class='score-pad-text']")

    # CONDITIONS IF SCOREBUTTONS == 4, PRINT ALL SCORES
    if str(len(scorebuttons)) == "4":
        
        # PRINT SCORES AND COUNT OF MENUS
        print("Count of Buttons: " + str(len(scorebuttons)))
        
        # PRINT ALL EXISTING SCORE BUTTONS
        print("\nCPOX SCORES:")
        for cpox in scorebuttons:
            print(cpox.text) 
    else:
        # FAILED PRINT
        print("No Scores/Failed")


def test_ScoreCategories():
    # IDENTIFY CLEAR BUTTON
    clear_button = driver.find_element(By.ID,"C")
    
    # CHECK CLEAR BUTTON ICON
    clear_image = "http://10.200.0.153:11000/dist/ebe3be568910e04584aa438eece294e6.svg"
    clear_icon = driver.find_element(By.XPATH,"//button[@id='C']/img[@class='imgSocrePad']")
    assert clear_image == clear_icon.get_attribute("src")

    # IDENTIFY PRECIPITATE BUTTON
    preci_button = driver.find_element(By.ID,"P")
    
    # CHECK PRECIPITATE BUTTON ICON
    preci_image = "http://10.200.0.153:11000/dist/cdbdaabac145bd0d2cc80e6bdcc26be9.svg"
    preci_icon = driver.find_element(By.XPATH,"//button[@id='P']/img[@class='imgSocrePad']")
    assert preci_image == preci_icon.get_attribute("src")

     # IDENTIFY OTHER BUTTON
    other_button = driver.find_element(By.ID,"O")
    
    # CHECK OTHER BUTTON ICON
    other_image = "http://10.200.0.153:11000/dist/d9979c2c02e422b748be5425142aebaa.svg"
    other_icon = driver.find_element(By.XPATH,"//button[@id='O']/img[@class='imgSocrePad']")
    assert other_image == other_icon.get_attribute("src")

     # IDENTIFY CRYSTAL BUTTON
    crystal_button = driver.find_element(By.ID,"X")
    
    # CHECK CRYSTAL BUTTON ICON
    crystal_image = "http://10.200.0.153:11000/dist/82e1d0c4727a4a4f4c185ddc72b93e72.svg"
    crystal_icon = driver.find_element(By.XPATH,"//button[@id='X']/img[@class='imgSocrePad']")
    assert crystal_image == crystal_icon.get_attribute("src")


def test_DropImageInfo():  
    # CHECK DROP IMAGE INFO AREA
    dropinfo = driver.find_element(By.XPATH,"//div[@class='dropInfo']")
    dropinfotitle = driver.find_element(By.XPATH,"//div[@class='dropInfo']//p")
    assert "DROP IMAGE INFO" == dropinfotitle.text

    #CHECK INFORMATION 
    accountname = driver.find_element(By.XPATH,"//table[@class='tableStyleDropInfo']//td[text()='Account Name']")
    projectid = driver.find_element(By.XPATH,"//table[@class='tableStyleDropInfo']//td[text()='Project ID']")
    experimentid = driver.find_element(By.XPATH,"//table[@class='tableStyleDropInfo']//td[text()='Experiment ID']")
    welldetails = driver.find_element(By.XPATH,"//table[@class='tableStyleDropInfo']//td[text()='Well Name / Well ID - Drop ID']")


def test_hideSideBar():
    hidebutton = driver.find_element(By.XPATH,"//button[@id='SHOW_SIDEBAR']")
    hidebutton.click()
    time.sleep(0.5)
    try:
    #identify element
        sidebar = driver.find_element(By.XPATH,"//div[@class='col-md-3 sideBarMenuPadding']")
        print("Element still exist")
    except NoSuchElementException:
        print("Element doesn't exist")
    showbutton = driver.find_element(By.XPATH,"//button[@id='HIDE_SIDEBAR']")
    assert "button rotated" == showbutton.get_attribute("class")


def test_ShowSideBar():
    showbutton = driver.find_element(By.XPATH,"//button[@id='HIDE_SIDEBAR']")
    showbutton.click()
    time.sleep(0.5)
    try:
        showbutton
        print("Button is not rotated")
    except NoSuchElementException:
        print("Button is rotated")
    sidebar = driver.find_element(By.XPATH,"//div[@class='col-md-3 sideBarMenuPadding']")


def test_EnableAutoLevel():
    # IDENTIFY SWITCH AUTO LEVEL ELEMENTS
    switch = driver.find_element(By.XPATH,"//div[@class='switchAutoLevel']")
    switch_cond = driver.find_element(By.XPATH,"//div[@class='react-switch-handle']")
    yes_switch = driver.find_element(By.XPATH,"//div[@class='react-switch-bg']/div[1]")
    no_switch = driver.find_element(By.XPATH,"//div[@class='react-switch-bg']/div[2]")  
    
    # SWITCH AUTO-LEVEL BUTTON
    switch.click()

    # ASSERT
    time.sleep(0.5)
    assert "true" == switch_cond.get_attribute("aria-checked")
    assert "opacity: 1;" in yes_switch.get_attribute("style")
    assert "opacity: 0;" in no_switch.get_attribute("style")

def test_DisableAutoLevel():
    # IDENTIFY SWITCH AUTO LEVEL ELEMENTS
    switch = driver.find_element(By.XPATH,"//div[@class='switchAutoLevel']")
    switch_cond = driver.find_element(By.XPATH,"//div[@class='react-switch-handle']")
    yes_switch = driver.find_element(By.XPATH,"//div[@class='react-switch-bg']/div[1]")
    no_switch = driver.find_element(By.XPATH,"//div[@class='react-switch-bg']/div[2]")  
    
    # SWITCH AUTO-LEVEL BUTTON
    switch.click()

    # ASSERT
    time.sleep(0.5)
    assert "false" == switch_cond.get_attribute("aria-checked")
    assert "opacity: 0;" in yes_switch.get_attribute("style")
    assert "opacity: 1;" in no_switch.get_attribute("style")


def test_tearDown():
    driver.quit()
