import argparse
import telegram
import time
import random
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='ТГ бот публикует всю директорию изображений с указанным интервалом. По умолчанию интервал равен 4 часам'
    )
    parser.add_argument('-interval', help='Временной интервал между фото')
    args = parser.parse_args()
    interval = args.interval
    if interval is None:
        interval = 14400

    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    images = list(os.walk('images'))[0][2]

    while True:
        for image in images:
            bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
            time.sleep(int(interval))
        random.shuffle(images)


if __name__ == "__main__":
    main()
