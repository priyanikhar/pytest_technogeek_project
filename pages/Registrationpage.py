from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class RegistrationPage():


    def __init__(self, driver):
        self.driver = driver
        self.entered_data = {}

    def is_on_registration_page(self):
            """Verifies user is on the Registration Page by checking the heading text."""
            try:
                page_heading = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Register a patient')or contains(text(), 'Registrar un paciente')]"))
                )
                return page_heading.is_displayed()
            except:
                return False

#     def verify_registration_page(self):
#         """Verifies user is on the Registration Page by checking the heading text."""
#
#         page_heading = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Register a patient')]")))
#         return page_heading.is_displayed()
# #
    def enter_name(self,name):
        self.driver.find_element(By.XPATH,'//input[@name="givenName"]').send_keys(name)
        self.entered_data["name"]=name
        print(self.entered_data)


    def enter_family_name(self,family_name):
        self.driver.find_element(By.XPATH,'//input[@name="familyName"]').send_keys(family_name)
        self.entered_data["family_name"]=family_name
        print(self.entered_data)

    def click_on_next_button(self):
        self.driver.find_element(By.ID,'next-button').click()


    def select_gender(self,gender="Female"):
        gender_sel=Select(self.driver.find_element(By.ID,'gender-field'))
        gender_sel.select_by_visible_text(gender)
        # self.entered_data["gender"]=gender


    def select_dof(self):

        wait=WebDriverWait(self.driver,10)
        birth_day = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//label[@for="birthdateDay-field"]/following-sibling::input')))
        birth_day.send_keys("19")
        # self.entered_data["birth_day"]="19"

        # Select Birth Month
        month = Select(self.driver.find_element(By.XPATH, '//select[@id="birthdateMonth-field"]'))
        month.select_by_index(5)
        # self.entered_data["birth_month"] = "May"


        # Wait and enter Birth Year
        year = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//label[@for="birthdateYear-field"]/following-sibling::input[@type="text"]')))
        year.send_keys("1995")
        # self.entered_data["birth_year"] = "1995"


    def patent_address(self, address1, address2, cityy, statee,countryy,postal_code):
        adr1=self.driver.find_element(By.XPATH,'//input[@id="address1"]')
        adr1.send_keys(address1)
        # self.entered_data["adr1"]=address1
        adr2=self.driver.find_element(By.XPATH,'//input[@id="address2"]')
        adr2.send_keys(address2)
        # self.entered_data["adr2"]=address2
        city=self.driver.find_element(By.XPATH,"//label[@name='cityVillage']/following-sibling::input")
        city.send_keys(cityy)
        # self.entered_data["city"]=cityy
        state=self.driver.find_element(By.XPATH,"//label[@name='stateProvince']/following-sibling::input")
        state.send_keys(statee)
        # self.entered_data["state"]=statee
        country=self.driver.find_element(By.XPATH,"//label[@name='country']/following-sibling::input")
        country.send_keys(countryy)
        # self.entered_data["country"]=countryy
        post_code=self.driver.find_element(By.XPATH,"//label[@name='postalCode']/following-sibling::input")
        post_code.send_keys(postal_code)
        # self.entered_data["post_code"]=postal_code

    def contact_phone_number(self,phone_no):
        ph_no=self.driver.find_element(By.XPATH,'//input[@class="phone"]')
        ph_no.send_keys(phone_no)
        # self.entered_data["ph_no"]=phone_no

    def relationship_relative(self,p_name):

        wait = WebDriverWait(self.driver, 10)
        relation_type = Select(wait.until(EC.visibility_of_element_located((By.ID, 'relationship_type'))))

        relation_type.select_by_index(1)
        # self.entered_data["relation_type"]="Doctor"
        person_name=self.driver.find_element(By.XPATH,'//input[@type="text" and @placeholder="Person Name"]')
        person_name.send_keys(p_name)
        # self.entered_data["person_name"]=p_name

    def confirmation(self):
        # namee=self.driver.find_element(By.XPATH,"//div[@id='dataCanvas']/div/p/span[contains(text(), 'Name: ')]").text
        # gender=self.driver.find_element(By.XPATH,"//div[@id='dataCanvas']/div/p/span[contains(text(), 'Gender: ')]").text
        # DOB=self.driver.find_element(By.XPATH,"//div[@id='dataCanva']/div/p/span[contains(text(), 'Birthdate: ')]").text
        # Addr=self.driver.find_element(By.XPATH,'//div[@id="dataCanvas]/div/p/span[contains(text(), "Address: ")]').text
        # pnumber=self.driver.find_element(By.XPATH,'//div[@id="dataCanvas"]/div/p/span[contains(text()," Phone Number: ")]').text
        # relative=self.driver.find_element(By.XPATH,'//div[@id="dataCanvas"]/div/p/span[contains(text(), "Relatives: ")]').text

        # namee_element = self.driver.find_element(By.XPATH,      "//div[@id='dataCanvas']//p/span[contains(text(), 'Name:')]")
        # namee = namee_element.get_attribute("textContent").strip()
        #
        # # Removing the label "Name: " from the extracted text
        # namee = namee.replace("Name:", "").strip()
        #
        # # Handling case where first and last name are separated by a comma
        # namee_split = namee.split(',')
        # if len(namee_split) == 2:
        #     namee = namee_split[0].strip() + " " + namee_split[1].strip()  # Combining names properly
        #
        # # Extract gender
        # gender_element = self.driver.find_element(By.XPATH, "//div[@id='dataCanvas']/div/p/span[contains(text(), 'Gender: ')]")
        # gender = gender_element.get_attribute("textContent").strip().replace("Gender:", "").strip()
        #
        # # Construct the expected full name from entered data
        # expected_full_name = f"{self.entered_data.get('name', '').strip()} {self.entered_data.get('family_name', '').strip()}"
        #
        # # Assertions
        # # assert namee == expected_full_name, f"Expected '{expected_full_name}', but got '{namee}'"
        # print(f"Entered Data: {self.entered_data}")
        #
        # assert namee == expected_full_name, f"Expected '{expected_full_name}', but got '{namee}'"
        #
        # assert gender == self.entered_data.get("gender",""), f"Expected '{self.entered_data.get('gender', '')}', but got '{gender}'"
        confirm=self.driver.find_element(By.ID,'submit')
        confirm.click()
        wait = WebDriverWait(self.driver, 10)
        Navigate_back_home = wait.until(EC.element_to_be_clickable((By.XPATH, '//ul[@id="breadcrumbs"]/li')))
        Navigate_back_home.click()













