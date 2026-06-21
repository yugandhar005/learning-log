import asyncio
import time


# ===== Sequential (await one by one) =====
async def make_tea():
    print("Boiling water...")
    await asyncio.sleep(3)
    print("Tea ready!")


async def make_toast():
    print("Toasting bread...")
    await asyncio.sleep(2)
    print("Toast ready!")


async def main_sequential():
    start = time.time()
    await make_tea()
    await make_toast()
    end = time.time()
    print(f"Sequential Total time: {end - start}")


asyncio.run(main_sequential())


# ===== Parallel (asyncio.gather) =====
async def main_parallel():
    start = time.time()
    await asyncio.gather(make_tea(), make_toast())
    end = time.time()
    print(f"Parallel Total time: {end - start}")


asyncio.run(main_parallel())
