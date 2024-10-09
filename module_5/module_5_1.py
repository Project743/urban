class House:
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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
