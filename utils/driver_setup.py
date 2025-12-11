# utils/driver_setup.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Headless opcional controlado por variable de entorno
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1366,768")

    # Flags recomendados para CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Configurar timeouts básicos
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)

    return driver

def quit_driver(driver):
    """Cierra el driver de forma segura."""
    try:
        driver.quit()
    except Exception:
        pass
