def print_formatted(number):
    output = []
    # minus two to get rid of the lenght added by the "0b" in "0b<binary>"
    space = len(str(bin(number))) - 2
    for i in range(1, number + 1):
        items = [
            str(i),
            str(oct(i))[2:],
            str(hex(i))[2:].upper(),
            str(bin(i))[2:]
        ]
        output.append(' '.join(map(lambda x: x.rjust(space, ' '), items)))

    print(f"{'\n'.join(output)}")
