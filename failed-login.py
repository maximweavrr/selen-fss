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

logins = [("regscorer1", "fmlx124"), ("regscorer5", "fmlx123"), ("regscore22", "fmlx1234")]
@pytest.mark.parametrize("acc, password",logins)
def test_InputLogin(acc,password,browser):
    #INPUTS
    driver.get("http://10.200.0.153:9090/")
    assert "Login - Formulatrix Score Server" in driver.title
    input_acc = driver.find_element(By.ID,"formHorizontalEmail")
    input_pass = driver.find_element(By.ID,"formHorizontalPassword")
    input_pass.clear()
    input_acc.clear()
    input_acc.send_keys(acc)
    time.sleep(2)
    input_pass.send_keys(password)
    time.sleep(2)
    assert acc == input_acc.get_attribute("value")
    assert password == input_pass.get_attribute("value")
    submit = driver.find_element(By.XPATH,"//button[@class='submit-button btn btn-default']")
    submit.click()
    driver.implicitly_wait(5)
    invalidlogin = driver.find_element(By.XPATH,"//div[@class='failed-login']/strong")
    driver.implicitly_wait(1)
    time.sleep(0.5)
    assert "User/password invalid" in invalidlogin.text
    time.sleep(2)

def test_tearDown(browser):
    driver.quit()



