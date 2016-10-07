class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


my_obj = MyClass('John')

my_obj.print_name()

MyClass.print_name(my_obj)