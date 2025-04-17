import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    return 1

print(main) # <function main at 0x000002769CAFA200>
print(main()) # <coroutine object main at 0x000002769EA55300>
if __name__ == '__main__':
    print(asyncio.run(main()))