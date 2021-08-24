import logging
import os
import pickle


def create_folder(directory):
    """Creates a folder if it doesn't exist.

    Returns:
        None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"{directory} folder created.")
    else:
        logging.info(f"{directory} folder already existed.")


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


def save_model(model):
    pickle.dump(model, open("model.pkl", "wb"))
