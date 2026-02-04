import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.login_page import LoginPage
from PageObject.leave_page import LeavePage
from config import LOGIN_URL, ADMIN_USERNAME, ADMIN_PASSWORD

def test_leave_tab(driver):
    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    # Wait for dashboard to load
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    # Now test Leave tab
    leave_page = LeavePage(driver)
    leave_page.click_leave_menu()

    # Verify Leave page is loaded
    assert leave_page.verify_leave_page_loaded(), "Leave page did not load correctly"