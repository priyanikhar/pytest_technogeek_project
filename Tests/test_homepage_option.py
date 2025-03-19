from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
import time
def test_all_home_page_option(login):
    driver = login
    home_page=HomePage(driver)
    home_page.list_of_all_options(option_language="english")
    time.sleep(10)

#option_language="Spanish"

def test_page_navigation(login):
    driver=login
    home_page=HomePage(driver)
    home_page.pagenavigation_registration_Home()

def test_click_on_find_patient(login):
    driver = login
    home_page = HomePage(driver)
    home_page.click_on_patient_record()

