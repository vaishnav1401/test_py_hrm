from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.leave_menu = (By.XPATH, "//span[text()='Leave']")
        self.leave_header = (By.XPATH, "//h6[text()='Leave']")

    def click_leave_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.leave_menu)).click()

    def verify_leave_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.leave_header))
        return self.driver.find_element(*self.leave_header).is_displayed()