import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()
    headless = os.environ.get("HEADLESS", "1") != "0"
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1366,768")

    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=opts)
    yield d
    d.quit()
