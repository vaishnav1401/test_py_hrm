import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.login_page import LoginPage
from PageObject.admin_page import AdminPage
from config import LOGIN_URL, ADMIN_USERNAME, ADMIN_PASSWORD

def test_admin_tab(driver):
    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    # Wait for dashboard to load
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    # Now test admin tab
    admin_page = AdminPage(driver)
    admin_page.click_admin_menu()

    # Verify admin page is loaded
    assert admin_page.verify_admin_page_loaded(), "Admin page did not load correctly"