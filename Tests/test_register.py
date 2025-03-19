import time

import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.Registrationpage import RegistrationPage


@pytest.mark.usefixtures("login")
def test_verify_registration_page_title(login):
    driver = login
    # Navigate to Registration Page from HomePage
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(option_language="Spanish"), "Register a patient option NOT found!"
    # Now verify Registration Page title
    registration_pg = RegistrationPage(driver)
    # registration_pg.verify_registration_page()
    assert registration_pg.is_on_registration_page(), "Registration page title is not displayed"


@pytest.mark.usefixtures("login")
def test_enter_name(login):
    driver = login
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(option_language="Spanish"), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    # assert registration_pg.is_on_registration_page(), "Not on Registration Page!"
    time.sleep(5)
    registration_pg.enter_name("Priya")


@pytest.mark.usefixtures("login")
def test_family_name(login):
    driver = login
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(option_language="Spanish"), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    # assert registration_pg.is_on_registration_page(), "Not on Registration Page!"
    time.sleep(5)

    registration_pg.enter_family_name("Nikhar Pal")


@pytest.mark.usefixtures("login")
def test_click_on_next(login):
    driver = login
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(option_language="Spanish"), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    # assert registration_pg.is_on_registration_page(), "Not on Registration Page!"
    time.sleep(5)
    registration_pg.click_on_next_button()


@pytest.mark.usefixtures("login")
def test_select_gender_and_click_on_next(login):
    driver = login
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(option_language="Spanish"), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    registration_pg.enter_name("Priya")
    registration_pg.enter_family_name("Nikhar Pal")
    registration_pg.click_on_next_button()
    registration_pg.select_gender()
    registration_pg.click_on_next_button()
    time.sleep(5)
    registration_pg=RegistrationPage(driver)
    registration_pg.select_dof()
    registration_pg.click_on_next_button()

@pytest.mark.usefixtures("login")

def test_contact_info_address(login):
    driver=login
    home_page=HomePage(driver)
    assert home_page.list_of_all_options(),"Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    registration_pg.enter_name("Priya")
    registration_pg.enter_family_name("Nikhar Pal")
    registration_pg.click_on_next_button()
    registration_pg.select_gender()
    registration_pg.click_on_next_button()
    time.sleep(5)
    registration_pg = RegistrationPage(driver)
    registration_pg.select_dof()
    registration_pg.click_on_next_button()
    registration_pg=RegistrationPage(driver)
    time.sleep(5)
    registration_pg.patent_address("padmaksh balaji lane,pashan","jai bhavani nagar","Pune","maharashtra","India","452001")
    registration_pg.click_on_next_button()

@pytest.mark.usefixtures("login")
def test_contact_phone_no(login):
    driver = login
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    registration_pg.enter_name("Priya")
    registration_pg.enter_family_name("Nikhar Pal")
    registration_pg.click_on_next_button()
    registration_pg.select_gender()
    registration_pg.click_on_next_button()
    time.sleep(5)
    registration_pg = RegistrationPage(driver)
    registration_pg.select_dof()
    registration_pg.click_on_next_button()
    registration_pg = RegistrationPage(driver)
    time.sleep(5)
    registration_pg.patent_address("padmaksh balaji lane,pashan", "jai bhavani nagar", "Pune", "maharashtra", "India",
                                   "452001")
    registration_pg.click_on_next_button()
    registration_pg = RegistrationPage(driver)
    time.sleep(5)
    registration_pg.contact_phone_number("468990098")
    registration_pg.click_on_next_button()
    time.sleep(5)


@pytest.mark.usefixtures("login")
def test_relationship_relative(login):
    driver = login
    home_page = HomePage(driver)
    assert home_page.list_of_all_options(option_language="Spanish"), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    registration_pg.enter_name("Priya")
    registration_pg.enter_family_name("Nikhar Pal")
    registration_pg.click_on_next_button()
    registration_pg.select_gender()
    registration_pg.click_on_next_button()
    time.sleep(5)
    registration_pg = RegistrationPage(driver)
    registration_pg.select_dof()
    registration_pg.click_on_next_button()
    registration_pg = RegistrationPage(driver)
    time.sleep(5)
    registration_pg.patent_address("padmaksh balaji lane,pashan", "jai bhavani nagar", "Pune", "maharashtra", "India",
                                   "452001")
    registration_pg.click_on_next_button()
    time.sleep(5)
    registration_pg = RegistrationPage(driver)
    registration_pg.contact_phone_number("468990098")
    registration_pg.click_on_next_button()
    time.sleep(5)
    # registration_pg = RegistrationPage(driver)
    # registration_pg.relationship_relative()
    registration_pg.relationship_relative("xyz")
    time.sleep(5)
    registration_pg.click_on_next_button()
    time.sleep(5)


@pytest.mark.usefixtures("login")
def test_confirmation(login):
    driver = login
    home_page = HomePage(driver)
    time.sleep(10)
    assert home_page.list_of_all_options(option_language="english"), "Register a patient option NOT found!"
    registration_pg = RegistrationPage(driver)
    first_name = "Priya"
    last_name = "Nikhar Pal"

    registration_pg.enter_name(first_name)
    registration_pg.enter_family_name(last_name)
    registration_pg.click_on_next_button()
    registration_pg.select_gender()
    registration_pg.click_on_next_button()
    time.sleep(5)
    # registration_pg = RegistrationPage(driver)
    registration_pg.select_dof()
    registration_pg.click_on_next_button()
    # registration_pg = RegistrationPage(driver)
    # time.sleep(5)
    # registration_pg.patent_address("padmaksh balaji lane,pashan", "jai bhavani nagar", "Pune", "maharashtra", "India",
    #                                "452001")
    # registration_pg.click_on_next_button()
    # time.sleep(5)
    # # registration_pg = RegistrationPage(driver)
    # registration_pg.contact_phone_number("468990098")
    # registration_pg.click_on_next_button()
    # time.sleep(5)
    # # registration_pg = RegistrationPage(driver)
    # # registration_pg.relationship_relative()
    # registration_pg.relationship_relative("xyz")
    # time.sleep(5)
    # registration_pg.click_on_next_button()
    # time.sleep(10)
    # # registration_pg = RegistrationPage(driver)
    registration_pg.confirmation()
    # assert registration_pg.entered_data
    time.sleep(10)






