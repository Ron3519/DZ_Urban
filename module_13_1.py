
import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
            await asyncio.sleep(10 - power)
            print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    sm1 = asyncio.create_task(start_strongman('Pasha', 3))
    sm2 = asyncio.create_task(start_strongman('Denis', 4))
    sm3 = asyncio.create_task(start_strongman('Apollon', 5))
    await sm1
    await sm2
    await sm3

asyncio.run(start_tournament())
