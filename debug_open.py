import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
# Forzar visible por defecto; usa HEADLESS=1 o --headless para headless
if os.environ.get("HEADLESS", "") == "1":
    opts.add_argument("--headless=new")

opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--window-size=1366,768")

service = Service(ChromeDriverManager().install())
# service.log_path = "chromedriver.log"
driver = webdriver.Chrome(service=service, options=opts)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    print("current_url:", driver.current_url)

    # Espera hasta 15s a que el título no esté vacío
    try:
        WebDriverWait(driver, 15).until(lambda d: d.title and d.title.strip() != "")
    except Exception:
        pass

    print("Title:", repr(driver.title))
    # Mostrar longitud del page_source y primeros 500 caracteres
    src = driver.page_source or ""
    print("page_source length:", len(src))
    print("page_source head:", src[:500].replace("\n", " "))

    # Alternativa: esperar a un elemento conocido de la página
    try:
        elem = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "practice-form-wrapper"))
        )
        print("Elemento practice-form-wrapper visible")
    except Exception as e:
        print("No se encontró practice-form-wrapper:", e)

    time.sleep(5)
finally:
    driver.quit()
