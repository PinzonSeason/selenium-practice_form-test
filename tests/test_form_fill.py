# tests/test_form_fill.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.wait_helpers import wait_for_visible
from utils.data_factory import user_data
from datetime import datetime

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
        subjects_input.send_keys(subject[0])
        wait_for_visible(driver, (By.CSS_SELECTOR, ".subjects-auto-complete__menu"), timeout=10)
        option = driver.find_element(
            By.XPATH,
            f"//div[contains(@id,'react-select-2-option') and normalize-space()='{subject}']"
        )
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
    state_input = driver.find_element(By.ID, "react-select-3-input")
    state_input.send_keys(data["state"])
    state_input.send_keys(Keys.ENTER)
    state_chip = driver.find_element(By.CSS_SELECTOR, "#state .css-1uccc91-singleValue")
    assert state_chip.text == data["state"]

    # City
    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys(data["city"])
    city_input.send_keys(Keys.ENTER)
    city_chip = driver.find_element(By.CSS_SELECTOR, "#city .css-1uccc91-singleValue")
    assert city_chip.text == data["city"]

    # Enviar formulario
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)

    # Validar modal
    modal = wait_for_visible(driver, (By.CLASS_NAME, "modal-content"), timeout=15)
    assert "Thanks for submitting the form" in modal.text

    # Validaciones finales
    assert data["first_name"] in modal.text
    assert data["last_name"] in modal.text
    assert data["email"] in modal.text
    assert phone_value in modal.text

    # Fecha con formato del modal
    dob_parsed = datetime.strptime(dob_value, "%d %b %Y")
    dob_modal_format = dob_parsed.strftime("%d %B,%Y")
    assert dob_modal_format in modal.text

    for hobby in data["hobbies"]:
        assert hobby in modal.text
    assert "love_bug.jpg" in modal.text
    assert f"{data['state']} {data['city']}" in modal.text