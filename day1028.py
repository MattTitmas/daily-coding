import argparse

'''
The number 6174 is known as Kaprekar's contant, after the mathematician who discovered
an associated property: for all four-digit numbers with at least two distinct digits,
repeatedly applying a simple procedure eventually results in this value.
The procedure is as follows:
For a given input x, create two new numbers that consist of the digits in x in ascending and
descending order.
Subtract the smaller number from the larger number.
'''

def kaprekar(value: int, verbose: bool):
    stored_int = value
    current_step = 0
    while stored_int != 6174:
        ascending = "".join(sorted(list(str(stored_int))))
        descending = ascending[::-1]
        stored_int = int(descending) - int(ascending)
        if verbose:
            print(f'Step: {current_step}\t\t{descending} - {ascending} = {stored_int}')
        current_step += 1
    return current_step



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Perform Kaprekar's procedure")
    parser.add_argument("-value", type=int, required=True,
                        help='value to perform the procedure on')
    parser.add_argument("-v", default=False, action="store_true",
                        help="make output verbose")
    args = parser.parse_args()
    current = 0
    steps = kaprekar(args.value, args.v)
    print(f'{args.value} took {steps} steps to reach 6174')