import config

FLAGS = None


def main(_):
    pass


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()

    FLAGS, _ = parser.parse_known_args()
    main(_)

