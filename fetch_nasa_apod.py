import os
import requests
import argparse
from pathlib import Path
from dotenv import load_dotenv
from global_functions import get_file_extension_from_url, download_image


def fetch_nasa_apod(api_key, count):
    api_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()

    image_urls = [image_data['url'] for image_data in response.json()]
    for image_num, image_url in enumerate(image_urls):
        extension = get_file_extension_from_url(image_url)
        download_image(image_url, f'images/nasa_apod_{image_num}{extension}')


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Программа, которая скачивает Nasa APOD. По умолчанию скачивается одно изображение'
    )
    parser.add_argument('-count', help='Количество скачиваемых изображений', type=int, default=1)
    args = parser.parse_args()

    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_apod(api_key, args.count)


if __name__ == "__main__":
    main()
