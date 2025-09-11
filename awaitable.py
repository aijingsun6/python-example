import asyncio

async def my_coroutine():
    print("Start")
    s = asyncio.sleep(1)
    print(s)
    print(type(s))
    await s  # Pause for 1 second
    print("End")

async def main():
    task = asyncio.create_task(my_coroutine())
    print(task)
    print(type(task))
    await task  # Wait for the task to complete


async def main2():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Simulate setting a result after 1 second
    async def set_result():
        print("Start")
        await asyncio.sleep(1)
        print("End")
        future.set_result("Done!")

    asyncio.create_task(set_result())
    result = await future  # Waits until result is set
    print(result)


asyncio.run(main())
asyncio.run(main2())