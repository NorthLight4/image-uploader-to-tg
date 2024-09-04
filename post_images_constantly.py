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
    parser.add_argument('-interval', help='Временной интервал между фото', type=int, default=14400)
    args = parser.parse_args()
    interval = args.interval

    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    images = list(os.walk('images'))[0][2]

    while True:
        for image in images:
            with open(f'images/{image}', 'rb') as image_file:
                bot.send_document(chat_id=chat_id, document=image_file)
            time.sleep(interval)
        random.shuffle(images)


if __name__ == "__main__":
    main()
