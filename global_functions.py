import requests
from os.path import splitext
from urllib.parse import urlparse


def download_image(image_url, image_path, payload=None):
    if payload:
        response = requests.get(image_url, params=payload)
    else:
        response = requests.get(image_url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def get_file_extension_from_url(url):
    path = urlparse(url).path
    extension = splitext(path)[-1]
    return extension
