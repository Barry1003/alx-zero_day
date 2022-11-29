import random
number = random.randint(-10, 10)
# to check if a number is positive or negative


if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is negative".format(number))
elif number < 0:
    print("{:d} is negative".format(number ))