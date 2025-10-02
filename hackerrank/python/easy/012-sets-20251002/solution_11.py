if __name__ == "__main__":
    a = set(map(int, input().split()))
    n = int(input())
    output = []
    for _ in range(n):
        b = set(map(int, input().split()))
        output.append(a.issuperset(b))
    print(all(output))
