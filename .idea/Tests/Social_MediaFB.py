from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome( executable_path='../../../Pythonintroduction/drivers/chromedriver.exe')
driver.get("https://sesorafrica.org/")
driver.maximize_window()


fb_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/header/div/div/div/div[3]/div/div/a[1]/i")))
fb_btn.click()


