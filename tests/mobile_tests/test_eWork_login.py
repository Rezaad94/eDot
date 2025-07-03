from mobile_pages.eWork_login_page import LoginPage
from fixtures.mobile_driver import mobile_driver
from fixtures.mobile_config import (
    valid_company_id,
    invalid_company_id,
    valid_username,
    valid_password,
    invalid_username,
    invalid_password
)

def test_eWork_login_with_valid_data(mobile_driver):
    login_page = LoginPage(mobile_driver)
    login_page.input_company_id(valid_company_id)
    login_page.input_username(valid_username)
    login_page.input_password(valid_password)
    login_page.click_login()
    # login_page.allow_location()
    assert login_page.assert_home_page_loaded(), "Home page did not load after valid login"

def test_login_with_empty_field(mobile_driver):
    login_page = LoginPage(mobile_driver)
    login_page.input_company_id("")
    login_page.input_username("")
    login_page.input_password("")
    login_page.click_login()
    assert login_page.assert_login_button_disabled(), "Login button should be disabled with empty fields"

def test_login_with_invalid_company_id(mobile_driver):
    login_page = LoginPage(mobile_driver)
    login_page.input_company_id(invalid_company_id)
    login_page.input_username(valid_username)
    login_page.input_password(valid_password)
    login_page.click_login()
    assert "Failed to login. Please contact Sales Admin." in login_page.get_error_message(), "Error message not displayed for invalid company ID"

def test_login_with_invalid_username(mobile_driver):
    login_page = LoginPage(mobile_driver)
    login_page.input_company_id(valid_company_id)
    login_page.input_username(invalid_username)
    login_page.input_password(valid_password)
    login_page.click_login()
    assert "Failed to login. Please contact Sales Admin." in login_page.get_error_message(), "Error message not displayed for invalid username"

def test_login_with_invalid_password(mobile_driver):
    login_page = LoginPage(mobile_driver)
    login_page.input_company_id(valid_company_id)
    login_page.input_username(valid_username)
    login_page.input_password(invalid_password)
    login_page.click_login()
    assert "Failed to login. Please contact Sales Admin." in login_page.get_error_message(), "Error message not displayed for invalid password"

def test_see_password_functionality(mobile_driver):
    login_page = LoginPage(mobile_driver)
    login_page.input_company_id(valid_company_id)
    login_page.input_username(valid_username)
    login_page.input_password(valid_password)
    login_page.click_see_password()
    text_input, content_desc_value = login_page.assert_password_visible()
    assert text_input == valid_password, "Password text input does not match"
    assert content_desc_value, "See password button did not change to 'Hide password' after clicking"