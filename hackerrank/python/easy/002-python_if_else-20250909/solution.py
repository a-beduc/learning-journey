if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 or n in set(range(6, 21)):
        print("Weird")
    else:
        print("Not Weird")
