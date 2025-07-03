from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fixtures.web_config import (
    company_name
)
class CompanyDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.open_company_detail_card = (By.XPATH, f"//div[contains(@class, 'rounded-lg') and .//div[@class='text-lg font-bold' and normalize-space(text())='{company_name}']]//button[normalize-space(text())='Manage']")
        self.open_company_detail_button = (By.XPATH, ".//button[contains(text(), 'Manage')]")
        self.detail_company_name = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.detail_industry_type = (By.XPATH, "(//div[contains(@class,'grid grid-cols-2')]//button)[1]")
        self.detail_company_type = (By.XPATH, "(//div[contains(@class,'grid grid-cols-2')]//button)[2]")
        self.detail_country = (By.XPATH, "(//div[contains(@class,'flex flex-col')]//button)[2]")
        self.detail_province = (By.XPATH, "//button[contains(.,'JAWA TENGAH')]")
        self.detail_city = (By.XPATH, "//span[normalize-space(text())='KOTA SURAKARTA']")
        self.detail_district = (By.XPATH, "//button[contains(.,'LAWEYAN')]")
        self.detail_company_email = (By.XPATH, "//input[@placeholder='Input Email']")
        self.detail_company_phone = (By.XPATH, "//input[@placeholder='Input Mobile Number']")
        self.detail_company_address = (By.XPATH, "//textarea[@placeholder='Input Company Address']")
        self.detail_company_id = (By.XPATH, "//input[@placeholder='Input Company ID']")
    
    def get_company_name(self):
        name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_company_name)).get_attribute("value")
        return name
    
    def get_company_email(self):
        email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_company_email)).get_attribute("value")
        return email

    def get_company_phone(self):
        phone = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_company_phone)).get_attribute("value")
        phone = int(phone)
        return phone
    
    def get_company_address(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_company_address)).text
    
    def get_company_industry_type(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_industry_type)).text
    
    def get_company_type(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_company_type)).text
    
    def get_company_country(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_country)).text
    
    def get_company_province(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_province)).text
    
    def get_company_city(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_city)).text
    
    def get_company_district(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_district)).text

    def open_company_detail(self):
        company_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.open_company_detail_card))
        company_element.click()

    def get_company_id(self):
        company_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.detail_company_id)).get_attribute("value")
        config_path = "fixtures/mobile_config.py"
        lines = []
        with open(config_path, "r") as file:
            for line in file:
                if line.strip().startswith("valid_company_id"):
                    lines.append(f'valid_company_id = "{company_id}"\n')
                else:
                    lines.append(line)
        with open(config_path, "w") as file:
            file.writelines(lines)

        return company_id 