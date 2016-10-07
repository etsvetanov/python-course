items = [('apple', 'fruit'), ('oak', 'tree'), ('house', 'building')]

my_dict = {key: value for key, value in items}

print(my_dict)
print("my_dict['apple']:", my_dict['apple'])
print('type:', type(my_dict))


l = [(1, 'apples'), (2, 'bananas'), (3, 'oranges')]
d = {k * 10 : v.upper() for k, v in l
     if k % 2 == 1 and v.endswith('es')}
print(d)
# pimping the expression
# items = [('apple', 'fruit'), ('oak', 'tree'), ('house', 'building')]
#
# my_dict = {key + '1' : value.capitalize() for key, value in items}
#
# print(my_dict)
# print('type:', type(my_dict))