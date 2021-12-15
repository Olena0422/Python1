

from selenium import webdriver

driver = webdriver.Chrome(executable_path='../../Pythonintroduction/drivers/chromedriver.exe')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")


new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn.click()


#Register Account
#first name
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class
firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Olena")

#last name
lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Brown")



#e-mail name
email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("Asya10@gmail.com")




#phone name
telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("123456")


# fax
fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_input = driver.find_element_by_id("input-fax")
fax_input.clear()
fax_input.send_keys("987654")


#company name
company_field = driver.find_element_by_xpath("//fieldset[2]/div[1]")
company_input = driver.find_element_by_id("input-company")
company_input.clear()
company_input.send_keys("Roshen")


#address1 name
address_field = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/fieldset[2]/div[2]/label")
address_field_class = address_field.get_attribute("class")
assert "required" in address_field_class
address_input = driver.find_element_by_id("input-address")
address_input.clear()
address_input.send_keys("12 Grant st")


#address2 name
address2_field = driver.find_element_by_xpath("//fieldset[2]/div[3]")
address2_input = driver.find_element_by_id("input-address2")
address2_input.clear()
address2_input.send_keys()


#city name
city_field = driver.find_element_by_xpath("//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys("Pittsburgh")


#postcode name
postcode_field = driver.find_element_by_xpath("//fieldset[2]/div[5]")
postcode_input = driver.find_element_by_id("input-postcode")
postcode_input.clear()
postcode_input.send_keys()


#country name
country_field = driver.find_element_by_xpath("//fieldset[2]/div[6]")
country_field_class = country_field.get_attribute("class")
assert "required" in country_field_class
country_input = driver.find_element_by_id("input-country")
country_input.clear()
country_input.send_keys("United States")


#regionstate name
regionstate_field = driver.find_element_by_xpath("//fieldset[2]/div[7]")
regionstate_field_class = regionstate_field.get_attribute("class")
assert "required" in regionstate_field_class
regionstate_input = driver.find_element_by_id("input-regionstate")
regionstate_input.clear()
regionstate_input.send_keys("PA")



#password name
password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Asya")



passwordconfirm_field = driver.find_element_by_xpath("//fieldset[3]/div[2]")
passwordconfirm_field_class = passwordconfirm_field.get_attribute("class")
assert "required" in passwordconfirm_field_class
passwordconfirm_input = driver.find_element_by_id("input-passwordconfirm")
passwordconfirm_input.clear()
passwordconfirm_input.send_keys("Asya")

continue_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div/div/input[2]")
continue_btn.click()


driver.quit()


