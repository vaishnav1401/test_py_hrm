from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.pim_header = (By.XPATH, "//h6[text()='PIM']")

    def click_pim_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.pim_menu)).click()

    def verify_pim_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_header))
        return self.driver.find_element(*self.pim_header).is_displayed()