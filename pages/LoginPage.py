from selenium.webdriver.common.by import By
class LoginPage():
        def __init__(self,driver):
         self.driver=driver

        def enter_username(self,username):
            self.driver.find_element(By.ID, 'username').send_keys(username)

        def enter_password(self,password):
            self.driver.find_element(By.ID, 'password').send_keys(password)


        def select_location(self,location):

           self.driver.find_element(By.ID, location).click()

        def click_on_login_button(self):
           self.driver.find_element(By.ID, 'loginButton').click()