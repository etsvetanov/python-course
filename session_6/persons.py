
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def print_name(self):
        prefix = 'Sir' if self.gender is 'M' else 'Madam'
        print('{prefix} {name}'.format(prefix=prefix, name=self.name))

class Employee(Person):
    def __init__(self, name, salary, position):
        Person.__init__(self, name)
        self.salary = salary
        self.position = position

john = Employee('John', '90000', 'Developer')
john.print_name()


class Manager(Employee):
    def increase_salary(self):
        self.salary *= 2


gosho = Employee(name='Gosho', salary=5000, position='QA')
print("Gosho's salary:", gosho.salary)
gosho.increase_salary()
print("Gosho's salary:", gosho.salary)

manager = Manager(name="Meringey", salary=10000, position='Manager')
print("Manager's salary:", manager.salary)
manager.increase_salary()
print("Manager's salary:", manager.salary)


l = [gosho, manager]

for employee in l:
    employee.increase_salary()