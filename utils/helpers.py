from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    user_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_input.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()