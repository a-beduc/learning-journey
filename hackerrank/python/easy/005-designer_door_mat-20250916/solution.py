def wrap(input_string, input_max_width):
    output_string = ""
    for i in range(0, len(input_string), input_max_width):
        output_string += f"{input_string[i:i + input_max_width]}\n"
    return output_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
