import argparse
from time import sleep
from typing import Callable


def schedule(n: int, f: Callable, verbose: bool = False):
    if verbose:
        print(f'Waiting {n} milliseconds')
    sleep(n / 1000)
    f()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wait n millisecond")
    parser.add_argument('-time', type=int, default=1, required=True,
                        help='time to wait (milliseconds)')
    parser.add_argument('-v', default=False, action='store_true',
                        help='make output verbose')
    args = parser.parse_args()

    schedule(args.time, lambda: print('Hello world!'), args.v)
