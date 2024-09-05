import argparse
import os
import requests
import datetime as dt
from pathlib import Path
from dotenv import load_dotenv
from global_functions import download_image_with_payload


def fetch_nasa_epic(api_key, count):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': api_key
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    response_data = response.json()

    for image_num in range(count):
        image_date = response_data[image_num]['date']
        date_time = dt.datetime.fromisoformat(image_date)
        formatted_date = date_time.strftime("%Y-%m-%d")
        year, month, day = formatted_date.split('-')

        image = response_data[image_num]['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        payload = {
            'api_key': api_key
        }
        download_image_with_payload(image_url, payload, f'images/nasa_epic_{image_num}.png')


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Программа, которая скачивает Nasa EPIC. По умолчанию скачивается одно изображение'
    )
    parser.add_argument('-count', help='Количество скачиваемых изображений', type=int, default=1)
    args = parser.parse_args()

    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_epic(api_key, args.count)


if __name__ == "__main__":
    main()
