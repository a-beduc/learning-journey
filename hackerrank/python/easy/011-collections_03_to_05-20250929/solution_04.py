from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    ordered_dictionary = OrderedDict()
    for _ in range(N):
        key, value = input().rsplit(" ", 1)
        old_value = ordered_dictionary.setdefault(key, 0)
        ordered_dictionary[key] += int(value)
    output_text = []
    for key, value in ordered_dictionary.items():
        print(f"{key} {value}")
