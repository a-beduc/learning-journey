from itertools import combinations


def combine(S, k):
    sort_string = sorted(S)
    output = [list(combinations(sort_string, i)) for i in range(1, k + 1)]
    return output


def format_combine(list_combined):
    stringify = [''.join(i) for sublist in list_combined for i in sublist]
    print(f"{'\n'.join(stringify)}")


if __name__ == "__main__":
    S, k = input().split(" ")
    combined = combine(S, int(k))
    format_combine(combined)
