def evaluate(x_train, y_train, x_test, y_test, model):
    train_score = model.score(x_train, y_train) * 100,
    test_score = model.score(x_test, y_test) * 100

    # Write scores to a file
    with open("metrics.txt", 'w') as outfile:
        outfile.write("Training variance explained: %2.1f%%\n" % train_score)
        outfile.write("Test variance explained: %2.1f%%\n" % test_score)


if __name__ == '__main__':
    evaluate()
