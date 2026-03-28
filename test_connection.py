import asyncio
import aiohttp

async def test():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://api.telegram.org', timeout=10) as resp:
                print(f"✓ Успех! Статус: {resp.status}")
        except Exception as e:
            print(f"✗ Ошибка: {e}")

asyncio.run(test())