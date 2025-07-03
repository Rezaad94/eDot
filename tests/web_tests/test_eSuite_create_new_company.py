from web_pages.eSuite_login_page import LoginPage
from web_pages.eSuite_create_new_company_page import CreateNewCompanyPage
from web_pages.eSuite_detail_company_page import CompanyDetailPage
from fixtures.web_driver import driver
from fixtures.web_config import (
    url,
    company_name,
    valid_email,
    phone_number,
    street_address,
    valid_username,
    valid_password,
    country,
    province,
    city,
    district,
    sub_district,
    industry_type,
    company_type,
    language,
    wrong_email_format
)

def test_create_company_with_valid_data(driver):
    login_page = LoginPage(driver)
    login_page.do_valid_login(url, valid_username, valid_password)
    create_new_company = CreateNewCompanyPage(driver)
    create_new_company.navigate_to_company_page()
    create_new_company.click_add_company()
    create_new_company.input_company_name(company_name)
    create_new_company.input_email(valid_email)
    create_new_company.input_phone_number(phone_number)
    create_new_company.select_industry()
    create_new_company.select_company_type()
    create_new_company.select_language()
    create_new_company.select_country()
    create_new_company.input_street_address(street_address)
    create_new_company.select_province()
    create_new_company.select_city()
    create_new_company.select_district()
    create_new_company.select_subdistrict()
    create_new_company.click_next()
    create_new_company.click_next()
    create_new_company.click_fill_address_same_as_company_record()
    create_new_company.agree_terms()
    create_new_company.click_register_company()
    assert "Success Register Company" == create_new_company.assert_company_registered(), "Company registration did not succeed"

def test_create_company_with_empty_data(driver):
    login_page = LoginPage(driver)
    login_page.do_valid_login(url, valid_username, valid_password)
    create_new_company = CreateNewCompanyPage(driver)
    create_new_company.navigate_to_company_page()
    create_new_company.click_add_company()
    assert create_new_company.assert_next_button_disabled(), "Next button should be disabled with empty fields"

def test_create_company_with_wrong_email_format(driver):
    login_page = LoginPage(driver)
    login_page.do_valid_login(url, valid_username, valid_password)
    create_new_company = CreateNewCompanyPage(driver)
    create_new_company.navigate_to_company_page()
    create_new_company.click_add_company()
    create_new_company.input_company_name(company_name)
    create_new_company.input_email(wrong_email_format)
    create_new_company.input_phone_number(phone_number)
    create_new_company.select_industry()
    create_new_company.select_company_type()
    create_new_company.select_language()
    create_new_company.select_country()
    create_new_company.input_street_address(street_address)
    create_new_company.select_province()
    create_new_company.select_city()
    create_new_company.select_district()
    create_new_company.select_subdistrict()
    create_new_company.click_next()
    assert "Please provide a valid email address" in create_new_company.assert_error_wrong_email_format(), "Error message for invalid email format not displayed"

def test_Make_sure_data_company_created_same_with_data_inputed_when_fill_the_form(driver):
    login_page = LoginPage(driver)
    login_page.do_valid_login(url, valid_username, valid_password)
    create_new_company = CreateNewCompanyPage(driver)
    create_new_company.navigate_to_company_page()
    company_detail_page = CompanyDetailPage(driver)
    company_detail_page.open_company_detail()
    company_detail_page.get_company_id()
    assert company_detail_page.get_company_name() == company_name, "Company name does not match"
    assert company_detail_page.get_company_email() == valid_email, "Company email does not match"
    assert company_detail_page.get_company_phone() == phone_number, "Company phone number does not match"
    assert company_detail_page.get_company_address() == street_address, "Company address does not match"
    assert company_detail_page.get_company_industry_type() == industry_type, "Company industry type does not match"
    assert company_detail_page.get_company_type() == company_type, "Company type does not match"
    assert company_detail_page.get_company_country() == country, "Company country does not match"
    assert company_detail_page.get_company_province() == province, "Company province does not match"
    assert company_detail_page.get_company_city() == city, "Company city does not match"
    assert company_detail_page.get_company_district() == district, "Company district does not match"

