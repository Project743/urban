def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3, 'Hello', False]
values_dict = {'a': 77, 'b': 'world', 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['coconut', 3.51]
print_params(*values_list_2, 42)
