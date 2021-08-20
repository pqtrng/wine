"""Download the csv dataset."""
import logging

import requests

from src.utils import check_execution_path
from src.utils import create_folder

DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
LOCAL_FILE_NAME = "data/wine_quality.csv"


def download_dataset(url=DATASET_URL, local_file=LOCAL_FILE_NAME):
    """download_dataset downloads the remote dataset to a local path.

    Args:
        url (str, optional): complete url path to the csv data source. Defaults to DATASET_URL.
        local_file (str, optional): initial local file location. Defaults to DATASET_URL.
    """

    logging.info(f"\tDownloading data from {url}")
    response = requests.get(url=url)
    with open(file=local_file, mode="wb") as file:
        file.write(response.content)

    logging.info("Download completed.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started download script")

    if check_execution_path():
        create_folder()
        download_dataset()

    logging.info("Finish download script")
