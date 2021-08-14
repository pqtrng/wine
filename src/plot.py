import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_residual(x_test, y_test, model, image_config):
    y_pred = model.predict(x_test) + np.random.normal(0, 0.25, len(y_test))

    y_jitter = y_test + np.random.normal(0, 0.25, len(y_test))

    res_df = pd.DataFrame(list(zip(y_jitter, y_pred)), columns=["true", "pred"])

    ax = sns.scatterplot(x="true", y="pred", data=res_df)
    ax.set_aspect("equal")

    ax.set_xlabel("True wine quality", fontsize=image_config.axis_fs)
    ax.set_ylabel(
        "Predicted wine quality", fontsize=image_config.axis_fs
    )  # ylabel
    ax.set_title("Residuals", fontsize=image_config.title_fs)

    # Make it pretty- square aspect ratio
    ax.plot(
        image_config.x_size,
        image_config.y_size,
        image_config.color,
        linewidth=image_config.line_width,
    )
    plt.ylim((image_config.limit_bottom, image_config.limit_top))
    plt.xlim((image_config.limit_bottom, image_config.limit_top))

    plt.tight_layout()
    plt.savefig("residuals.png", dpi=image_config.dpi)
    plt.close()


def plot_feature(model, labels, image_config):
    importances = model.feature_importances_

    feature_df = pd.DataFrame(
        list(zip(labels, importances)), columns=["feature", "importance"]
    )
    feature_df = feature_df.sort_values(
        by="importance",
        ascending=False,
    )

    # image formatting
    sns.set(style=image_config.style)

    ax = sns.barplot(x="importance", y="feature", data=feature_df)

    ax.set_xlabel("Importance", fontsize=image_config.axis_fs)
    ax.set_ylabel("Feature", fontsize=image_config.axis_fs)

    ax.set_title(
        "Random forest\nfeature importance", fontsize=image_config.title_fs
    )

    plt.tight_layout()
    plt.savefig("feature_importance.png", dpi=image_config.dpi)
    plt.close()


if __name__ == "__main__":
    pass
