from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CreateNewCompanyPage:
    def __init__(self, driver):
        self.driver = driver
        self.company_hyperlink = (By.XPATH, "//a[normalize-space(text())='Companies']")
        self.add_company_button = (By.XPATH, "//button[contains(.,'+ Add Company')]")
        self.company_name_input = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.email_input = (By.XPATH, "//input[@placeholder='Input Email']")
        self.phone_number_input = (By.XPATH, "//input[@placeholder='Input Phone']")
        self.industry_dropdown = (By.XPATH, "//button[contains(.,'Choose Industry Type')]")
        self.industry_automative_option = (By.XPATH, "//span[normalize-space(text())='Automotive']")
        self.company_type_dropdown = (By.XPATH, "//button[contains(.,'Choose Company Type')]")
        self.company_type_private_option = (By.XPATH, "//span[normalize-space(text())='Retailer']")
        self.language_dropdown = (By.XPATH,"//button[contains(.,'Choose Language')]")
        self.language_indonesia_option = (By.XPATH, "//div[@data-value='indonesia']")
        self.street_address_input = (By.XPATH, "//input[@placeholder='Input Address']")
        self.country_dropdown = (By.XPATH, "//button[contains(.,'Choose Country')]")
        self.country_indonesia_option = (By.XPATH, "//div[@data-value='id']")
        self.province_dropdown = (By.XPATH, "//button[contains(.,'Choose Province')]")
        self.province_jawa_tengah_option = (By.XPATH, "//span[normalize-space(text())='JAWA TENGAH']")
        self.city_dropdown = (By.XPATH, "//button[contains(.,'Choose City')]")
        self.city_surakarta_option = (By.XPATH, "//span[normalize-space(text())='KOTA SURAKARTA']")
        self.district_dropdown = (By.XPATH, "//button[contains(.,'Choose District')]")
        self.district_laweyan_option = (By.XPATH, "//div[@data-value='v337201']")
        self.subdistrict_dropdown = (By.XPATH, "//button[contains(.,'Choose Sub District')]")
        self.subdistrict_laweyan_option = (By.XPATH, "//div[@data-value='laweyan']")
        self.next_button = (By.XPATH, "//button[normalize-space(text())='Next']")
        self.fill_address_same_as_company_record_button = (By.XPATH, "//button[normalize-space(text())='Fill in with the same data from the Company records']")
        self.aggree_terms_checkbox = (By.ID, "select-all")
        self.register_company_button = (By.XPATH, "//button[normalize-space(text())='Register']")
        self.success_toast = (By.XPATH, "//*[contains(text(),'Success Register Company')]")
        self.error_wrong_email_format = (By.XPATH, "//span[normalize-space(text())='Please provide a valid email address']")

    def navigate_to_company_page(self):
        WebDriverWait(self.driver, 20).until( EC.visibility_of_element_located(self.company_hyperlink))
        self.driver.find_element(*self.company_hyperlink).click()

    def click_add_company(self):
        self.driver.find_element(*self.add_company_button).click()

    def input_company_name(self, company_name):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.company_name_input))
        self.driver.find_element(*self.company_name_input).send_keys(company_name)
    
    def input_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def input_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)

    def select_industry(self):
        self.driver.find_element(*self.industry_dropdown).click()
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.industry_automative_option))
        self.driver.find_element(*self.industry_automative_option).click()
    
    def select_company_type(self):
        self.driver.find_element(*self.company_type_dropdown).click()
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.company_type_private_option))
        self.driver.find_element(*self.company_type_private_option).click() 

    def select_language(self):
        self.driver.find_element(*self.language_dropdown).click()
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.language_indonesia_option))
        self.driver.find_element(*self.language_indonesia_option).click()
    
    def input_street_address(self, street_address):
        self.driver.find_element(*self.street_address_input).send_keys(street_address)  

    def select_country(self):
        self.driver.find_element(*self.country_dropdown).click()
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.country_indonesia_option))
        self.driver.find_element(*self.country_indonesia_option).click()

    def select_province(self):
        self.driver.find_element(*self.province_dropdown).click()
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.province_jawa_tengah_option))
        self.driver.find_element(*self.province_jawa_tengah_option).click()

    def select_city(self):
        self.driver.find_element(*self.city_dropdown).click()
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.city_surakarta_option))
        self.driver.find_element(*self.city_surakarta_option).click()

    def select_district(self):
        WebDriverWait(self.driver, 30).until( EC.visibility_of_element_located(self.district_dropdown))
        self.driver.find_element(*self.district_dropdown).click()
        WebDriverWait(self.driver, 30).until( EC.visibility_of_element_located(self.district_laweyan_option))
        self.driver.find_element(*self.district_laweyan_option).click()

    def select_subdistrict(self):
        WebDriverWait(self.driver, 10).until( EC.presence_of_element_located(self.subdistrict_dropdown))
        # self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", self.subdistrict_dropdown)
        self.driver.find_element(*self.subdistrict_dropdown).click()
        WebDriverWait(self.driver, 60).until( EC.visibility_of_element_located(self.subdistrict_laweyan_option))
        self.driver.find_element(*self.subdistrict_laweyan_option).click()

    def click_next(self):
        self.driver.find_element(*self.next_button).click() 

    def click_fill_address_same_as_company_record(self):
        try:
            WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.fill_address_same_as_company_record_button))
            self.driver.find_element(*self.fill_address_same_as_company_record_button).click()
        except TimeoutException:
            pass  

    def agree_terms(self):
        self.driver.find_element(*self.aggree_terms_checkbox).click()

    def click_register_company(self):
        self.driver.find_element(*self.register_company_button).click()

    def assert_company_registered(self):
        toast = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_toast))
        return toast.text
    
    def assert_next_button_disabled(self):
        button = self.driver.find_element(*self.next_button)
        return button.get_attribute("disabled") is not None
    
    def assert_error_wrong_email_format(self):
            error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_wrong_email_format))
            return error_message.text
        

    