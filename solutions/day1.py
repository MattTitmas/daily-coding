import argparse


def add_to(numbers: list, value: int):
    values_wanted = set()
    for i in numbers:
        if i in values_wanted:
            return value - i, i
        values_wanted.add(value - i)
    return None, None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find elements in the list that sum to the value")
    parser.add_argument('-value', type=int, default=17,
                        help='value to sum to')
    parser.add_argument('-list', nargs='+', type=int, default=[10, 15, 7, 3])
    parser.add_argument('-v', default=False, action='store_true',
                        help='make output verbose')
    args = parser.parse_args()
    combination = add_to(args.list, args.value)
    print(f'The list {", ".join([str(i) for i in args.list])} can produce {args.value} '
          f'with {combination[0]} + {combination[1]}')
