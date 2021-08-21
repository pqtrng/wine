import logging
import os


def create_folder():
    """Creates a data folder if it doesn't exist.

    Returns:
        None
    """
    directory = "data/"
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info("Data folder created.")
    else:
        logging.info("Data folder already existed.")


def check_execution_path():
    """Check if the function and therefore all subsequent functions
        are executed from the root of the project
    Returns:
        boolean -- returns False if execution path isn't the root,
            otherwise True
    """
    file_name = "LICENSE.md"
    if not os.path.exists(file_name):
        logging.error(
            "Don't execute the script from a sub-directory. "
            "Switch to the root of the project folder"
        )
        return False
    return True
