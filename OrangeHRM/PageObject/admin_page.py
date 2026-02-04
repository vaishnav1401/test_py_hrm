from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.admin_header = (By.XPATH, "//h6[text()='Admin']")

    def click_admin_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.admin_menu)).click()

    def verify_admin_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.admin_header))
        return self.driver.find_element(*self.admin_header).is_displayed()