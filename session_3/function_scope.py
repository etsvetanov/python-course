a = 10

def func():
    a = 5
    print('locals:', locals())

func()

print('globals:', globals())