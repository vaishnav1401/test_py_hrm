import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.login_page import LoginPage
from PageObject.pim_page import PIMPage
from config import LOGIN_URL, ADMIN_USERNAME, ADMIN_PASSWORD

def test_pim_tab(driver):
    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    # Wait for dashboard to load
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    # Now test PIM tab
    pim_page = PIMPage(driver)
    pim_page.click_pim_menu()

    # Verify PIM page is loaded
    assert pim_page.verify_pim_page_loaded(), "PIM page did not load correctly"