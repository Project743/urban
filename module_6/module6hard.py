class Figure:
    side_count = 0

    def __init__(self, color, *sides):
        self.__sides = None
        self.__sides = sides
        self.__color = color
        self.filled = bool

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == len(self.__sides):
            for item in sides:
                if item < 0 or not isinstance(item, int):
                    return False
            return True

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):

        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    side_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.side_count:
            sides = [1] * self.side_count

        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * 3.1415)

    def get_square(self):
        return self.get_sides()[0] * 2 / (4 * 3.1415)


class Triangle(Figure):
    side_count = 3

    def __init__(self, color, *sides):
        if (len(sides) != self.side_count
                or sides[0] + sides[1] < sides[2]
                or sides[1] + sides[2] < sides[0]
                or sides[0] + sides[2] < sides[1]):
            sides = [1] * self.side_count
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = 1 / 2 * (a + b + c)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s


class Cube(Figure):
    side_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1] * self.side_count
        super().__init__(color, *(sides * self.side_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    print(f'стороны созданного круга: {circle1.get_sides()}')
    print(f'цвет созданного круга: {circle1.get_color()}')
    cube1 = Cube((222, 35, 130), 6)
    print(f'стороны созданного куба: {cube1.get_sides()}')
    print(f'цвет созданного куба: {cube1.get_color()}')
    triagle1 = Triangle((250, 200, 180), 4, 7, 1)
    # треугольник создается со сторонами 1*1*1 -> одна из указаных сторон больше суммы двух других
    print(f'стороны созданного треугольника: {triagle1.get_sides()}')
    print(f'цвет созданного треугольника: {triagle1.get_color()}')

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(f'цвет круга после попытки его изменить: {circle1.get_color()}')
    cube1.set_color(300, 70, 15)  # Не изменится
    print(f'цвет куба после попытки его изменить: {cube1.get_color()}')

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(f'стороны куба после попытки их изменить: {cube1.get_sides()}')
    triagle1.set_sides(5, 3, 7)  # изменится
    print(f'стороны треугольника после попытки их изменить: {triagle1.get_sides()}')
    circle1.set_sides(15)  # Изменится
    print(f'сторона круга после попытки её изменить: {circle1.get_sides()}')

    # Проверка периметра:
    print(f'периметр круга: {len(circle1)}')
    print(f'периметр треугольника: {len(triagle1)}')
    print(f'периметр куба: {len(cube1)}')

    # Проверка объёма (куба):
    print(f'объём куба: {cube1.get_volume()}')
    # Проверка площадь (круга):
    print(f'площадь круга: {circle1.get_square():.4f}')
    # Проверка площадь (треугольника):
    print(f'площадь треугольника: {triagle1.get_square():.4f}')
