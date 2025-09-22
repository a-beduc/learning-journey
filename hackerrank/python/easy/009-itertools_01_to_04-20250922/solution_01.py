from itertools import product


def clean_input():
    return [int(i) for i in input().split(' ')]


def cartesian_product(list_a, list_b):
    return list(product(list_a, list_b))


def format_result(cartesian_list):
    print(' '.join([str(i) for i in cartesian_list]))


if __name__ == "__main__":
    A, B = clean_input(), clean_input()
    output = cartesian_product(A, B)
    format_result(output)
