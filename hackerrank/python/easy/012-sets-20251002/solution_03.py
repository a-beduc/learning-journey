def process(number, data):
    commands = {
        "pop": data.pop,
        "remove": data.remove,
        "discard": data.discard
    }
    for _ in range(number):
        command, *value = input().split()
        func = commands[command]
        func(int(value[0])) if value else func()
    print(sum(data))


if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    c = int(input())
    process(c, s)
