import pprint
import config

FLAGS = None


def main(_):
    # TODO(LuHa): read configuration from file
    pass


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str,
                        default='config.ini',
                        help=('configuration file. '
                              'you can copy .template file'))

    FLAGS, _ = parser.parse_known_args()
    main(_)

