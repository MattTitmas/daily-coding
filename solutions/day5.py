import argparse


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(con):
    return con(lambda a, _: a)


def cdr(con):
    return con(lambda _, b: b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='car and cdr')
    parser.add_argument("-value1", type=int, required=True,
                        help='first element of cons')
    parser.add_argument("-value2", default=int, required=True,
                        help="second element of cons")
    parser.add_argument("-v", default=False, action="store_true",
                        help="make output verbose")
    args = parser.parse_args()

    print(f'First element: {car(cons(args.value1, args.value2))}')
    print(f'Second element: {cdr(cons(args.value1, args.value2))}')
