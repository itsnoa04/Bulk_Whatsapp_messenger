from csv import reader
from browser import browser
from config import config, message
from actions import send_image_with_message
from errors import handle_conn_error
from log import log


browser.maximize_window()


with open(config['contacts_path'], 'r') as contacts_file:
    reader = reader(contacts_file)

    index = 0
    img_path = config['img_path']

    for row in reader:
        try:
            send_image_with_message(row[0], message, img_path)
            log(row[0], 'success', 'success')
        except Exception as e:
            print(e)
            handle_conn_error(row[0], message, img_path)
            log(row[0], 'failed', e)
            continue

# retry_failed_numbers()
# browser.quit()
