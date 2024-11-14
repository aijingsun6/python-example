import asyncio
import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(filename)s %(funcName)s %(message)s")
logger = logging.getLogger(__name__)

async def say_after(delay:float, msg: str):
    await asyncio.sleep(delay=delay)
    logger.info(msg)

async def main():
    logger.info("start...")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    logger.info("end...")

if __name__ == '__main__':
    asyncio.run(main())
