def my_func(some_obj):
    print('The object name is: {}'.format(some_obj.name))


class MyClass:
    pass


MyClass.my_method = my_func

my_obj = MyClass()
my_obj.name = 'Zoidberg'

MyClass.my_method(my_obj)

my_obj.my_method()