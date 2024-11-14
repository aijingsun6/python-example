from asyncioexample.logger import LOGGER
import asyncio
async def long_running_task(delay:float):
    LOGGER.info("start...")
    await asyncio.sleep(delay)
    LOGGER.info("end...")

async def main():
    LOGGER.info("start...")
    try:
        async with asyncio.timeout(5):
            await long_running_task(10)
    except TimeoutError as e:
        print(e)
    LOGGER.info("end...")

asyncio.run(main())
