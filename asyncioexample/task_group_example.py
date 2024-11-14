import asyncio
from asyncio import Task
from asyncioexample.logger import LOGGER

async def say_after(delay:float, msg: str):
    LOGGER.info(f'{msg}')
    await asyncio.sleep(delay=delay)
    LOGGER.info(f'{msg}')


async def main():
    LOGGER.info("start...")
    async with asyncio.TaskGroup() as tg:
        task1:Task = tg.create_task(say_after(1,"hello"))
        task2:Task = tg.create_task(say_after(2,"world"))
        LOGGER.info("start-2...")
    LOGGER.info(f"end... {task1},{type(task1)} {task2}")

asyncio.run(main())
