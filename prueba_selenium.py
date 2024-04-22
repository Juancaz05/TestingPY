from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
opciones = Options()
opciones.add_argument("--disable-notifications")


driver = webdriver.Chrome(options=opciones)


driver.get('https://syspass.org/en')

time.sleep(2)
button1 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/a"))
)
button1.click()
time.sleep(2)
User_input = driver.find_element(By.XPATH, '//*[@id="user"]')
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')

User_input.send_keys("demo")
time.sleep(2)
password_input.send_keys("syspass")
time.sleep(2)
buttonLogin = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="btnLogin"]/span'))
)
buttonLogin.click()
time.sleep(5)
driver.quit()


