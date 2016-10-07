class MyClass:
    class_attr = 'This is a class attribute'

    def __init__(self, value):
        self.instance_attr = value


my_instance1 = MyClass('This is an instance attribute')
my_instance2 = MyClass('This is another instance attribute')

print('MyClass __dict__', MyClass.__dict__)
print('my_instance1 __dict__', my_instance1.__dict__)
print('my_instance2 __dict__', my_instance2.__dict__)

print('my_instance1.class_attr', my_instance1.class_attr)
print('my_instance2.class_attr', my_instance2.class_attr)

MyClass.class_attr = 'The class attribute has changed'

print('my_instance1.class_attr', my_instance1.class_attr)
print('my_instance2.class_attr', my_instance2.class_attr)

my_instance1.class_attr = 'We want to set the class attribute to new value'

print('MyClass.class_attr', MyClass.class_attr)
print('my_instance1.class_attr', my_instance1.class_attr)
print('my_instance2.class_attr', my_instance2.class_attr)

