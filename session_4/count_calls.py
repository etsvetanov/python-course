
def count_calls(func):

    count = []

    def inner(*args, **kwargs):
        # nonlocal count
        count.append(1)
        print('{} : {}'.format(func.__name__, count))
        return func(*args, **kwargs)

    return inner


@count_calls
def add(a, b):
    pass


@count_calls
def change_sign(a):
    pass


add(1, 2)
add(1, 2)

change_sign(1)
change_sign(2)
change_sign(21321321)

# print('Function {} has been called {} times'.format('add', add.count))
# print('Function {} has been called {} times'.format('change_sign', change_sign.count))