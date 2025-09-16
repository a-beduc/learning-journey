# Enter your code here. Read input from STDIN. Print output to STDOUT

def welcome_line(m):
    return "WELCOME".center(m, "-")


def cone_block(n, m):
    return [(i * ".|.").center(m, "-") for i in range(1, n - 1, 2)]


if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    wel = welcome_line(M)
    cone = cone_block(N, M)
    top_cone = '\n'.join(cone)
    cone.reverse()
    bot_cone = '\n'.join(cone)
    doormat = '\n'.join([top_cone, wel, bot_cone])
    print(doormat)
