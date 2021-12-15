from selenium import webdriver


driver = webdriver.Chrome(executable_path='../../Pythonintroduction/drivers/chromedriver.exe')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")


email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("asya10@gmail.com")


password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("asya10")

login_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/form/input")


login_btn.click()

driver.quit()

#driver.quit()








