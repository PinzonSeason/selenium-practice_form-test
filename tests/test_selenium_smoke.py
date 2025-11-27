from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_demoqa(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(driver, 15)
    wrapper = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "practice-form-wrapper")))
    assert "practice form" in wrapper.text.lower() or "automation-practice-form" in driver.current_url
