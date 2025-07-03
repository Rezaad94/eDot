from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.company_id_input = (AppiumBy.ID, "id.edot.ework.debug:id/tv_company_id")
        self.username_input = (AppiumBy.ID, "id.edot.ework.debug:id/tv_username")
        self.password_input = (AppiumBy.ID, "id.edot.ework.debug:id/tv_password")
        self.login_button = (AppiumBy.ID, "id.edot.ework.debug:id/button_text")
        self.see_password_button = (AppiumBy.ID, "id.edot.ework.debug:id/text_input_end_icon")
        self.error_message = (AppiumBy.ID, "id.edot.ework.debug:id/textView") # text: Failed to login. Please contact Sales Admin.
        self.no_save_password_button = (AppiumBy.ID, "android:id/autofill_save_no")
        self.allow_location_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        self.home_relative_contenct = (AppiumBy.ID, "id.edot.ework.debug:id/relative_content")

    def input_company_id(self, company_id):
        self.driver.find_element(*self.company_id_input).send_keys(company_id)

    def input_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_see_password(self):
        self.driver.find_element(*self.see_password_button).click()

    def assert_password_visible(self):
        see_password_button = self.driver.find_element(*self.see_password_button)
        text_input = self.driver.find_element(*self.password_input).text
        content_desc_value = see_password_button.get_attribute("checked") == "true"
        return text_input, content_desc_value
    
    def assert_login_button_disabled(self):
        login_button = self.driver.find_element(*self.login_button)
        return not login_button.is_enabled()

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message))
        return self.driver.find_element(*self.error_message).text
    
    def click_no_save_password(self):
        self.driver.find_element(*self.no_save_password_button).click()

    def click_allow_location(self):
        self.driver.find_element(*self.allow_location_button).click()

    def assert_home_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home_relative_contenct))
        return self.driver.find_element(*self.home_relative_contenct).is_displayed()

    def allow_location(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_elements_located(self.allow_location_button))
        self.driver.find_element(*self.allow_location_button).click()
