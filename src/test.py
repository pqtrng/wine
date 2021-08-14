import hydra
from omegaconf.dictconfig import DictConfig


@hydra.main(config_path="../configs", config_name="default")
def main(cfg: DictConfig):
    print(hydra.utils.get_original_cwd())


if __name__ == "__main__":
    main()
