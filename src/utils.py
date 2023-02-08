import argparse
import yaml
from easydict import EasyDict

def parse_args():
    parser = argparse.ArgumentParser(description='Simple DIY home assistant')
    parser.add_argument('--config', type=str, default='')
    return parser.parse_args()

def parse_config():
    args = parse_args()
    with open(args.config) as f:
        config = yaml.safe_load(f)
    
    for key, value in vars(args).items():
        if value is not None:
            config[key] = value

    config = EasyDict(config)
    return config