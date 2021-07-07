import os
from src.data import get_data
from src.model import get_model


def train(current_path, data_config, model_config):
    X_train, y_train, X_test, y_test = get_data(
        data_path=os.path.join(
            current_path,
            data_config.data_path,
            data_config.file_name
        ),
        test_size=data_config.test_size,
        seed=data_config.seed
    )

    model = get_model(**model_config)

    model.fit(X_train, y_train)

    return X_train, y_train, X_test, y_test, model


if __name__ == '__main__':
    train()
