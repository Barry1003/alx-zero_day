for i in range(0, 9):
    for j in range(0, 10):
        if i < j and i != 8:
            print("{:d}{:d}, ".format(i, j), end="")

        #how to continue the progeram such that 89 wouldn't be printed out'