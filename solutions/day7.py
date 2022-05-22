import argparse

def decode(value: int, verbose: bool = False):
    # Dynamic programming

    value = str(value)

    # ways[n] = ways[n-1] + ways[n-1]
    ways = [0] * (len(value) + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, len(value) + 1):
        ways[i] = 0

        if value[i - 1] != '0':
            ways[i] = ways[i-1]

        if value[i-2] == '1' or \
            (value[i-2] == '2' and value[i-1] < '7'):
            ways[i] += ways[i-2]

        if verbose:
            print(f'there are {ways[i]} ways to decode {value[:i]}')

    return ways[len(value)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Number of decodings")
    parser.add_argument('-value', type=int, default=1,
                        help='number to decode')
    parser.add_argument('-v', default=False, action='store_true',
                        help='make output verbose')
    args = parser.parse_args()

    print(f'you can deocde {args.value} in {decode(args.value, args.v)} ways')
