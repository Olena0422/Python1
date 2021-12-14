from selenium import webdriver


driver = webdriver.Chrome(executable_path='../../Pythonintroduction/drivers/chromedriver.exe')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")


email_input = driver.find_element_by_xpath("//*[@id=input-email]")
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("asya10@gmail.com")


password_login_field = driver.find_element_by_xpath("//*[@id=input-password]")
password_login_input = driver.find_element_by_id("input-password")
password_login_input.clear()
password_login_input.send_keys("Asya")

driver.quit()






