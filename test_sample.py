from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
#class TestSample():
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/sai/Desktop/Drivers/chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():

    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(10)
   # x = driver.title()
   # print(x)
  #  assert x == "OrangeHRM"

def teardown():
    driver.close()
    driver.quit()






