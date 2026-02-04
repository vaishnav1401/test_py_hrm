from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TimePage:
    def __init__(self, driver):
        self.driver = driver
        self.time_menu = (By.XPATH, "//span[text()='Time']")
        self.time_header = (By.XPATH, "//h6[text()='Time']")

    def click_time_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.time_menu)).click()

    def verify_time_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.time_header))
        return self.driver.find_element(*self.time_header).is_displayed()