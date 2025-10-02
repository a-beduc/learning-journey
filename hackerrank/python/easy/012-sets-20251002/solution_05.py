if __name__ == "__main__":
    n = int(input())
    sample_n = set(map(int, input().split()))
    b = int(input())
    sample_b = set(map(int, input().split()))
    print(len(sample_n.intersection(sample_b)))
