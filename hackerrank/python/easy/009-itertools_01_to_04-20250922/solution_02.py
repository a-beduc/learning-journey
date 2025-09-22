from itertools import permutations


def permute(input_s, input_k):
    return permutations(input_s, input_k)


def format_permute(permuted_list):
    stringify = [''.join(i) for i in permuted_list]
    stringify.sort()
    print(f"{'\n'.join(stringify)}")


if __name__ == "__main__":
    S, k = input().split(" ")
    permute_list = permute(S, int(k))
    format_permute(permute_list)

