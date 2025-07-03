from web_pages.eSuite_login_page import LoginPage
from fixtures.web_driver import driver
from fixtures.web_config import (
    url,
    valid_username,
    valid_password,
    invalid_username,
    invalid_email,
    wrong_email_format,
    invalid_password
)

def test_eSuite_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.do_valid_login(url, valid_username, valid_password)
    assert "Home" == login_page.assert_home_element(), "Home page did not load after valid login"

def test_eSuite_login_with_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username(valid_username)
    login_page.click_Login()
    login_page.input_password(invalid_password)
    login_page.click_Login()
    assert "Incorrect password" == login_page.assert_invalid_password_message(), "Incorrect password message not displayed"

def test_eSuite_login_with_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username(invalid_username)
    login_page.click_Login()
    assert "Username Not Registered" == login_page.assert_invalid_username_message(), "Username Not Registered message not displayed"

def test_eSuite_login_with_invalid_email(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username(invalid_email)
    login_page.click_Login()
    assert "Email Not Registered" == login_page.assert_invalid_email_message(), "Email Not Registered message not displayed"

def test_eSuite_login_with_wrong_email_format(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username(wrong_email_format)
    assert "Wrong email format" == login_page.assert_invalid_email_format_message(), "Wrong email format message not displayed"

def test_eSuite_login_with_empty_username_or_email(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username("")
    assert login_page.assert_login_button_disabled() is True, "Login button should be disabled with empty username"

def test_eSuite_login_with_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username(valid_username)
    login_page.click_Login()
    login_page.input_password("")
    assert login_page.assert_login_button_disabled() is True, "Login button should be disabled with empty password"

def test_see_input_password(driver):
    login_page = LoginPage(driver)
    login_page.load(url)
    login_page.click_use_email_username()
    login_page.input_username(valid_username)
    login_page.click_Login()
    login_page.input_password(valid_password)
    login_page.click_see_password()
    assert login_page.assert_see_password_button() == valid_password, "Password text input does not match"
