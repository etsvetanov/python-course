def print_args(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

print_args(42, name='John', surname='Smith')