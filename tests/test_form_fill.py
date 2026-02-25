# tests/test_form_fill.py
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.data_factory import user_data
from utils.wait_helpers import wait_for_visible

def test_fill_form_extended(driver):
    data = user_data()
    driver.get("https://demoqa.com/automation-practice-form")

    # Quitar banners que interceptan clicks
    driver.execute_script("""
        try { document.querySelector('#fixedban')?.remove(); } catch(e) {}
        try { document.querySelector('footer')?.remove(); } catch(e) {}
    """)

    wait_for_visible(driver, (By.CLASS_NAME, "practice-form-wrapper"), timeout=15)

    # Datos básicos
    first_name_input = driver.find_element(By.ID, "firstName")
    first_name_input.send_keys(data["first_name"])
    assert first_name_input.get_attribute("value") == data["first_name"]

    last_name_input = driver.find_element(By.ID, "lastName")
    last_name_input.send_keys(data["last_name"])
    assert last_name_input.get_attribute("value") == data["last_name"]

    email_input = driver.find_element(By.ID, "userEmail")
    email_input.send_keys(data["email"])
    assert email_input.get_attribute("value") == data["email"]

    # Gender
    gender_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)
    driver.execute_script("arguments[0].click();", gender_label)
    male_radio = driver.find_element(By.ID, "gender-radio-1")
    assert male_radio.is_selected()

    # Teléfono
    phone_input = driver.find_element(By.ID, "userNumber")
    phone_input.send_keys(data["phone"])
    phone_value = phone_input.get_attribute("value")
    assert len(phone_value) == 10
    assert phone_value.isdigit()

    # Date of Birth
    dob_input = driver.find_element(By.ID, "dateOfBirthInput")
    dob_value = dob_input.get_attribute("value")
    assert isinstance(dob_value, str) and len(dob_value) > 0

    # Subjects
    subjects_input = driver.find_element(By.ID, "subjectsInput")
    subjects_input.click()
    for subject in data["subjects"]:
        subjects_input.send_keys(subject)
        wait_for_visible(driver, (By.CSS_SELECTOR, ".subjects-auto-complete__menu"), timeout=10)
        option = driver.find_element(By.XPATH, f"//div//child::div[contains(text(),'{subject}')]")
        option.click()
        chip = driver.find_element(
            By.XPATH,
            f"//div[contains(@class,'subjects-auto-complete__multi-value__label') and normalize-space()='{subject}']"
        )
        assert chip.text == subject
    chips = driver.find_elements(By.CSS_SELECTOR, ".subjects-auto-complete__multi-value__label")
    assert len(chips) >= 1

    # Hobbies
    hobby_map = {"Sports": "hobbies-checkbox-1", "Reading": "hobbies-checkbox-2", "Music": "hobbies-checkbox-3"}
    for hobby in data["hobbies"]:
        hobby_element = driver.find_element(By.ID, hobby_map[hobby])
        driver.execute_script("arguments[0].scrollIntoView(true);", hobby_element)
        driver.execute_script("arguments[0].click();", hobby_element)
    selected_hobbies = driver.find_elements(By.CSS_SELECTOR, "input[id^='hobbies-checkbox-']:checked")
    assert len(selected_hobbies) >= 1

    # Picture
    upload_input = driver.find_element(By.ID, "uploadPicture")
    upload_input.send_keys(data["picture"])
    assert "love_bug.jpg" in upload_input.get_attribute("value")

    # Address
    address_input = driver.find_element(By.ID, "currentAddress")
    address_input.send_keys(data["current_address"])
    assert address_input.get_attribute("value") == data["current_address"]

    # State
    state_dropdown = driver.find_element(By.ID, "state")
    state_dropdown.click()
    driver.find_element(By.XPATH, data["state_xpath"]).click()

    state_chip = driver.find_element(
        By.XPATH,
        "//div[@id='state']//div[contains(@class,'singleValue')]"
    )
    assert state_chip.text == data["state"]

    # City
    city_dropdown = driver.find_element(By.ID, "city")
    city_dropdown.click()
    driver.find_element(By.XPATH, data["city_xpath"]).click()

    city_chip = driver.find_element(
        By.XPATH,
        "//div[@id='city']//div[contains(@class,'singleValue')]"
    )
    assert city_chip.text == data["city"]
