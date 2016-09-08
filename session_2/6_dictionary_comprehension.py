items = [('apple', 'fruit'), ('oak', 'tree'), ('house', 'building')]

my_dict = {key : value for key, value in items}

print(my_dict)
print("my_dict['apple']:", my_dict['apple'])
print('type:', type(my_dict))


# pimping the expression
# items = [('apple', 'fruit'), ('oak', 'tree'), ('house', 'building')]
#
# my_dict = {key + '1' : value.capitalize() for key, value in items}
#
# print(my_dict)
# print('type:', type(my_dict))