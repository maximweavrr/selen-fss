from cgitb import text
from tkinter import END
from turtle import clear
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
from regscorer_login import *

def test_openTrainingImage():
    driver.implicitly_wait(3)
    trainingmenu = driver.find_element(By.XPATH,"//button[@id='training-image']")
    trainingmenu.click()


def test_canvasExist():
    canvas = driver.find_element(By.XPATH,"//div[@class='row dropContentRow oneDropContentRow']/canvas")
    canvas_id = "2024889"
    canvas_id == canvas.get_attribute("id")


def test_disableToScore():
    # IDENTIFY EACH SCORES ELEMENT
    disabled_button = driver.find_elements(By.XPATH,"//table[@class='scoreTableStyle']//button")

    if len(disabled_button)  == 12:
        for disabled in disabled_button:
            assert False == disabled.is_enabled()


def test_SelectedScore1():
    # IDENTIFY IF ONLY 1 BUTTON IS IN SELECTED STATE
    selectedbutton = driver.find_elements(By.XPATH,"//table[@class='scoreTableStyle']//button[@style='height: 5vw; background: rgb(135, 222, 135);']")
    if len(selectedbutton) == 1:
        # ASSERT IF PRECIPITATE IS THE SELECTED BUTTON
        for button in selectedbutton:
            assert "P" == button.get_attribute("id") 


def test_ScoreNote1():
    # SCROLL DOWN
    time.sleep(1)
    end_page = driver.find_element(By.XPATH,"//div[@id='inner-sidebar']").click()
    end_page.send_keys(Keys.END)

    # IDENTIFY ELEMENTS
    regscorer1 = driver.find_element(By.XPATH,"//td[text()='regscorer1']/following-sibling::td/b")
    regscorer2 = driver.find_element(By.XPATH,"//td[text()='regscorer2']/following-sibling::td/b")
    regscorer3 = driver.find_element(By.XPATH,"//td[text()='regscorer3']/following-sibling::td/b")
    pmscorer1 = driver.find_element(By.XPATH,"//td[text()='pmscorer1']/following-sibling::td/b")
    pmscorer2 = driver.find_element(By.XPATH,"//td[text()='pmscorer2]']/following-sibling::td/b")
    pmscorer3 = driver.find_element(By.XPATH,"//td[text()='pmscorer3']/following-sibling::td/b")

    # ASSERTIONS SCORE FROM EACH SCORERS
    assert "0" == regscorer1.text
    assert "1" == regscorer2.text
    assert "2" == regscorer3.text
    assert "1" == pmscorer1.text
    assert "1" == pmscorer2.text
    assert "1" == pmscorer3.text


def test_navigateImagesNext1():
    # IDENTIFY ELEMENTS
    nextbutton = driver.find_element(By.XPATH,"//button[@id='NEXT_BUTTON']")
    canvasold_id = "2024889"
    canvasnew_id = "2024890"

    # CLICK NEXT
    nextbutton.click()
    time.sleep(1)
    
    # ASSERT IF THE CANVAS ID IS CHANGED AFTER NAVIGATION 
    canvas = driver.find_element(By.XPATH,"//canvas").get_attribute("id")
    assert canvasold_id != canvas
    assert canvasnew_id == canvas


def test_SelectedScore2():
    # IDENTIFY IF ONLY 1 BUTTON IS IN SELECTED STATE
    selectedbutton = driver.find_elements(By.XPATH,"//table[@class='scoreTableStyle']//button[@style='height: 5vw; background: rgb(135, 222, 135);']")
    if len(selectedbutton) == 1:
        # ASSERT IF PRECIPITATE IS THE SELECTED BUTTON
        for button in selectedbutton:
            assert "P" == button.get_attribute("id") 


def test_ScoreNote2():
    # SCROLL DOWN
    time.sleep(1)
    end_page = driver.find_element(By.XPATH,"//div[@id='inner-sidebar']").click()
    end_page.send_keys(Keys.END)

    # IDENTIFY ELEMENTS
    regscorer1 = driver.find_element(By.XPATH,"//td[text()='regscorer1']/following-sibling::td/b")
    regscorer2 = driver.find_element(By.XPATH,"//td[text()='regscorer2']/following-sibling::td/b")
    regscorer3 = driver.find_element(By.XPATH,"//td[text()='regscorer3']/following-sibling::td/b")
    pmscorer1 = driver.find_element(By.XPATH,"//td[text()='pmscorer1']/following-sibling::td/b")
    pmscorer2 = driver.find_element(By.XPATH,"//td[text()='pmscorer2]']/following-sibling::td/b")
    pmscorer3 = driver.find_element(By.XPATH,"//td[text()='pmscorer3']/following-sibling::td/b")

    # ASSERTIONS SCORE FROM EACH SCORERS
    assert "0" == regscorer1.text
    assert "1" == regscorer2.text
    assert "2" == regscorer3.text
    assert "1" == pmscorer1.text
    assert "1" == pmscorer2.text
    assert "1" == pmscorer3.text


def test_navigateImageNext2():
    # IDENTIFY ELEMENTS
    nextbutton = driver.find_element(By.XPATH,"//button[@id='NEXT_BUTTON']")
    canvasold_id = "2024890"
    canvasnew_id = "2024891"

    # CLICK NEXT
    nextbutton.click()
    time.sleep(1)
    
    # ASSERT IF THE CANVAS ID IS CHANGED AFTER NAVIGATION 
    canvas = driver.find_element(By.XPATH,"//canvas").get_attribute("id")
    assert canvasold_id != canvas
    assert canvasnew_id == canvas


def test_SelectedScore3():
    # IDENTIFY IF ONLY 1 BUTTON IS IN SELECTED STATE
    selectedbutton = driver.find_elements(By.XPATH,"//table[@class='scoreTableStyle']//button[@style='height: 5vw; background: rgb(135, 222, 135);']")
    if len(selectedbutton) == 1:
        # ASSERT IF PRECIPITATE IS THE SELECTED BUTTON
        for button in selectedbutton:
            assert "O" == button.get_attribute("id") 

def test_ScoreNote3():
    # SCROLL DOWN
    time.sleep(1)
    end_page = driver.find_element(By.XPATH,"//div[@id='inner-sidebar']").click()
    end_page.send_keys(Keys.END)
    
    # IDENTIFY ELEMENTS
    regscorer1 = driver.find_element(By.XPATH,"//td[text()='regscorer1']/following-sibling::td/b")
    regscorer2 = driver.find_element(By.XPATH,"//td[text()='regscorer2']/following-sibling::td/b")
    regscorer3 = driver.find_element(By.XPATH,"//td[text()='regscorer3']/following-sibling::td/b")
    pmscorer1 = driver.find_element(By.XPATH,"//td[text()='pmscorer1']/following-sibling::td/b")
    pmscorer2 = driver.find_element(By.XPATH,"//td[text()='pmscorer2]']/following-sibling::td/b")
    pmscorer3 = driver.find_element(By.XPATH,"//td[text()='pmscorer3']/following-sibling::td/b")

    # ASSERTIONS SCORE FROM EACH SCORERS
    assert "0" == regscorer1.text
    assert "1" == regscorer2.text
    assert "2" == regscorer3.text
    assert "1" == pmscorer1.text
    assert "1" == pmscorer2.text
    assert "1" == pmscorer3.text


def test_navigateImageNextEnd():
    # IDENTIFY ELEMENTS
    nextbutton = driver.find_element(By.XPATH,"//button[@id='NEXT_BUTTON']")
    nextbutton.click()
    driver.implicitly_wait(2)
    
    # IDENTIFY IF WARNING END OF IMAGES ELEMENTS EXISTS
    warningtext = driver.find_element(By.XPATH,"//div[@class='row warningText']")


def test_navigatePrevious1():
    prevbutton = driver.find_element(By.XPATH,"//button[@id='PREV_BUTTON']")
    prevbutton.click()

    time.sleep(1)
    canvas = driver.find_element(By.XPATH,"//canvas").get_attribute("id")
    canvasnew_id = "2024891"
    assert canvasnew_id == canvas


def test_navigatePrevious2():
    prevbutton = driver.find_element(By.XPATH,"//button[@id='PREV_BUTTON']")
    prevbutton.click()

    time.sleep(1)
    canvas = driver.find_element(By.XPATH,"//canvas").get_attribute("id")
    canvasold_id = "2024890"
    assert canvasold_id == canvas


def test_navigatePrevious3():
    prevbutton = driver.find_element(By.XPATH,"//button[@id='PREV_BUTTON']")
    prevbutton.click()

    time.sleep(1)
    canvas = driver.find_element(By.XPATH,"//canvas").get_attribute("id")
    canvasold_id = "2024889"
    assert canvasold_id == canvas


def test_tearDown():
    driver.quit()
    
