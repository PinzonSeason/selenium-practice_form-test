import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Diccionario centralizado de selectores
selectors = {
    "first_name": (By.ID, "firstName"),
    "last_name": (By.ID, "lastName"),
    "email": (By.ID, "userEmail"),
    "phone": (By.ID, "userNumber"),
}

# Datos de prueba
def user_data():
    return {
        "first_name": "Eduardo",
        "last_name": "Reyna",
        "email": "eduardo.reyna@example.com",
        "phone": "8112345678"
    }

@pytest.mark.parametrize( "key", [
    "first_name",
    "last_name",
    "email",
    "phone",
])
def test_field_filling(driver, key):
    driver.get("https://demoqa.com/automation-practice-form")
    data = user_data()

    by, value = selectors[key]

    field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, value))
    )
    field.send_keys(data[key])

    assert field.get_attribute("value") == data[key]
