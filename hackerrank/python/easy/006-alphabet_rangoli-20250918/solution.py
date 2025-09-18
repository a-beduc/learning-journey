def letters(size):
    return [chr(number) for number in range(97, 97 + size)]


def process_text(size, list_letters):
    cone = []
    line_length = 4 * size - 3
    for i in range(1, size + 1):
        # [-1:-i:-1] start at the last element, stop at -i, in reverse
        #   >>> [e, d]
        # [-i:] start at -i element, normal order >>> [c, d, e]
        # together >>> [e, d, c, d, e]
        line_letters = list_letters[-1:-i:-1] + list_letters[-i:]
        cone.append("-".join(line_letters).center(line_length, "-"))
    reversed_cone = cone[::-1]
    return "\n".join([*cone, *reversed_cone[1::]])


def print_rangoli(size):
    list_letters = letters(size)
    text = process_text(size, list_letters)
    print(text)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
