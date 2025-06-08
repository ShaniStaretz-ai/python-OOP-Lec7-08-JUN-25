def fibonaci(i):
    if i < 3:
        return 1
    return fibonaci(i - 2) + fibonaci(i - 1)


# return the fibonaci number in index i
print(fibonaci(8))
