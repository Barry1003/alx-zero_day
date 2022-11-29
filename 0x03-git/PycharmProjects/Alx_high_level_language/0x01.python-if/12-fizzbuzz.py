def fizzbuzz():
    for num in range(1, 100):
        if ((num % 3) == 0) or ((num % 5 ) == 0):
            print("fizzbuzz")
        else:
            return num