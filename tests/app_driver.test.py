## CAN ONLY BE USED WITH FIREFOX ##

import time
import json
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

mock_data = None

with open("./MOCK_DATA.json", "r") as json_data:
    mock_data = json.load(json_data)


driver.get('http://localhost:5000')


def create_deals(deals_list: list):
    for deal in deals_list:
        add_button = driver.find_element(by=By.XPATH, value="/html/body/a")
        add_button.click()
        time.sleep(.25)
        company_name_input = driver.find_element(
            by=By.NAME, value="companyName")
        rm_input = driver.find_element(by=By.NAME, value="relationshipManager")
        deal_amount_input = driver.find_element(by=By.NAME, value="dealAmount")
        submit_button = driver.find_element(
            by=By.XPATH, value="/html/body/form/div/button")
        company_name_input.send_keys(deal["companyName"])
        time.sleep(.25)
        rm_input.send_keys(deal["relationshipManager"])
        time.sleep(.25)
        deal_amount_input.send_keys(deal["dealAmount"])
        time.sleep(.25)
        submit_button.click()
        print("Added new deal.")


create_deals(mock_data)


time.sleep(3)

driver.close()
