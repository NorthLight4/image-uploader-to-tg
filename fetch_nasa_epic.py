import argparse
import os
import requests
import datetime
from pathlib import Path
from dotenv import load_dotenv
from global_functions import download_image


def fetch_nasa_epic(count):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = os.environ['NASA_API_KEY']
    payload = {
        'api_key': api_key
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()

    for i in range(count):
        image_date = response.json()[i]['date']
        DateTime = datetime.datetime.fromisoformat(image_date)
        year, month, day = str(DateTime.year), str(DateTime.month), str(DateTime.day)
        if len(month) == 1:
            month = '0' + month
        if len(day) == 1:
            day = '0' + day

        image = response.json()[i]['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png?api_key={api_key}'
        download_image(image_url, f'images/nasa_epic_{i}.png')


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Программа, которая скачивает Nasa EPIC. По умолчанию скачивается одно изображение'
    )
    parser.add_argument('-count', help='Количество скачиваемых изображений')
    args = parser.parse_args()
    count = args.count
    if count is None:
        count = 1

    fetch_nasa_epic(int(count))


if __name__ == "__main__":
    main()
