import os
import requests
import argparse
from pathlib import Path
from dotenv import load_dotenv
from global_functions import get_file_extension_from_url, download_image


def fetch_nasa_apod(count):
    api_url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.environ['NASA_API_KEY']
    payload = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()

    image_urls = []
    for item in response.json():
        image_urls.append(item['url'])

    for image_num, image_url in enumerate(image_urls):
        extension = get_file_extension_from_url(image_url)
        download_image(image_url, f'images/nasa_apod_{image_num}{extension}')


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Программа, которая скачивает Nasa APOD. По умолчанию скачивается одно изображение'
    )
    parser.add_argument('-count', help='Количество скачиваемых изображений')
    args = parser.parse_args()
    count = args.count
    if count is None:
        count = 1

    fetch_nasa_apod(count)


if __name__ == "__main__":
    main()
