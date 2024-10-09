class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print('Такого этажа не сушествует.')
        else:
            count = 1
            while new_floor >= count:
                print(f'Вы поднялись на {count} этаж')
                count += 1

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __it__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor = self.number_of_floor + value
        else:
            print(f'{value} не является целым числом, количество этажей не может быть увеличено на это значение')
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floor = value + self.number_of_floor
        else:
            print(f'{value} не является целым числом, количество этажей не может быть увеличено на это значение')
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        else:
            print(f'{value} не является целым числом, количество этажей не может быть увеличено на это значение')
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
