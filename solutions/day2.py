import argparse
from functools import reduce


def multipy(values: list, verbose: bool):
    mult_value = int(reduce(lambda a, b: a * b, values))
    prod = [mult_value] * len(values)
    for i in range(len(values)):
        prod[i] = int(prod[i] / values[i])
    if verbose:
        print(f'Calculating using divide:')
        print(f'Value of multiplying all values: {mult_value}')
        print("")

    return prod


def multipy_no_div(values: list, verbose: bool):
    prod = [1] * len(values)

    left = [1] * len(values)
    for i in range(1, len(values)):
        left[i] = left[i-1] * values[i-1]

    right = [1] * len(values)
    for i in range(len(values)-2, -1, -1):
        right[i] = right[i+1] * values[i+1]

    for i in range(0, len(values)):
        prod[i] = left[i] * right[i]

    if verbose:
        print(f'Calculating using divide:')
        print(f'Value of left: {", ".join([str(i) for i in left])}')
        print(f'Value of right: {", ".join([str(i) for i in left])}')
        print("")
    return prod


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Product of array except itself")
    parser.add_argument('-list', nargs='+', type=int, default=[10, 15, 7, 3])
    parser.add_argument('-v', default=False, action='store_true',
                        help='make output verbose')
    args = parser.parse_args()
    prod_div = multipy(args.list, args.v)
    prod_no_div = multipy_no_div(args.list, args.v)

    print(f'Result of calculating the product of the array (div): '
          f'{", ".join([str(i) for i in prod_div])}')
    print(f'Result of calculating the product of the array (no div): '
          f'{", ".join([str(i) for i in prod_no_div])}')
