import asyncio
import logging
import random

from aiolimiter import AsyncLimiter

requests_per_second = 45  # Оптимальное значение составляет 45-50. Если вы хотите, чтобы бот работал быстрее, можете увеличить это значение, но имейте в виду, что при более высоких значениях есть риск, что ваш бот будет попадать в рейтлимиты.
limiter = AsyncLimiter(requests_per_second + 1, 1.0185)

loop = asyncio.new_event_loop()


async def request(method, url, headers, json=None, return_json=False):
    async with limiter:
        resp = await method(url, headers=headers, json=json)
        if return_json and resp.status in [200, 201, 204]:
            return await resp.json()
        if resp.status == 429:
            resp_json = await resp.json()
            retry_after = resp_json["retry_after"]
            logging.warn(f"Мы впали в рейтлимиты. Ожидаю {retry_after}.")
            if float(resp_json["retry_after"]) < 15:
                await asyncio.sleep(resp_json["retry_after"])
                return await request(method, url, headers, json, return_json)


async def _wait_for_tasks_end():
    amount = requests_per_second
    if requests_per_second >= 50:
        amount -= 10

    while not limiter.has_capacity(amount):
        await asyncio.sleep(0.001)


async def create_tasks(urls, method, headers, json=None):
    if not urls:
        return

    random.shuffle(urls)
    tasks = []
    for i in range(0, len(urls), requests_per_second):
        current_urls = urls[i : requests_per_second + i]
        tasks += [
            asyncio.create_task(request(method, url, headers, json))
            for url in current_urls
        ]
        await asyncio.sleep(0.25)
        await _wait_for_tasks_end()

    await asyncio.wait(tasks)
