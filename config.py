from json import load


def get_config():
    with open('/etc/quasar/quasar.config', 'r') as cfg:
        return load(cfg)


if __name__ == '__main__':
    print(get_config())
