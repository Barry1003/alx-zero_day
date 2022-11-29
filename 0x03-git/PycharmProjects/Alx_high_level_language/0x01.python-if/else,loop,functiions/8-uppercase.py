def uppercase(str):
        for letter in str:
            if letter in range((ord(str) >= 65 and ord(str) <= 90)):
                return uppercase(str)
            else:
                 return False


uppercase("best")
uppercase("Best School 98 Battery street")


#uncopleted project

#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[i]) - num), end='')
    print()