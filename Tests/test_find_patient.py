import pytest

from pages.HomePage import HomePage
from pages.RegisterPatientPage import RegisterPatientPage


@pytest.mark.usefixtures("login")
def test_search_patient_by_name(login):
    driver = login
    home_page = HomePage(driver)
    registerPatientPg = RegisterPatientPage(driver)
    home_page.click_on_patient_record()
    registerPatientPg.search_patient_by_name("priya nikhar pal")