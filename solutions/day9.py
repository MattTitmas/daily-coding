import argparse


def maximum_no_adjacent(values: list, verbose: bool = False):
    s2 = values[0]
    s1 = max(s2, values[1])

    for i in range(2, len(values)):
        s0 = max(s1, s2 + values[i])
        s2 = s1
        s1 = s0
    return max(s1, s2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Product of array except itself")
    parser.add_argument('-list', nargs='+', type=int, default=[5, 1, 1, 5])
    parser.add_argument('-v', default=False, action='store_true',
                        help='make output verbose')
    args = parser.parse_args()

    print(f'maximum sum of {args.list} without adjacent elements is: {maximum_no_adjacent(args.list, args.v)}')