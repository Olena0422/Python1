from selenium import webdriver

driver = webdriver.Chrome(executable_path='../../../Pythonintroduction/drivers/chromedriver.exe')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

continue_btn = WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/form/div/div/input[2]")))
continue_btn.click()

register_title = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,"/html/body//h1")))













