from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin.dclutter4u.com/")
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("Admin@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(50)

# WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
time.sleep(5)