class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1


if __name__ == "__main__":
    x = C()
    print("Number of instances: : ", str(C.counter))
    y = C()
    print("Number of instances: : ", str(C.counter))
