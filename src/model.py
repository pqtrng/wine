from sklearn.ensemble import RandomForestRegressor


def get_model(max_depth, seed):
    regr = RandomForestRegressor(max_depth=max_depth, random_state=seed)
    return regr


if __name__ == '__main__':
    model = get_model(max_depth=10, seed=100)
    print(model)