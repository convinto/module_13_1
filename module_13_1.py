import asyncio

async def start_strongman(name, power):
    konstant = 5                                    #переменная для установления константы в обратной пропорциональности
    print(f'Силач {name} начал соревнования.')
    for number_ball in range(1, 6):                 #определяем в цикле количество шаров для участника
        await asyncio.sleep(t:=konstant/power)               #устанавливаем время задержки, обратно пропорциональное силе
        print(f'Силач {name} поднял {number_ball}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))        #формирование задачи№1
    task2 = asyncio.create_task(start_strongman('Denis', 4))        #формирование задачи№2
    task3 = asyncio.create_task(start_strongman('Apollon', 5))      #формирование задачи№3
    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(start_tournament())     #запуск программы через метод run
