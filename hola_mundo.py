from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/")

print(driver.title)
time.sleep(15)

driver.close()
