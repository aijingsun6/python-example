import asyncio
import logging
import types
logger = logging.getLogger(__name__)

async def read_data():
    print("before sleep")
    await asyncio.sleep(5)
    print("after sleep")

@types.coroutine
def process_data():
    data = yield from read_data()
    print(data)

if __name__ == '__main__':
    asyncio.run(process_data())