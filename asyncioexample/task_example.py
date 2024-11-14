import asyncio
import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(filename)s %(funcName)s %(message)s")
logger = logging.getLogger(__name__)

async def say_after(delay:float, msg: str):
    logger.info("start say {}".format(msg))
    await asyncio.sleep(delay=delay)
    logger.info("end say {}".format(msg))

async def main():
    logger.info("start...")
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    await task1
    await task2
    logger.info("end...")

if __name__ == '__main__':
    asyncio.run(main())