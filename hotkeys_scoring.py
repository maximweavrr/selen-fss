from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
import psycopg2


hotkeys = [("0"), ("1"), ("2"), ("3"), ("4"), ("j"), ("t")]
@pytest.mark.parametrize('a', hotkeys)
def test_ScoreHotkeys(a):
    conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "fss_dev",
    user = "empi",
    password = "empi123",
    port = "5454"
    )

    cur = conn.cursor()

    delete_script = '''delete from imagescorelistdetail i where exists (select 1 from imagescorelist i2 where dataset='VIS2021Q3-SQA' and i2.id = i.id)'''

    cur.execute(delete_script)
    conn.commit()

    cur.close()
    conn.close()

    
    # ========== OPEN BROWSER =========== #
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")

    # buka browser
    driver = webdriver.Chrome(options=chrome_options)

    # maximize window
    driver.maximize_window()
    driver.get("http://10.200.0.153:11000/")
    assert "Login - Formulatrix Score Server" in driver.title

    # ========== LOGIN =========== #
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

    # ========== SELECT FSS SCORE MENU =========== #
    driver.implicitly_wait(2)
    fss_score = driver.find_element(By.XPATH,"//button[@id='fss-score']//div[@class='title']")
    fss_score.click()
    

    # ========== HOTKEYS =========== #
    driver.implicitly_wait(2)
    time.sleep(0.5)
    i = 0
    while i < 10:
        webdriver.ActionChains(driver).send_keys(a).perform()
        driver.find_element(By.ID,"SUBMIT_BUTTON").click()
        time.sleep(2)
        i = i + 1
        print("Current Drop Scored: " + str(i) + "using hotkey " + a )
        
        # CHECK IF TOTAL SCORED INFORMATION == "i" VALUE
        totalscored = driver.find_element(By.XPATH,"//p[@class='score-note-header']")
        assert str(i) in  totalscored.text
    
    # ========== TEARDOWN =========== #
    driver.quit()
