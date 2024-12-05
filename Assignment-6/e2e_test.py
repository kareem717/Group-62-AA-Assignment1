from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5007/sign-up")
time.sleep(2)

driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "password").send_keys("testpassword")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
time.sleep(2)

# assert "Sign Up Successful" in driver.page_source

driver.get("http://localhost:5007/login")
driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "password").send_keys("testpassword")
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
time.sleep(2)

# assert "Welcome" in driver.page_source

driver.find_element(By.XPATH, "//a[contains(@class, 'bg-gray-200')]").click()
time.sleep(2)

# assert "Purchase" in driver.page_source

driver.quit()