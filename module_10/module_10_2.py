from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        self.power = power
        self.enemy = 100
        super().__init__(name=name)

    def run(self):
        count_day = 0
        print(f'{self.name}, на нас напали')
        while self.enemy > 0:
            count_day += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {count_day} дней, осталось {self.enemy} войнов')
            sleep(1)
        print(f'{self.name} одержал победу спустя {count_day}дней')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    list_knight = [first_knight, second_knight]

    threads = []
    for knight in list_knight:
        thread = knight
        sleep(0.01)  # задержка что бы разные потоки не выводили информацию в одну строку
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('Все битвы закончились!')
