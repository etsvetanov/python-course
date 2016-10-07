my_list = ['dog', 'cat', 'donkey', 'frog', 'rabbit', 'bird', 'donkey']

my_list.append('pig')
print(my_list)

my_list.extend(['beaver', 'mouse'])
print(my_list)

my_list.insert(3, 'spider')
print(my_list)

a = my_list.pop()
print(my_list)

b = my_list.remove('donkey')
print(my_list)

my_list.sort()
print('The sorted list:', my_list)

print('Is there a pig in my list? -', 'pig' in my_list)
print('My list has a length of:', len(my_list))
