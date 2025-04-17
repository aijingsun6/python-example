import collections


class Cursor:
    buffer: collections.deque[int]
    max_size: int
    cur: int
    def __init__(self):
        self.buffer = collections.deque()
        self.max_size = 10
        self.cur = 0

    async def _prefetch(self):
        if self.cur < self.max_size:
            self.buffer.append(self.cur)
            self.cur += 1

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.buffer:
            await self._prefetch()
            if not self.buffer:
                raise StopAsyncIteration
        return self.buffer.popleft()

if __name__ == "__main__":
    c = Cursor()
    async for e in c:
        print(e)