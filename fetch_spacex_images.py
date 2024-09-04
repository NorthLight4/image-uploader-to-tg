import requests
import argparse
from pathlib import Path
from global_functions import download_image


def fetch_spacex_launch(launch_id):
    api_url_template = 'https://api.spacexdata.com/v5/launches/{}'
    api_url = api_url_template.format(launch_id)

    response = requests.get(api_url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr']['original']
    for image_num, image_url in enumerate(image_urls):
        download_image(image_url, f'images/spacex_{image_num}.jpg')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Программа, которая загружает фотографии запуска ракет spaceX по ID запуска. По умолчанию скачивает фото последнего запуска (при их наличии)'
    )
    parser.add_argument('-launch_id', help='ID запуска', type=str, default='latest')
    args = parser.parse_args()

    fetch_spacex_launch(args.launch_id)


if __name__ == "__main__":
    main()
