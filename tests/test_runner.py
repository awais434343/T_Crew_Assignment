import pytest
import allure
from steps.subscription_steps import SubscriptionSteps


class TestSubscriptionChecks:

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.title("Verify KSA Basic Subscription Type")
    def test_ksa_basic_card(self, my_driver, soft_assert):
        subscription_steps = SubscriptionSteps(my_driver, soft_assert)
        subscription_steps.verify_ksa_basic_card()

    @allure.title("Verify Kuwait Basic Subscription Type")
    def test_kwd_basic_card(self, my_driver, soft_assert):
        subscription_steps = SubscriptionSteps(my_driver, soft_assert)
        subscription_steps.verify_Kuwait_basic_card()

    @allure.title("Verify Bahrain Basic Subscription Type")
    def test_bhd_basic_card(self, my_driver, soft_assert):
        subscription_steps = SubscriptionSteps(my_driver, soft_assert)
        subscription_steps.verify_Bahrain_basic_card()

# ----------------- Premium Cases --------------------- #

    @allure.title("Verify KSA Premium Subscription Type, Price and Currency")
    def test_ksa_premium_card_price_currency(self, my_driver, soft_assert):
        subscription_steps = SubscriptionSteps(my_driver, soft_assert)
        subscription_steps.verify_ksa_premium_card_price_currency()

    @allure.title("Verify Kuwait Premium Subscription Type, Price and Currency")
    def test_kwd_premium_card_price_currency(self, my_driver, soft_assert):
        subscription_steps = SubscriptionSteps(my_driver, soft_assert)
        subscription_steps.verify_kwd_premium_card_price_currency()

    @allure.title("Verify bahrain Premium Subscription Type, Price and Currency")
    def test_bhd_premium_card_price_currency(self, my_driver, soft_assert):
        subscription_steps = SubscriptionSteps(my_driver, soft_assert)
        subscription_steps.verify_bahrain_premium_card_price_currency()
