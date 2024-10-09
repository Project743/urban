class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floors):
        if new_floors not in range(1, self.number_of_floors + 1):
            print('Такого этажа не сушествует.')
        else:
            count = 1
            while new_floors >= count:
                print(f'Вы поднялись на {count} этаж')
                count += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __it__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print(f'Объект {other} не подходит для сравнения с {self}')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        elif isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value.number_of_floors
        else:
            print(f'{value} не является целым числом, количество этажей не может быть увеличено на это значение')
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
        elif isinstance(value, House):
            self.number_of_floors = value.number_of_floors + self.number_of_floors
        else:
            print(f'{value} не является целым числом, количество этажей не может быть увеличено на это значение')
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        else:
            print(f'{value} не является целым числом, количество этажей не может быть увеличено на это значение')
        return self

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
