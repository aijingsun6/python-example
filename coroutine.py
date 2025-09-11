import logging
import sys
import asyncio
logging.basicConfig(stream=sys.stdout,level=logging.INFO, format='%(asctime)s %(threadName)s %(taskName)s [%(levelname)s] - %(message)s')


async def hello_coroutine(ret):
    logging.info('before sleep')
    await asyncio.sleep(1)
    logging.info('after sleep')
    return ret

# cor = hello_coroutine(123)
# logging.info(f'hello_coroutine is iscoroutinefunction: {asyncio.iscoroutinefunction(hello_coroutine)}')
# logging.info(f'hello_coroutine() is iscoroutine: {asyncio.iscoroutine(cor)}')
# logging.info(f'object:{cor}, class: {type(cor)}')
#
# res = asyncio.run(cor)
# logging.info(f'result: {res}')

async def delay_print(value, sleep):
    await asyncio.sleep(sleep)
    logging.info(value)


async def multi_print():
    await asyncio.gather(delay_print('1',1),delay_print('2',2),delay_print('3',3))

# asyncio.run(multi_print())


async def timeout_print(value, sleep):
    logging.info(f'before print {value}')
    await asyncio.sleep(sleep)
    logging.info(f'after print {value}')


async def timeout_demo():
    try:
        await asyncio.wait_for(timeout_print('value', 2), timeout=1.0)
    except asyncio.TimeoutError:
        logging.info('timeout!')

# asyncio.run(timeout_demo())

async def timeout_demo_2():
    try:
        async with asyncio.timeout(1.0):
            await timeout_print('value', 2)
    except asyncio.TimeoutError:
        logging.info('timeout!')
# asyncio.run(timeout_demo_2())