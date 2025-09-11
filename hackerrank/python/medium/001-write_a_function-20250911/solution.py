def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True

    if leap and not year % 400:
        pass
    elif leap and not year % 100:
        leap = False
    else:
        pass

    return leap

