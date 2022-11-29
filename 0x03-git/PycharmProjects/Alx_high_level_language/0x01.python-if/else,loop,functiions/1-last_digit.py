import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    print("The last digit of {} is greater than 5".format(number % 10))
elif (number % 10 < 6) and (number % 10 != 0):
    print("The last digit of {} is less than 6 and 0".format(number % 10))
elif number % 10 == 0:
    print("The last digit {} is zero".format(number % 10))