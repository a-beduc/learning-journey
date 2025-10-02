def process(number, data):
    commands = {
        "intersection_update": data.intersection_update,
        "update": data.update,
        "symmetric_difference_update": data.symmetric_difference_update,
        "difference_update": data.difference_update,
    }
    for _ in range(number):
        command, *_ = input().split()
        input_set = set(map(int, input().split()))
        func = commands[command]
        func(input_set)
    print(sum(data))


if __name__ == "__main__":
    len_a = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    process(n, a)
