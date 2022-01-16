
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../../../Pythonintroduction/drivers/chromedriver.exe')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field.send_keys("Asya10@gmail.com")

password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]")
password_field.send_keys("Asya")

login_field = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,"//a[contains(text(), 'Continue')]")))
login_field.click()
