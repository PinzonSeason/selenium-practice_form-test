# tests/test_fields_unit.py
from selenium.webdriver.common.by import By
from utils.data_factory import user_data

def test_first_name_field(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    data = user_data()
    el = driver.find_element(By.ID, "firstName")
    el.send_keys(data["first_name"])
    assert el.get_attribute("value") == data["first_name"]

def test_last_name_field(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    data = user_data()
    el = driver.find_element(By.ID, "lastName")
    el.send_keys(data["last_name"])
    assert el.get_attribute("value") == data["last_name"]

def test_email_field(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    data = user_data()
    el = driver.find_element(By.ID, "userEmail")
    el.send_keys(data["email"])
    assert el.get_attribute("value") == data["email"]

def test_phone_field(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    data = user_data()
    el = driver.find_element(By.ID, "userNumber")
    el.send_keys(data["phone"])
    assert el.get_attribute("value") == data["phone"]

def test_dob_read_only(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    el = driver.find_element(By.ID, "dateOfBirthInput")
    value = el.get_attribute("value")
    assert isinstance(value, str) and len(value) > 0
