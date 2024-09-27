immutable_var = (1, 'world', True, 5.5)
print('Immutable tuple:', immutable_var)
# immutable_var[0] = 10  # кортеж неизменяемый объект

mutable_list = [1, 'world', True, 5.5]
mutable_list[0] = 'new string'
print('Mutable list:', mutable_list)
