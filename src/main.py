import logging
from pathlib import Path

# third party
import hydra
from omegaconf import DictConfig, OmegaConf

# local
from src.train import train
from src.plot import plot_feature, plot_residual
from src.evaluate import evaluate

logger = logging.getLogger(__name__)


@hydra.main(config_path='../configs', config_name='default')
def main(cfg: DictConfig):
    logger.info(OmegaConf.to_yaml(cfg=cfg))

    path = Path(hydra.utils.get_original_cwd())

    # train model
    X_train, y_train, X_test, y_test, model = train(
        current_path=path,                          data_config=cfg.data,
        model_config=cfg.model
    )

    # evaluate model
    evaluate(
        x_train=X_train,
        y_train=y_train,
        x_test=X_test,
        y_test=y_test,
        model=model
    )

    # visualization
    plot_feature(
        model=model,
        labels=X_train.columns,
        image_config=cfg.visualization.image
    )

    plot_residual(
        x_test=X_test,
        y_test=y_test,
        model=model,
        image_config=cfg.visualization.image
    )


if __name__ == '__main__':
    main()
