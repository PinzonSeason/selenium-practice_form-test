from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_visible(driver, locator, timeout=10):
    """Espera hasta que el elemento indicado por locator sea visible."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_clickable(driver, locator, timeout=10):
    """Espera a que el elemento sea clickeable."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_for_presence(driver, locator, timeout=10):
    """Espera a que el elemento esté presente en el DOM (no necesariamente visible)."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def wait_until_invisible(driver, locator, timeout=10):
    """Espera hasta que un elemento desaparezca (invisible o no presente)."""
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )
