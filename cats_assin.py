import asyncio
import random


async def download_cat(n: int):
    print("Котенок ", n, "-ый начинает скачиваться", sep="")
    await asyncio.sleep(random.random() + 1)
    print("Котенок ", n, "-ый скачался", sep="")


async def async_main_cats():
    tasks = []
    for i in range(1, 11):
        tasks.append(download_cat(i))
    await asyncio.gather(*tasks)

asyncio.run(async_main_cats())
