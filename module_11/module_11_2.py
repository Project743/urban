def introspection_info(obj):
    dict_data = {'type': type(obj).__name__}
    if hasattr(obj, '__module__'):
        dict_data['module'] = getattr(obj, '__module__')
    dict_data['attributes'] = [attr for attr in dir(obj) if
                               not callable(getattr(obj, attr)) and not attr.startswith('__')]
    dict_data['methods'] = [method for method in dir(obj) if
                            callable(getattr(obj, method)) and not method.startswith('__')]
    return dict_data


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floors):
        if new_floors not in range(1, self.number_of_floors + 1):
            print('Такого этажа не существует.')
        else:
            count = 1
            while new_floors >= count:
                print(f'Вы поднялись на {count} этаж')
                count += 1


h1 = House('ЖК Горский', 18)

s = 'lst'
number_info = introspection_info(h1)
print(number_info)
