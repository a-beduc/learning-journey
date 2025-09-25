def minion_game(string):
    kevin = 0
    stuart = 0
    for idx, letter in enumerate(string):
        if letter in {"A", "E", "I", "O", "U"}:
            kevin += len(string) - idx
        else:
            stuart += len(string) - idx
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
