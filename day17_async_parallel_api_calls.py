import asyncio
import time

async def fetch_user_data(user_id):
    print(f"Fetching data for user {user_id}...")
    await asyncio.sleep(2)
    print(f"Got data for user {user_id}")
    return {"user_id": user_id, "name": f"User{user_id}"}

async def main():
    start = time.time()
    
    users = [1, 2, 3, 4, 5]
    results = await asyncio.gather(*[fetch_user_data(uid) for uid in users])
    
    end = time.time()
    print(results)
    print(f"Total time: {end - start}")

asyncio.run(main())