import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.login_page import LoginPage
from config import LOGIN_URL, ADMIN_USERNAME, ADMIN_PASSWORD

def test_login(driver):
    driver.get(LOGIN_URL)
    
    login_page = LoginPage(driver)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    
    # Wait for dashboard to load
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    
    # Verify user is logged in by checking the URL
    assert "dashboard" in driver.current_url