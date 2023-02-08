import argparse
import yaml
import wget
import subprocess

def runcmd(cmd, verbose = False, *args, **kwargs):
    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

def parse_args():
    parser = argparse.ArgumentParser(description='Simple DIY home assistant')
    subparsers = parser.add_subparsers(dest='subcommand')
    parser_download = subparsers.add_parser('download')
    parser_download.add_argument('model', help='The type of model to download')
    parser_config = subparsers.add_parser('config', help='Path to config file')
    parser_config.add_argument('config', help='Path to config file')
    args = parser.parse_args()
    config = {}
    if hasattr(args, 'config'):
        with open(args.config) as f:
            config = yaml.safe_load(f)
    return args, config

def download_model(model):
    small = 'wget --cut-dirs=5 -nH -r --no-parent --reject "index.html*" \
        https://the-eye.eu/public/AI/models/GPT-NeoX-20B/slim_weights/ -P data/20B_checkpoints'
    large = 'wget --cut-dirs=5 -nH -r --no-parent --reject "index.html*" \
        https://the-eye.eu/public/AI/models/GPT-NeoX-20B/full_weights/ -P data/20B_checkpoints'
    if model == 'wee':
        print('Downloading wee model (this may take a while)...')
        runcmd(small, verbose = True)
    else:
        print('Downloading homongous model (this may take more than a while)...')
        runcmd(large, verbose = True)