from itertools import combinations_with_replacement


def combine(input_s, input_k):
    return list(combinations_with_replacement(sorted(input_s), input_k))


def format_combine(combined_list):
    stringify = [''.join(i) for i in combined_list]
    print(f"{'\n'.join(stringify)}")


if __name__ == "__main__":
    S, k = input().split(" ")
    combine_list = combine(S, int(k))
    format_combine(combine_list)
