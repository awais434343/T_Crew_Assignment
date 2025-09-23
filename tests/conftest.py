import pytest
from selenium.common import (
    TimeoutException,
    StaleElementReferenceException,
    NoSuchElementException,
    ElementNotInteractableException
)
from selenium.webdriver.support.ui import WebDriverWait
from utils.driver_factory import get_driver
from utils.logger import FrameworkLogger
from utils.soft_asserts import SoftAssert
from utils.yaml_loader import TestDataProvider

logger = FrameworkLogger.get_logger("conftest")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="Environment name")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


@pytest.fixture(scope='session')
def my_driver(request):
    browser = request.config.getoption("--browser")
    env = request.config.getoption("--env")
    logger.info(f"Starting WebDriver for browser: {browser} on env: {env}")
    driver = get_driver(browser)
    # TestDataProvider.initialize(client="test_data", env=env)
    # # Navigate to base URL of selected environment
    # base_url = TestDataProvider.get_env_url()
    # driver.get(base_url)
    # logger.info(f"Navigated to URL: {base_url}")
    wait = WebDriverWait(
        driver,
        timeout=30,
        poll_frequency=1,
        ignored_exceptions=[
            TimeoutException,
            StaleElementReferenceException,
            NoSuchElementException,
            ElementNotInteractableException
        ]
    )
    yield driver, wait
    logger.info("Quitting WebDriver")
    driver.quit()


@pytest.fixture()
def soft_assert():
    sa = SoftAssert()
    yield sa
    sa.assert_all()
