from collections import defaultdict


def main(a, m):
    d = defaultdict(list)
    for idx, word in enumerate(a, 1):
        d[word].append(str(idx))

    output_block = []

    for _ in range(m):
        word = input()
        target = d.get(word)
        if target:
            line = ' '.join(target)
        else:
            line = "-1"
        output_block.append(line)

    print("\n".join(output_block))


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input())
    main(A, M)
