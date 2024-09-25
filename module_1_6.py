my_dict = {'Pavel': 1988, 'Elena': 1986, 'Egor': 1991, 'Sergei': 1995, 'Antonina': 1990}
print('Dict:', my_dict)
print('Existing value:', my_dict['Egor'])
print('Not existing value:', my_dict.get('Semen'))
my_dict.update({'Semen': 2000,
                'Oleg': 1999})
print('Deleted value:', my_dict.pop('Sergei'))
print('Modified dictionary:', my_dict)

print('--------------------------------------------------')  # строка для разделения заданий

my_set = {9, 0, 'test', True, 'aple', 3, 'aple', 7, 25, 9, 1, False, 0}
print(my_set)
my_set.update({'coconut', 5})
my_set.discard(25)
print(my_set)
