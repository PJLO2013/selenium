from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=es&service=mail&ifkv=Af_xneHWaDoZdYcr4RnssYK153BRUh5mGoCfdax4Jb44bJcH0SFWru6UMyfZuA1gwjBxvCo79lyz&flowName=GlifWebSignIn&flowEntry=ServiceLogin#__utma=29003808.1270445324.1688006726.1688006726.1688006726.1&__utmb=29003808.0.10.1688007077194&__utmc=29003808&__utmx=-&__utmz=29003808.1688006726.1.1.utmcsr=google%7Cutmccn=(organic)%7Cutmcmd=organic%7Cutmctr=(not%20provided)&__utmv=-&__utmk=17116410")

time.sleep(2)
element_email = driver.find_element(By.ID,"identifierId")
element_email.send_keys("plopezorozco70@gmail.com")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#identifierNext > div > button > span").click()

time.sleep(5)

element_pass=driver.find_element(By.CLASS_NAME,"whsOnd zHQkBf")
element_pass.send_keys("Apolo123..")

element_clik = driver.find_element("VfPpkd-muHVFf-bMcfAe")
element_clik.click()
time.sleep(5)

element_clik = driver.find_element("V67aGc")
element_clik.click()

time.sleep(10)

driver.close()

