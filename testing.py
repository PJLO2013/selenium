from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.toolsqa.com/")

time.sleep(3)

btn_inicio = driver.find_element(By.CLASS_NAME,"navbar__tutorial-menu--menu-bars").click()

time.sleep(3)

btn_demo_site = driver.find_element(By.XPATH,"/html/body/header/nav/div/div/div[3]/div/div[1]/ul/li[3]/a").click()

time.sleep(15)


btn_elements = driver.find_element(By.CSS_SELECTOR,"#app > div > div > div.home-body > div > div:nth-child(1) > div > div.avatar.mx-auto.white > svg").click()

time.sleep(5)


