import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Replace with your actual username and password
username = "suryaprakash.v@solidpro-es.com"
password = "Surya@2802"

    # Create a WebDriver instance
driver = webdriver.Chrome()

    # Navigate to the login page
driver.get("https://www.solidprohrms.online/")  # Replace with the actual login page URL

    # Locate the username and password input fields
username_field = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[1]/form/div[1]/input")  # Replace with the actual ID or other locator
password_field = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[1]/form/div[2]/div/input")  # Replace with the actual ID or other locator

    # Send the username and password
username_field.send_keys(username)
password_field.send_keys(password)

    # Locate and click the login button
login_button = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[1]/form/button")  # Replace with the actual ID or other locator
login_button.click()

Checkin_button = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/nav/div[1]/div[2]/div[1]/button") 
Checkin_button.click()

time.sleep(1)
    # Close the WebDriver instance
driver.quit()
