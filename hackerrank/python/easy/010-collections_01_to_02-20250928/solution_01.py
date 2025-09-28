from collections import Counter


def main():
    X = int(input())
    shoe_stock = Counter(map(int, input().split()))
    N = int(input())
    total = 0
    for _ in range(N):
        shoe_size, price = [int(i) for i in input().split()]
        if shoe_stock[shoe_size]:
            total += price
            shoe_stock[shoe_size] -= 1
    print(total)


if __name__ == "__main__":
    main()
