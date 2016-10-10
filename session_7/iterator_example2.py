class MyIterator:
    def __init__(self, end):
        self.end = end
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            curr = self.current
            self.current += 1

            return curr


it = MyIterator(10)

for i in it:
    print(i)