import random
import argparse


def main(s: list) -> None:

    for part in s:
        print(
            part[0] + ''.join(
                random.sample(part[1:], len(part[1:]))), end=' ')

    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('string', nargs='*')

    args = parser.parse_args()

    main(args.string)
