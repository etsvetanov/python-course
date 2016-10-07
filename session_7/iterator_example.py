class MyList:
    def __init__(self, l=None):
        self.index = 0
        if l:
            self.l = l
        else:
            self.l = []

    def add(self, item):
        self.l.append(item)

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.l * 2)

    def __next__(self):
        if self.index >= len(self.l):
            raise StopIteration
        else:
            item = self.l[self.index]
            self.index += 1
            return item

    def __str__(self):
        return "I am a MyList object"






my_list = MyList([1, 2, 3])