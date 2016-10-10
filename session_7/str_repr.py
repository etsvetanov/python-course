class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        prefix = 'Sir' if self.gender is 'M' \
            else 'Madam'
        return prefix + ' ' + self.name

    def __repr__(self):
        return "Person('" + self.name + "')"

    def __len__(self):
        name_length = 0
        for char in self.name:
            name_length += 1

        return name_length

rob = Person('Robert', 'M')
print(rob)
print(len(rob))
#
#
#
# class Employee(Person):
#     def __init__(self, name, salary, position):
#         Person.__init__(self, name)
#         self.salary = salary
#         self.position = position
#
# john = Employee('John', '90000', 'Developer')
# john.print_name()