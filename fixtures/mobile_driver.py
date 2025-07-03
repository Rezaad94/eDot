import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def mobile_driver():
    # desired_caps = {
    #     "platformName": "Android",
    #     "deviceName": "emulator-5554",
    #     "appPackage": "id.edot.ework.debug",
    #     "appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
    #     "automationName": "UiAutomator2",
    #     "autoGrantPermissions": True
    # }
    # driver = webdriver.Remote("http://localhost:4723", desired_caps)

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "id.edot.ework.debug"
    options.app_activity = "id.edot.onboarding.ui.splash.SplashScreenActivity"
    options.automation_name = "UiAutomator2"
    options.auto_grant_permissions = True
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
