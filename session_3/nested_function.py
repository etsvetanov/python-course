def do(f, x, y):
    res = f(x, y)
    return res

def add(a, b):
    return a + b

result = do(add, 5, 10)
