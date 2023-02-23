#!/usr/local/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

apEmail = 'admin'
apPassword = 'Admin_Password'

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


def apToggleControl():
    driver.get("http://192.168.3.1")
    driver.find_element("id", "user_name_field").send_keys(apEmail)
    driver.find_element("id", "password_field").send_keys(apPassword)
    driver.find_element("id", "login_btn").click()

    driver.get("http://192.168.3.1/#/html/wireless/wireless/radio")
    ### wait for 2.4GHz radio toggle to be clickable then click
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID,"radio_setting_24enable"))
    )
    driver.find_element("id", "radio_setting_24enable").click()

    ### wait for apply button to be clickable and click to apply changes
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID,"radio_setting_apply"))
    )
    driver.find_element("id", "radio_setting_apply").click()

if __name__ == '__main__':
    apToggleControl()


# http://192.168.3.1/#/html/wireless/wireless/radio
# href="#/html/wireless/wireless/radio"
# radio_setting_24enable
# radio_setting_24ax