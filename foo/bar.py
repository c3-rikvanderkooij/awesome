from pathlib import PurePath


def add_one(number):
    return number + 1


def read_config():
    root = PurePath(__file__).parents[0]
    with open(root / 'config/config.xml') as f:
        s = f.read()
    return s
