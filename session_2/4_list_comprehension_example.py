urls = ['google.com', 'abv.bg', 'python.org']

# list comprehensions do not have to use the current value from the iterable at all
my_list = [2 ** 4 for url in urls]

print(my_list)


# for url in urls:
#     print('tatatata')