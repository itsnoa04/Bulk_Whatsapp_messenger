import csv
from config import config
from actions import send_image_with_message


def log(number, status, message):
    log_file = open(config['log_path'], 'w')
    log_item = '{0} : {1} ==> {2}'.format(number, status, message)
    log_file.write(log_item+' \n')

    if status == 'failed':
        with open(config['failed_path'], 'a') as failed_file:
            csv.writer(failed_file).writerow([number])


def retry_failed_numbers():
    with open(config['failed_path'], 'r') as failed_file:
        reader = csv.reader(failed_file)
        for row in reader:
            send_image_with_message(
                row[0], config['message'], config['img_path'])
