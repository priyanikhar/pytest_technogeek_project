import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
@pytest.fixture
def driver():
    # chr_option = Options()
    # chr_option.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(chr_option)

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")  # Bypass sandbox issue
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes due to memory limits
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (helps in some cases)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://o2.openmrs.org/openmrs/login.htm")
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture
def login(driver):
    driver.get("https://o2.openmrs.org/openmrs/login.htm")  # Open login page
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("Admin123")
    loc = 'Outpatient Clinic'
    driver.find_element(By.XPATH,f"//ul[@id='sessionLocation']//li[text()='{loc}']").click()
    driver.find_element(By.ID, "loginButton").click()
    return driver



