# # 01 My naive subpar solution

# if __name__ == "__main__":
#     k = int(input())
#     keys = list(map(int, input().split()))
#     possible = set(keys)
#     found = set()
#     for key in keys:
#         if key in found:
#             possible.discard(key)
#         found.add(key)
#     print(possible.pop())


# # Counter solution

# from collections import Counter
#
# if __name__ == "__main__":
#     k = int(input())
#     keys = list(map(int, input().split()))
#     counts = Counter(keys)
#     print(next(k for k, c in counts.items() if c == 1))


# Mathematics approach (see notes for explanation)

if __name__ == "__main__":
    k = int(input())
    keys = list(map(int, input().split()))
    captain_key = (k * sum(set(keys)) - sum(keys)) // (k - 1)
    print(captain_key)
