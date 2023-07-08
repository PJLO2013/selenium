from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://outlook.live.com/owa/")

time.sleep(3)

element_usr=driver.find_element(By.XPATH,"/html/body/header/div/aside/div/nav/ul/li[2]/a").click()

time.sleep(3)

element_email = driver.find_element(By.ID,"i0116")
element_email.send_keys("comcamp2005@hotmail.com")

time.sleep(3)

btn_next = driver.find_element(By.ID,"idSIButton9").click()

time.sleep(3)

element_pass = driver.find_element(By.NAME,"passwd")
element_pass.send_keys("dftocomptonstyle")

time.sleep(3)

btn_sign_in = driver.find_element(By.ID,"idSIButton9").click()

time.sleep(3)

btn_no = driver.find_element(By.ID,"idBtn_Back").click()

time.sleep(8)
