import argparse
import telegram
import time
import random
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='ТГ бот публикует указанное в качестве параметра фото. При отсутствии параметра публикует случайное фото'
    )
    parser.add_argument('-image_name', help='Название изображения')
    args = parser.parse_args()
    image = args.image_name

    images = list(os.walk('images'))[0][2]
    if image is None:
        image = random.choice(images)

    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))


if __name__ == "__main__":
    main()
