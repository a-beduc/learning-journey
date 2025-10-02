def average(array):
    set_a = set(array)
    return round(sum(set_a) / len(set_a), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
