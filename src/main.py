import logging
from pathlib import Path

import hydra
import wandb
from omegaconf import DictConfig
from omegaconf import OmegaConf

from src.evaluate import evaluate
from src.plot import plot_feature
from src.plot import plot_residual
from src.train import train

logger = logging.getLogger(__name__)


@hydra.main(config_path="../configs", config_name="default")
def main(cfg: DictConfig):
    logger.info(OmegaConf.to_yaml(cfg=cfg))

    path = Path(hydra.utils.get_original_cwd())

    wandb.init(
        project=cfg.project.name,
        name=cfg.project.model,
        config={
            "test_size": cfg.data.test_size,
            "max_depth": cfg.model.max_depth,
            "seed": cfg.data.seed,
        },
    )

    logger.info("Train model")
    X_train, y_train, X_test, y_test, model = train(
        current_path=path, data_config=cfg.data, model_config=cfg.model
    )
    wandb.sklearn.plot_learning_curve(model, X_train, y_train)

    logger.info("Evaluate model")
    evaluate(
        x_train=X_train,
        y_train=y_train,
        x_test=X_test,
        y_test=y_test,
        model=model,
    )
    wandb.sklearn.plot_summary_metrics(
        model, X=X_train, y=y_train, X_test=X_test, y_test=y_test
    )

    logger.info("Plot features")
    plot_feature(
        model=model,
        labels=X_train.columns,
        image_config=cfg.visualization.image,
    )
    wandb.sklearn.plot_feature_importances(model, model.feature_importances_)

    logger.info("Plot residual")
    plot_residual(
        x_test=X_test,
        y_test=y_test,
        model=model,
        image_config=cfg.visualization.image,
    )
    wandb.sklearn.plot_residuals(model, X_train, y_train)


if __name__ == "__main__":
    main()
