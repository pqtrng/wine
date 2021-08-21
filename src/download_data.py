import logging

import requests

from src.utils import check_execution_path
from src.utils import create_folder

DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

# Initial local dataset location
LOCAL_FILE_NAME = "data/wine_quality.csv"


def download_dataset(url=DATASET_URL, filename=LOCAL_FILE_NAME):
    print(f"Downloading from {url} to {filename}")
    response = requests.get(url)

    with open(filename, "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started download script")

    if check_execution_path():
        create_folder()
        download_dataset()

    logging.info("Finished download script")
