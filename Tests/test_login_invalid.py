import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
import time
from selenium.webdriver.chrome.options import Options
# @pytest.mark.parametrize("username, password,",[("admin","Admin1234"),("adminn","Admin123"),("",""),("admin",""),("","Admin1234")])
@pytest.mark.wrongcredential
def test_invalid_login_with_wrong_password(driver,username,password):
    login_page=LoginPage(driver)
    login_page.enter_username(username)

    login_page.enter_password(password)
    loc='Outpatient Clinic'

    login_page.select_location(loc)

    login_page.click_on_login_button()
    time.sleep(5)

    expected_page="Login"
    actual=driver.title
    assert expected_page==actual
    expected_msg = "Invalid username/password. Please try again."
    error = driver.find_element(By.ID, 'error-message').text
    assert expected_msg.__contains__(error)

#
# @pytest.mark.wrongcredential
#
# def test_invalid_login_with_wrong_username(driver):
#
#     driver.find_element(By.ID,'username').send_keys("adminn")
#     driver.find_element(By.ID,'password').send_keys("Admin123")
#     loc='Outpatient Clinic'
#     driver.find_element(By.ID,loc).click()
#     driver.find_element(By.ID,'loginButton').click()
#     expected_page="Login"
#     actual=driver.title
#     assert expected_page==actual
#     expected_msg = "Invalid username/password. Please try again."
#     error = driver.find_element(By.ID, 'error-message').text
#     assert expected_msg.__contains__(error)
#
# @pytest.mark.blankcase
# def test_invalid_login_with_blank_input(driver):
#
#     driver.find_element(By.ID,'username').send_keys("")
#     driver.find_element(By.ID,'password').send_keys("")
#     loc='Outpatient Clinic'
#     driver.find_element(By.ID,loc).click()
#     driver.find_element(By.ID,'loginButton').click()
#     expected_page="Login"
#     actual=driver.title
#     assert expected_page==actual
#     expected_msg = "Invalid username/password. Please try again."
#     error = driver.find_element(By.ID, 'error-message').text
#     assert expected_msg.__contains__(error)
#
# @pytest.mark.blankcase
# def test_invalid_login_with_blank_password(driver):
#
#     driver.find_element(By.ID,'username').send_keys("admin")
#     driver.find_element(By.ID,'password').send_keys("")
#     loc='Outpatient Clinic'
#     driver.find_element(By.ID,loc).click()
#     driver.find_element(By.ID,'loginButton').click()
#     expected_page="Login"
#     actual=driver.title
#     assert expected_page==actual
#     expected_msg = "Invalid username/password. Please try again."
#     error = driver.find_element(By.ID, 'error-message').text
#     assert expected_msg.__contains__(error)
#
# @pytest.mark.blankcase
# def test_invalid_login_with_blank_username(driver):
#
#
#
#     driver.find_element(By.ID,'username').send_keys("")
#     driver.find_element(By.ID,'password').send_keys("Admin1234")
#     loc='Outpatient Clinic'
#     driver.find_element(By.ID,loc).click()
#     driver.find_element(By.ID,'loginButton').click()
#     expected_page="Login"
#     actual=driver.title
#     assert expected_page==actual
#     expected_msg = "Invalid username/password. Please try again."
#     error = driver.find_element(By.ID, 'error-message').text
#     assert expected_msg.__contains__(error)


