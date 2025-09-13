import asyncio
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s %(threadName)s %(taskName)s [%(levelname)s] - %(message)s')

SIZE = 5
def gen():
    for i in range(SIZE):
        yield i
g = gen()
print(type(gen)) # <class 'function'>
print(type(g))   # <class 'generator'>
print(dir(g))
for e in gen():
    print(e)

while True:
    try:
        e = next(g)
        print(e)
    except StopIteration:
        break


