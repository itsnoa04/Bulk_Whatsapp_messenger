from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from config import config


def new_browser():
    try:
        options = Options()
        profile = FirefoxProfile(config['browser_profile_path'])
        options.profile = profile
        browser = webdriver.Firefox(
            executable_path=config['driver_path'],
            options=options,
        )
        return browser

    except Exception as e:
        error = ("failed", e, "check your browser profile path and driver path")
        return error


browser = new_browser()
