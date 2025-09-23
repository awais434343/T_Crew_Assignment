import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_url(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def find_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text.strip()

    def select_item_by_text(self, by_locator, item_text):
        container = self.wait.until(EC.presence_of_element_located(by_locator))
        items = container.find_elements(By.XPATH, "./div")  # direct child divs
        for item in items:
            if item_text in item.text:
                print(item.text)
                item.click()
                break

    def is_element_present(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_attribute(self, locator, attribute_name):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute_name)