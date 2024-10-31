import os
from datetime import datetime
import multiprocessing

directory = '../trades'


class VolatilityCalc(multiprocessing.Process):

    def __init__(self, file, queue):
        super().__init__()
        self.file = file
        self.queue = queue
        self.volatility, self.max_price, self.min_price = 0, 0, 0

    def run(self):
        with open(f'{directory}/{self.file}', 'r') as f:
            for line in f:
                price = line.split(',')[2]
                if price != 'PRICE':
                    price = float(price)
                    if self.max_price != 0 and self.max_price != 0:
                        if price > self.max_price:
                            self.max_price = price
                        elif price < self.min_price:
                            self.min_price = price
                    else:
                        self.max_price, self.min_price = price, price
        average_price = (self.max_price + self.min_price) / 2
        self.volatility = (self.max_price - self.min_price) / average_price * 100
        self.queue.put(self.volatility)



def main():
    zero_volatility = []
    dict_volatility = {}
    queue = multiprocessing.Queue()
    files = [file for file in os.listdir(directory)]
    proces = []
    for file in files:
        proc = VolatilityCalc(file, queue)
        proc.start()
        proces.append(proc)
        res = queue.get()
        if res == 0.0:
            zero_volatility.append(file)
        else:
            dict_volatility[file] = res
    print(zero_volatility)
    for proc in proces:
        proc.join()
    print('max volatility:')
    for _ in range(3):
        max_ = max(dict_volatility, key=dict_volatility.get)
        print(f'    {max_}   {dict_volatility[max_]:.2f}%')
        dict_volatility.pop(max_)
    print('min volatility:')
    for _ in range(3):
        min_ = min(dict_volatility, key=dict_volatility.get)
        print(f'    {min_}   {dict_volatility[min_]:.2f}%')
        dict_volatility.pop(min_)
    print('zero volatility:')
    print(' ' * 4, ', '.join(sorted(zero_volatility)))


if __name__ == '__main__':
    count = 100
    start_time = datetime.now()
    for _ in range(count):
        main()
    end_time = datetime.now()
    print((end_time - start_time) / count)
