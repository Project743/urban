class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor not in range(1, self.number_of_floor + 1):
            print('Такого этажа не сушествует.')
        else:
            count = 1
            while new_floor >= count:
                print(f'Вы поднялись на {count} этаж')
                count += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
