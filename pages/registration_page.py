# pages/registration_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def load(self):
        self.driver.get(self.url)

    def fill_first_name(self, name):
        self.driver.find_element(By.ID, "firstName").send_keys(name)

    def fill_last_name(self, last):
        self.driver.find_element(By.ID, "lastName").send_keys(last)

    def fill_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def select_gender(self):
        self.driver.find_element(By.XPATH, "//label[text()='Male']").click()

    def fill_mobile(self, number):
        self.driver.find_element(By.ID, "userNumber").send_keys(number)

    def submit_form(self):
        self.driver.find_element(By.ID, "submit").send_keys(Keys.ENTER)
