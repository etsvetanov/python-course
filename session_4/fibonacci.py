def fib(n):
    if n < 2:
        return [n]

    # return fib(n-1) + [fib(n-2)[-1] + fib(n-1)[-1]]
    res = fib(n-1)
    return fib(n-1) + [fib(n-2)[-1] + fib(n-1)[-1]]

print(fib(5))



