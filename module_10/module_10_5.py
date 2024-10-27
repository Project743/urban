from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    start_time = datetime.now()
    for file in filenames:
        read_info(file)
    end_time = datetime.now()
    print(f'{end_time - start_time}(линейный)')

    start1_time = datetime.now()
    with multiprocessing.Pool(len(filenames)) as p:
        p.map(read_info, filenames)
    end1_time = datetime.now()
    print(f'{end1_time - start1_time}(многопроцесный)')
