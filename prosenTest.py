from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path='/Users/aysebetulaksakal/Desktop/chromedriver'
url='https://demoqa.com/automation-practice-form'
name='John'
surname='Doe'
email='jdoe@procenne.com'
phone='5356916363'
subject='Arts'
picture='/Users/aysebetulaksakal/Downloads/picture.png'
address='3425 Stone Street, Apt. 2A, Jacksonville, FL 39404'
state='NCR'
city='Delhi'

driver = webdriver.Chrome(path)
driver.get(url)

sleep(2)

driver.find_element(By.ID, "firstName").send_keys(name)

driver.find_element(By.ID, "lastName").send_keys(surname)

driver.find_element(By.ID, "userEmail").send_keys(email)

male_web_element = driver.find_element_by_id("gender-radio-1")
print(male_web_element.is_selected())
driver.execute_script("arguments[0].click();", male_web_element)

driver.find_element(By.ID, "userNumber").send_keys(phone)

driver.find_element(By.ID, "uploadPicture").send_keys(picture)

sleep(2)

driver.find_element(By.ID, "currentAddress").send_keys(address)

products=driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
products.send_keys(state)
products.send_keys(Keys.ARROW_DOWN)
products.send_keys(Keys.ENTER)

sleep(2)

products=driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
products.send_keys(city)
products.send_keys(Keys.ARROW_DOWN)
products.send_keys(Keys.ENTER)

driver.find_element(By.ID, 'submit').click()

sleep(3)

print('Gut gemacht!')
driver.quit()
