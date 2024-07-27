import asyncio
import json

from aiohttp import ClientSession


class Data:

    def __init__(self, url: str) -> None:
        self.url = url

    async def get_data(self):
        async with ClientSession() as session:
            async with session.get(self.url) as response:
                with open('data.json', 'w') as file:
                    json.dump(await response.json(), file)


data = Data(
    url='https://jsonplaceholder.typicode.com/posts'
)
asyncio.run(data.get_data())
