from telnetlib import EC
import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SubscriptionPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # --- Locators ---
    ENGLISH_BUTTON = (By.XPATH, "//a[@data-test-id='language-switcher-btn']")
    HEADER_COUNTRY_SWITCH_LOCATOR = (By.XPATH, "//button[@data-test-id='header-country-switch']")
    COUNTRY_CONTAINER = (By.CSS_SELECTOR, "div[data-testid='country-picker-wrapper']")
    KUWAIT_PICKER = (By.ID, "kw-country-label")
    KSA_PICKER = (By.ID, "sa-country-label")
    BEH_PICKER = (By.ID, "bh-country-label")
    BASIC_CARD = (By.CSS_SELECTOR, "div[data-test-id='FREE_TIER-component']")
    BASIC_TITLE = (By.XPATH, "//div[@data-test-id='FREE_TIER-component']//strong[@data-test-id='tier-title']")
    PREMIUM_CARD = (By.CSS_SELECTOR, "div[data-test-id='PLUS_TIER-component']")
    PREMIUM_TITLE = (By.XPATH, "//div[@data-test-id='PLUS_TIER-component']//strong[@data-test-id='tier-title']")
    PREMIUM_PRICE_LOCATOR = (By.CSS_SELECTOR, "div[data-test-id='tier-price'] b")
    PREMIUM_CURRENCY_LOCATOR = (By.CSS_SELECTOR, "div[data-test-id='tier-price'] i")

    # --- Page Methods ---
    def click_english_button(self):
        """Click the English language switch button"""
        self.click_element(self.ENGLISH_BUTTON)
        # time.sleep(5)

    def click_country_switch_button(self):
        """Click the currency/country switch button"""
        time.sleep(5)
        self.click_element(self.HEADER_COUNTRY_SWITCH_LOCATOR)

    def choose_ksa(self):
        element = self.find_element(self.KUWAIT_PICKER)
        element.click()

    def choose_kuwait(self):
        element = self.find_element(self.KUWAIT_PICKER)
        element.click()

    def choose_Bahrain(self):
        element = self.find_element(self.BEH_PICKER)
        element.click()

    # --- Methods to verify visibility ---
    def is_basic_card_visible(self):
        """Return True if Basic card is visible"""
        element = self.find_element(self.BASIC_CARD)
        return element is not None

    def get_basic_text(self):
        element = self.find_element(self.BASIC_TITLE)
        return element.text.strip()

    def is_premium_card_visible(self):
        """Return True if Premium card is visible"""
        element = self.find_element(self.PREMIUM_CARD)
        return element is not None

    def get_premium_text(self):
        element = self.find_element(self.PREMIUM_TITLE)
        return element.text.strip()

    def get_premium_price(self):
        element = self.find_element(self.PREMIUM_PRICE_LOCATOR)
        time.sleep(4)
        return element.text.strip()

    def get_premium_currency(self):
        element = self.find_element(self.PREMIUM_CURRENCY_LOCATOR)
        return element.text.strip()
