import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
res_1 = list(map(lambda x, y: x == y, first, second))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


if __name__ == '__main__':
    print(res_1)

    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
