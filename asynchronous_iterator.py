import asyncio
import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO, format='%(asctime)s %(threadName)s %(taskName)s [%(levelname)s] - %(message)s')


class AsyncIterable:
    data: list
    cursor: int

    def __init__(self, size):
        self.data = list(range(size))
        self.cursor = 0

    def __aiter__(self):
        logging.info('__aiter__ called.')
        self.cursor = 0
        return self

    async def __anext__(self):
        logging.info(f'__anext__ called, cursor={self.cursor}')
        if self.cursor < len(self.data):
            data = self.data[self.cursor]
            self.cursor += 1
            return data
        else:
            raise StopAsyncIteration

async def hello():
    # 必须要放在携程函数里
    iterator = AsyncIterable(5)
    async for e in iterator:
        logging.info(e)

asyncio.run(hello())



