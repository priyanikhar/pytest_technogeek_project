import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from pages.LoginPage import LoginPage
from utils import ExcelUtils


# @pytest.mark.parametrize("username,password",[("admin","Admin123")])
@pytest.mark.parametrize("username,password,location",ExcelUtils.get_data_from_excel("ExcelFiles/openmrslogin.xlsx","valid_login"))

def test_valid_login(driver,username,password,location):

    login_page = LoginPage(driver)
    login_page.enter_username(username)

    login_page.enter_password(password)
    # loc = 'Outpatient Clinic'

    login_page.select_location(location)

    login_page.click_on_login_button()

    time.sleep(7)
    expected_page = "Home"
    actual = driver.title
    assert expected_page == actual


