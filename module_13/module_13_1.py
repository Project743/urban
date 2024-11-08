import asyncio


async def start_storngman(name, power):
    print(f'Силач {name} начал соревнования')
    ball = 1
    while ball <= 5:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball} шар')
        ball += 1
    print(f'Силач {name} закончил соревнования.')


async def main():
    # task1 = asyncio.create_task(start_storngman('Pasha', 3))
    # task2 =  asyncio.create_task(start_storngman('Denis', 4))
    # task3 =  asyncio.create_task(start_storngman('Apollon', 5))
    # await task1
    # await task2
    # await task3
    strongman_list = [('Pasha', 3), ('Denis', 4), ('Apollon', 5)]
    tasks = []
    for man in strongman_list:
        tasks.append(asyncio.create_task(start_storngman(*man)))
    for task in tasks:
        await task


if __name__ == '__main__':
    asyncio.run(main())
