from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://its.iust.ac.ir/hotspot/login.php")
assert "ورود به اینترنت دانشگاه علم و صنعت" in driver.title
username_elem = driver.find_element(By.NAME, "username")
username_elem.clear()
username_elem.send_keys("")

password_elem = driver.find_element(By.NAME, "password")
password_elem.clear()
password_elem.send_keys("")
password_elem.send_keys(Keys.RETURN)

# mouse handling
sleep(100)
pyautogui.moveTo(646, 609)
pyautogui.click()

assert "ورود 1" in driver.title
sleep(1)
driver.quit()

