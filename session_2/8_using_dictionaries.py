
my_dict = {'name': 'John', 'position': 'QA', 'workplace': 102}

my_dict['project'] = 'Bonanza'
print(my_dict)

del my_dict['position']
print(my_dict)

item = my_dict.get(key='position', default='New York')
print(item)

my_dict.update([('address', 'Chicago'), ('salary', 70000)])
print(my_dict)

length = len(my_dict)
print('length:', length)

print('Is there an "address" key in my_dict?', 'address' in my_dict)

for key in my_dict:
    print(key, ':',  my_dict[key])
