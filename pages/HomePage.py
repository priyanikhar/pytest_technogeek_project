from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/div[@id="apps"]//a')))
        # return self.driver.find_element(By.XPATH,'/div[@id="apps"]//a')

    # def list_of_all_options(self,option_language):
        # """
        #       Clicks on "Register a patient" regardless of the language (English/Spanish).
        # """
        # option_language = option_language.strip().lower()
        #
        # # Define option text based on language
        # # Define option text based on language
        # if option_language == "english":
        #     select_option = "Register a patient"
        # elif option_language == "spanish":
        #     select_option = "Registrar un paciente"
        # # select_option = "Register a patient" if option_language.lower() == "english" else "Registrar un paciente"
        #
        # wait = WebDriverWait(self.driver, 10)
        #
        # # Get all option elements
        # all_options = wait.until(
        #     EC.presence_of_all_elements_located((By.XPATH, '//div[@id="apps"]//a'))
        # )
        # # Print available options for debugging
        # print("Available options on page:")
        # for option in all_options:
        #     print(f"- {option.text.strip()}")
        #
        # for option in all_options:
        #     if option.text.strip().lower() == select_option:  # Strip whitespace for accuracy
        #         print(f"Found option: {option.text}")
        #
        #         # Scroll into view before clicking
        #         self.driver.execute_script("arguments[0].scrollIntoView();", option)
        #
        #         # Click the option
        #         option.click()
        #         return True  # Return success
        #
        # print("Option not found!")
        # return False  # Return failure

    def list_of_all_options(self, option_language):
            """
            Clicks on "Register a patient" regardless of the language (English/Spanish).
            """
            # Normalize the input language
            option_language = option_language.strip().lower()

            # Define the selection based on the language
            if option_language == "english":
                select_option = "Register a patient"
            elif option_language == "spanish":
                select_option = "Registrar un paciente"
            else:
                raise ValueError(f"Unsupported language '{option_language}'. Expected 'English' or 'Spanish'.")

            wait = WebDriverWait(self.driver, 10)

            # Get all option elements
            all_options = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@id="apps"]//a'))
            )

            print("Available options on page:")
            for option in all_options:
                print(f"- {option.text}")

            for option in all_options:
                if option.text.strip() == select_option:  # No unnecessary .lower()
                    print(f"Found option: {option.text}")

                    # Scroll into view before clicking
                    self.driver.execute_script("arguments[0].scrollIntoView();", option)

                    # Click the option
                    option.click()
                    return True  # Success

            print(f"Option '{select_option}' not found!")
            return False  # Failure

    def pagenavigation_registration_Home(self):
        page_header=self.driver.find_element(By.TAG_NAME,'h4').text
        print(page_header)

    def click_on_patient_record(self):
        fnd_patient=self.driver.find_element(By.XPATH,'//a//i[@class="icon-search"]')
        fnd_patient.click()

