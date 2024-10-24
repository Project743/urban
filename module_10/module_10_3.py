from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            repl_balance = randint(50, 500)
            self.balance = self.balance + repl_balance
            print(f'Пополнение: {repl_balance}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for _ in range(100):
            rem_balance = randint(50, 500)
            print(f'Запрос на {rem_balance}')
            if rem_balance <= self.balance:
                self.balance = self.balance - rem_balance
                print(f'Снятие: {rem_balance}. Баланс: {self.balance}')
                sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
