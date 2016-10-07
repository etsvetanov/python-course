
def even_validator(passed_function):

    def inner(*args, **kwargs):

        for key in kwargs:
            if not kwargs[key] % 2 == 0:
                print('Error, argument with value {} is not an even number!'.format(kwargs[key]))

        for arg in args:
            if not arg % 2 == 0:
                print('Error, argument with value {} is not an even number!'.format(arg))

        print('Before calling the passed function')
        return_value = passed_function(*args, **kwargs)
        print('After execute the passed function')

        if not return_value % 2 == 0:
            print('Error, return value ({}) is not an even number'.format(return_value))

        return return_value

    return inner


def add(a, b):
    return a + b

add = even_validator(add)


@even_validator
def change_sign(a):
    return -a


ret1 = add(3, b=4)
ret2 = change_sign(-8)
