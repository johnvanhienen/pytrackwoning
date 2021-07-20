import pathlib


def create_media_dir(media_path):
    pathlib.Path(media_path).mkdir(parents=True, exist_ok=True)


def create_asset(media_path, filename, content):
    open(f"{media_path}/{filename}", 'wb').write(content)
