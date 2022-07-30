import aiohttp
import aiofiles
import asyncio
from bs4 import BeautifulSoup
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = "https://stackoverflow.com"
DEPTH = 3


async def get_link(client: aiohttp.ClientSession, url: str, depth: int = DEPTH) -> None:
    async with client.get(url) as response:
        try:
            result = await response.text()
            soup = BeautifulSoup(result, 'html.parser')

            for link in soup.find_all('a'):
                link_str = link.get('href')
                logger.info(f'depth-{depth}, link-{link_str}')
                if link_str is not None and link_str.startswith("http"):
                    await write_to_file(link_str)
                    if depth > 0:
                        await get_link(client, link_str, depth - 1)
        except UnicodeDecodeError as err:
            logger.error(err)


async def write_to_file(content: str):
    async with aiofiles.open('links_db.txt', mode='a') as f:
        await f.write(content + '\n')


async def get_all_htmls(*url):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        htmls = [get_link(client, i_url) for i_url in url]
        return await asyncio.gather(*htmls)


def main(*url):
    asyncio.run(get_all_htmls(*url))


if __name__ == '__main__':
    main(URL)

