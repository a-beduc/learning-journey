from collections import deque


if __name__ == "__main__":
    N = int(input())
    d = deque()
    commands = {
        "append": d.append,
        "appendleft": d.appendleft,
        "pop": d.pop,
        "popleft": d.popleft
    }
    for _ in range(N):
        command, *value = input().split()
        func = commands[command]
        func(int(value[0])) if value else func()
    print(*d)


# Slower because getattr is quite slow.

# from collections import deque
#
#
# if __name__ == "__main__":
#     N = int(input())
#     d = deque()
#     for _ in range(N):
#         command = input().split(' ')
#         if len(command) > 1:
#             getattr(d, command[0])(int(command[1]))
#         else:
#             getattr(d, command[0])()
#     print(f"{' '.join(map(str, d))}")
