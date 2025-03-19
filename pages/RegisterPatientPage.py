from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.Registrationpage import RegistrationPage


class RegisterPatientPage():
    def __init__(self,driver):
        self.driver=driver
        # self.registration_pg = RegistrationPage(driver)

    def search_patient_by_name(self,patient_name):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="patient-search"]'))
        )
        # search_box=self.driver.find_element(By.XPATH,'//div[@id="apps"]/a/i[@class="icon-search"]')
        search_box.clear()
        search_box.send_keys(patient_name)
        search_box.send_keys(Keys.ENTER)
        # Wait for the search results table to load
        rows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@id="patient-search-results-table"]//tr/td[2]'))
        )

        # Extract names from the results
        patient_names = [row.text.lower().strip() for row in rows]
        print("Found patient names:", patient_names)  # Debugging

        # Assert that the expected patient name is found
        assert patient_name in patient_names, f"Patient '{patient_name}' not found in search results!"

        print("Assertion Passed: Patient found successfully!")





