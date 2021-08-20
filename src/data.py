import pandas as pd
from sklearn.model_selection import train_test_split


def get_data(data_path, test_size, delimiter, seed):

    # Load in the data
    df = pd.read_csv(data_path, delimiter=delimiter)

    # Split into train and test sections
    y = df.pop("quality")
    X_train, X_test, y_train, y_test = train_test_split(
        df, y, test_size=test_size, random_state=seed
    )
    return X_train, y_train, X_test, y_test


if __name__ == "__main__":
    get_data()
