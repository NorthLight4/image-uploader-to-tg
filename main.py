import requests
import datetime
import os
from pathlib import Path
from os.path import splitext
from urllib.parse import urlparse
from dotenv import load_dotenv


def download_image(image_url, image_path):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(launch_id):
    api_url_template = 'https://api.spacexdata.com/v5/launches/{}'
    api_url = api_url_template.format(launch_id)

    response = requests.get(api_url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr']['original']
    for image_num, image_url in enumerate(image_urls):
        download_image(image_url, f'images/spacex_{image_num}.jpg')


def get_file_extension_from_url(url):
    path = urlparse(url).path
    extension = splitext(path)[-1]
    return extension


def fetch_nasa_apod(count):
    api_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': os.environ['NASA_API_KEY'],
        'count': count
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()

    image_urls = []
    for resp in response.json():
        image_urls.append(resp['url'])

    for image_num, image_url in enumerate(image_urls):
        extension = get_file_extension_from_url(image_url)
        download_image(image_url, f'images/nasa_apod_{image_num}{extension}')


def fetch_nasa_epic(count):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': os.environ['NASA_API_KEY']
    }

    response = requests.get(api_url, params=payload)
    response.raise_for_status()

    image_urls = []
    for i in range(count):
        image_date = response.json()[i]['date']
        DateTime = datetime.datetime.fromisoformat(image_date)
        year, month, day = DateTime.year, DateTime.month, DateTime.day
        image = response.json()[i]['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/0{month}/{day}/png/{image}.png?api_key=DEMO_KEY'
        download_image(image_url, f'images/nasa_epic_{i}.png')


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)

    fetch_spacex_last_launch('5eb87d2dffd86e000604b376')
    fetch_nasa_apod(3)
    fetch_nasa_epic(3)


if __name__ == "__main__":
    main()
