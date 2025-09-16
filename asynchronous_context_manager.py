import asyncio
import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO, format='%(asctime)s %(threadName)s %(taskName)s [%(levelname)s] - %(message)s')

async def sleep_print(value=None,secs=1):
    await asyncio.sleep(secs)
    return value

class AsyncContextManager:

    def __init__(self,value='AsyncContextManager'):
        self.value = value

    async def __aenter__(self,):
        logging.info('__aenter__')
        return await sleep_print(self.value)

    async def __aexit__(self, exc_type, exc, tb):
        logging.info(f'__aexit__ {exc_type} {exc} {tb}')
        await sleep_print('__aexit__')

async def hello():
    async with AsyncContextManager() as acm:
        logging.info(f'with {acm}')

asyncio.run(hello())