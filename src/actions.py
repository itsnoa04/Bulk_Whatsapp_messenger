import time
import urllib.parse as parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import browser
from elements import attachment_btn, image_upload_btn, send_btn, get


whatsapp_url = 'https://web.whatsapp.com/send/?'


def send_image_with_message(number, message, image_Dir):

    # API format = https://api.whatsapp.com/send?phone={ phone number }&text={ message }

    payload = {'text': message, 'phone': number}
    url_params = parse.urlencode(
        payload, safe='/', quote_via=parse.quote, encoding='utf-8')
    URL = "{0}{1}&app_absent=0".format(whatsapp_url, url_params)
    print()

    browser.get(URL)
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located(attachment_btn())
    )
    time.sleep(1)
    get(attachment_btn()).click()
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located(image_upload_btn())
    )
    time.sleep(0.5)
    get(image_upload_btn()).send_keys(image_Dir)
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located(send_btn())
    )
    time.sleep(0.5)

    get(send_btn()).click()
    time.sleep(1)
