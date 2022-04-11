from browser import browser
from selenium.webdriver.common.by import By


def attachment_btn():
    return (
        By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
    )


def image_upload_btn():
    return (
        By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input'
    )


def send_btn():
    return (
        By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div'
    )


def get(element):
    return browser.find_element(element[0], element[1])
