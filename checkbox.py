from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/text-box")

time.sleep(3)

btn_check_box = driver.find_element(By.ID,"item-1").click()

time.sleep(5)

btn_cbx_plus = driver.find_element(By.CLASS_NAME,"rct-icon-expand-all").click()

time.sleep(3)

btn_cbx_all = driver.find_element(By.CSS_SELECTOR,"#tree-node > ol > li > span > label > span.rct-checkbox > svg").click()

time.sleep(3)

btn_cbx_all = driver.find_element(By.CLASS_NAME,"rct-icon-check").click()

time.sleep(3)

btn_cbx_collapse = driver.find_element(By.CLASS_NAME,"rct-option-collapse-all").click()

time.sleep(3)



#tree-node > div > button.rct-option.rct-option-expand-all > svg