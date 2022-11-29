# Function that prints the first n elements of a fibonnacci series
def fib(n):
    a = 0
    b = 1
    c = 1
    while c <= n:
        print(a, end=', ')
        a, b = b, a+b
        c += 1
fib(20)