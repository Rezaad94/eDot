from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.use_email_username_button = (By.XPATH, "//button[normalize-space(text())='Use Email or Username']")
        self.username_input = (By.NAME, "username")
        self.login_button = (By.XPATH, "//button[normalize-space(text())='Log In']")
        self.password_input = (By.NAME, "password")
        self.error_message = (By.ID, "errorMessage")
        self.home_element = (By.XPATH, "//a[normalize-space(text())='Home']")
        self.invalid_password_message = (By.XPATH, "//p[normalize-space(text())='Incorrect password']")
        self.invalid_username_message = (By.XPATH, "//p[normalize-space(text())='Username Not Registered']")
        self.invalid_email_message = (By.XPATH, "//p[normalize-space(text())='Email Not Registered']")
        self.invalid_email_format_message = (By.XPATH, "//p[normalize-space(text())='Wrong email format']")
        self.see_password_button = (By.XPATH, "//div[contains(@class,'absolute right-[12px]')]//img[1]")

    def load(self, url):
        self.driver.get(url)

    def click_use_email_username(self):
        self.driver.find_element(*self.use_email_username_button).click()

    def input_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def input_password(self, password):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.password_input))
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_Login(self):
        self.driver.find_element(*self.login_button).click()
    
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
    
    def assert_home_element(self):
        return self.driver.find_element(*self.home_element).text
    
    def assert_invalid_password_message(self):
        return self.driver.find_element(*self.invalid_password_message).text
    
    def assert_invalid_username_message(self):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.invalid_username_message))
        return self.driver.find_element(*self.invalid_username_message).text
    
    def assert_invalid_email_message(self):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.invalid_email_message))
        return self.driver.find_element(*self.invalid_email_message).text
    
    def assert_invalid_email_format_message(self):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(self.invalid_email_format_message ))
        return self.driver.find_element(*self.invalid_email_format_message ).text
    
    def assert_login_button_disabled(self):
        button = self.driver.find_element(*self.login_button)
        return button.get_attribute("disabled") is not None
    
    def click_see_password(self):
        self.driver.find_element(*self.see_password_button).click()

    def assert_see_password_button(self):
        text_input = self.driver.find_element(*self.password_input).get_attribute("value")
        return text_input
    
    def do_valid_login(self, url, username, password):
        self.load(url)
        self.click_use_email_username()
        self.input_username(username)
        self.click_Login()
        self.input_password(password)
        self.click_Login()
