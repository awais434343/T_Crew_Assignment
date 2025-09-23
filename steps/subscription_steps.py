import allure
from pages.subscription_page import SubscriptionPage  # Updated page import
from utils.logger import FrameworkLogger


class SubscriptionSteps:
    def __init__(self, my_driver, soft_assert):
        self.driver, self.wait = my_driver
        self.soft_assert = soft_assert
        self.subscription_page = SubscriptionPage(self.driver, self.wait)
        self.logger = FrameworkLogger.get_logger(self.__class__.__name__)

    # ---------------------- Basic Test Scripts Steps -------------------- #
    def verify_ksa_basic_card(self):
        with allure.step("Navigate to the main URL"):
            url = "https://subscribe.stctv.com/"
            self.logger.info(f"Opening URL: {url}")
            self.subscription_page.open_url(url)

        # with allure.step("Click the English language button"):
        #     self.logger.info("Clicking on the English language button")
        #     self.subscription_page.click_english_button()

        with allure.step("Verify that the Basic card is visible"):
            self.logger.info("Checking visibility of Basic card")
            visible = self.subscription_page.is_basic_card_visible()
            self.logger.info(f"Basic card visible: {visible}")
            self.soft_assert.assert_true(visible, "Basic card should be visible for KSA")

    def verify_Bahrain_basic_card(self):
        with allure.step("Navigate to the main URL"):
            url = "https://subscribe.stctv.com/"
            self.logger.info(f"Opening URL: {url}")
            self.subscription_page.open_url(url)

        with allure.step("Click the country changing button"):
            self.logger.info("Clicking on country change button")
            self.subscription_page.click_country_switch_button()

        with allure.step("Select Bahrain as the country"):
            self.subscription_page.choose_Bahrain()
            self.logger.info("Chosen bahrain country")

        with allure.step("Verify that the Basic card is visible"):
            self.logger.info("Checking visibility of Basic card")
            visible = self.subscription_page.is_basic_card_visible()
            self.logger.info(f"Basic card visible: {visible}")
            self.soft_assert.assert_true(visible, "Basic card should be visible for Bahrain")

    def verify_Kuwait_basic_card(self):
        with allure.step("Navigate to the main URL"):
            url = "https://subscribe.stctv.com/"
            self.logger.info(f"Opening URL: {url}")
            self.subscription_page.open_url(url)

        with allure.step("Click the country change button"):
            self.logger.info("Clicking on country change button")
            self.subscription_page.click_country_switch_button()

        with allure.step("Select Kuwait as the country"):
            self.subscription_page.choose_kuwait()
            self.logger.info("Chosen Kuwait country")

        with allure.step("Verify that the Basic card is visible"):
            self.logger.info("Checking visibility of Basic card")
            visible = self.subscription_page.is_basic_card_visible()
            self.logger.info(f"Basic card visible: {visible}")
            self.soft_assert.assert_true(visible, "Basic card should be visible for Kuwait")

    # ---------------------- Premium Test Scripts steps -------------------- #
    def verify_ksa_premium_card_price_currency(self):
        with allure.step("Navigate to the main URL"):
            url = "https://subscribe.stctv.com/"
            self.logger.info(f"Opening URL: {url}")
            self.subscription_page.open_url(url)

        with allure.step("Verify that the Premium card is visible and validate price & currency"):
            self.logger.info("Checking if Premium card is visible")
            visible = self.subscription_page.is_premium_card_visible()

            if visible:
                self.logger.info(f"Premium card is visible: {visible}, fetching price & currency")
                price = self.subscription_page.get_premium_price()
                currency = self.subscription_page.get_premium_currency()
                expected_price = "15"
                expected_currency = "ريال سعودي/الشهر"
                # Validate Price
                if self.soft_assert.assert_equal(price, expected_price,
                                                 f"Expected Premium price for KSA:'{expected_price}', got: '{price}'"):
                    self.logger.info(f"Premium price verified successfully: '{price}'")
                # Validate Currency
                if self.soft_assert.assert_equal(currency, expected_currency,
                                                 f"Expected Premium currency for KSA: '{expected_currency}', got: '{currency}'"):
                    self.logger.info(f"Premium currency verified successfully: '{currency}'")
            else:
                self.logger.warning("Premium card not visible for KSA — unable to verify price and currency")

    def verify_kwd_premium_card_price_currency(self):
        with allure.step("Navigate to the main URL"):
            url = "https://subscribe.stctv.com/"
            self.logger.info(f"Opening URL: {url}")
            self.subscription_page.open_url(url)

        with allure.step("Click the country change button"):
            self.logger.info("Clicking the country change button")
            self.subscription_page.click_country_switch_button()

        with allure.step("Select Kuwait as the country"):
            self.logger.info("Selecting country: bahrain")
            self.subscription_page.choose_kuwait()

        with allure.step("Verify that the Premium card is visible and validate price & currency"):
            self.logger.info("Checking if Premium card is visible")
            visible = self.subscription_page.is_premium_card_visible()

            if visible:
                self.logger.info(f"Premium card is visible: {visible}, fetching price & currency")
                price = self.subscription_page.get_premium_price()
                currency = self.subscription_page.get_premium_currency()
                expected_price = "2.5"
                expected_currency = "دينار كويتي/الشهر"
                # Validate Price
                if self.soft_assert.assert_equal(price, expected_price,
                                                     f"Expected Premium price for Kuwait:'{expected_price}', got: '{price}'"):
                    self.logger.info(f"Premium price verified successfully: '{price}'")
                # Validate Currency
                if self.soft_assert.assert_equal(currency, expected_currency,
                                                     f"Expected Premium currency for Kuwait: '{expected_currency}', got: '{currency}'"):
                    self.logger.info(f"Premium currency verified successfully: '{currency}'")
            else:
                self.logger.warning("Premium card not visible for Kuwait — unable to verify price and currency")

    def verify_bahrain_premium_card_price_currency(self):
        with allure.step("Navigate to the main URL"):
            url = "https://subscribe.stctv.com/"
            self.logger.info(f"Opening URL: {url}")
            self.subscription_page.open_url(url)

        with allure.step("Click the country change button"):
            self.logger.info("Clicking the country change button")
            self.subscription_page.click_country_switch_button()

        with allure.step("Select bahrain as the country"):
            self.logger.info("Selecting country: bahrain")
            self.subscription_page.choose_Bahrain()

        with allure.step("Verify that the Premium card is visible and validate price & currency"):
            self.logger.info("Checking if Premium card is visible")
            visible = self.subscription_page.is_premium_card_visible()

            if visible:
                self.logger.info(f"Premium card is visible: {visible}, fetching price & currency")
                price = self.subscription_page.get_premium_price()
                currency = self.subscription_page.get_premium_currency()
                expected_price = "3"
                expected_currency = "دينار بحريني/الشهر"
                # Validate Price
                if self.soft_assert.assert_equal(price, expected_price,
                                                     f"Expected Premium price for bahrain:'{expected_price}', got: '{price}'"):
                    self.logger.info(f"Premium price verified successfully: '{price}'")
                # Validate Currency
                if self.soft_assert.assert_equal(currency, expected_currency,
                                                     f"Expected Premium currency for bahrain: '{expected_currency}', got: '{currency}'"):
                    self.logger.info(f"Premium currency verified successfully: '{currency}'")
            else:
                self.logger.warning("Premium card not visible for bahrain — unable to verify price and currency")
