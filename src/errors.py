import time
from utils import is_connected
from actions import send_image_with_message

def handle_conn_error(number , message , img_path):
    conn_status = is_connected('web.whatsapp.com', 80)
    if conn_status == False:
        time.sleep(300)
        # send msg again
        send_image_with_message(number, message, img_path)
