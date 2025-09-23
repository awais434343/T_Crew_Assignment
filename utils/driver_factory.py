import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


# def get_driver(browser="firefox"):
#     # Read HEADLESS from environment, default to True
#     headless = os.getenv("HEADLESS", "true").lower() == "true"
#
#     if browser.lower() == "chrome":
#         options = ChromeOptions()
#         if headless:
#             options.add_argument("--headless=new")  # Use latest headless mode
#             options.add_argument("--no-sandbox")  # Required for CI
#             options.add_argument("--disable-dev-shm-usage")  # Avoid small shared memory issues
#             options.add_argument("--window-size=1920,1080")  # Ensure enough viewport
#             options.add_argument("--disable-gpu")  # Sometimes needed on Windows
#             options.add_argument("--disable-extensions")
#             options.add_argument("--start-maximized")
#             options.add_argument("--remote-debugging-port=9222")  # Optional: helpful for debugging
#         driver = webdriver.Chrome(options=options)
#
#     else:  # Firefox
#         options = FirefoxOptions()
#         if headless:
#             options.add_argument("--headless")
#             options.add_argument("--width=1920")
#             options.add_argument("--height=1080")
#             options.add_argument("--disable-gpu")
#             options.add_argument("--no-sandbox")
#         driver = webdriver.Firefox(options=options)
#         driver.set_window_size(1920, 1080)  # Extra safety for scrolling
#
#     driver.maximize_window()  # Ensure full viewport
#     return driver

def get_driver(browser="firefox"):
    headless = False
    if browser.lower() == "chrome":
        options = ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        options.page_load_strategy = "eager"   # 👈 important
        driver = webdriver.Chrome(options=options)

    else:  # Firefox
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("webdriver.load.strategy", "eager")  # 👈 important
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.set_page_load_timeout(60)
    return driver
