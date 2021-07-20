import requests
from utils import file_functions


def download_asset(uris, house_name):
    media_path = f"media/{house_name}"
    file_functions.create_media_dir(media_path)

    for uri in uris:
        asset = requests.get(uri)
        filename = uri.split("/")[-1]
        file_functions.create_asset(media_path, filename, asset.content)
