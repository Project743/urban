from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


lst_1 = [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]
lst_2 = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]

time_start_0 = datetime.now()

for x in lst_1:
    write_words(*x)

time_end_0 = datetime.now()
print(f'Время поочередной записи: {time_end_0 - time_start_0}')

time_start_1 = datetime.now()

threads = []
for y in lst_2:
    thr = Thread(target=write_words, args=y)
    threads.append(thr)
    thr.start()

for thr in threads:
    thr.join()

time_end_1 = datetime.now()
print(f'Время записи в потоках: {time_end_1 - time_start_1}')
