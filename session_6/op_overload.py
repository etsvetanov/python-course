class Length:
    def __init__(self, centimeters):
        self.length = centimeters

    def __add__(self, other):
        return (self.length + other.length)/100

l1 = Length(38)
l2 = Length(112)
print('Length in meters:', l1 + l2)