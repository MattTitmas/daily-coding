import argparse


def lowest_missing(values: list, verbose: bool):
    length = len(values)
    j = len(values) - 1
    for i in range(len(values)-1, -1, -1):
        if values[i] <= 0:
            values[i], values[j] = values[j], abs(values[i])
            j -= 1
    no_of_positive = j + 1

    for i in range(no_of_positive):
        if abs(values[i])-1 < length:
            values[abs(values[i])-1] = abs(values[abs(values[i])-1]) * (-1)

    for c, i in enumerate(values):
        if i > 0:
            return c+1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Product of array except itself")
    parser.add_argument('-list', nargs='+', type=int, default=[10, 15, 7, 3])
    parser.add_argument('-v', default=False, action='store_true',
                        help='make output verbose')
    args = parser.parse_args()

    lowest = lowest_missing(args.list[:], args.v)

    print(f'Lowest missing integer from {", ".join([str(i) for i in args.list])} is {lowest}')

