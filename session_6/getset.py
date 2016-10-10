class MyClass:
    def __init__(self, arg):
        self.attrib = arg

    @property
    def attrib(self):
        return self.__attrib

    @attrib.setter
    def attrib(self, arg):
        self.__attrib = arg


my_instance = MyClass('Hello')
my_instance.attrib = 'World'

print(my_instance.attrib)
print('bla')