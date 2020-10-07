import yaml

def read_config_file(path):
    """Read yaml config file from specific path. 
    """
    with open(path, 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg