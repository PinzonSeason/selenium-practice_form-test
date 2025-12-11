# tests/test_fields_param.py
import pytest
from selenium.webdriver.common.by import By
from utils.data_factory import user_data

@pytest.mark.parametrize("field_id,key", [
    ("firstName", "first_name"),
    ("lastName", "last_name"),
    ("userEmail", "email"),
    ("userNumber", "phone"),
])
def test_field_filling(driver, field_id, key):
    driver.get("https://demoqa.com/automation-practice_form")
    data = user_data()

    field = driver.find_element(By.ID, field_id)
    field.send_keys(data[key])

    # Validación de que el input contiene lo que enviamos
    assert field.get_attribute("value") == data[key]
