if __name__ == "__main__":
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    sym_diff = "\n".join(map(str, sorted(list(a.symmetric_difference(b)))))
    print(sym_diff)
