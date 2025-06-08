def fibonaci(i):
    if i < 3:
        return 1
    return fibonaci(i - 2) + fibonaci(i - 1)


# return the fibonaci number in index i
print(fibonaci(8))

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def print_fib_series(i, n):
    if i > n:
        return
    print(fib(i), end=" ")
    print_fib_series(i + 1, n)

print_fib_series(1, 5)

