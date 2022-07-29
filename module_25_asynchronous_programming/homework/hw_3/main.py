from pathlib import Path
from time import time

import aiofiles
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import validators

# start_url = 'http://www.aclweb.org/anthology/'
start_url = 'http://evklid.makdu-skillbox.tmweb.ru/'
OUT_PATH = Path(__file__).parent / 'url'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()
url_list = [start_url]
links = set()


async def write_to_disk(content):
    file_path = "{}/url.text".format(OUT_PATH)
    async with aiofiles.open(file_path, mode='a') as f:
        await f.write(content)


def parse_for_links(url, text):

    soup = BeautifulSoup(text, "html.parser")
    tags = soup.findAll('a', href=True)

    def_url = url.split('/')[0] + '//' + url.split('/')[2]

    return [urljoin(url, tag['href']) for tag in tags
            if not urljoin(url, tag['href']).startswith(def_url) and '@'
            not in urljoin(url, tag['href']) and validators.url(urljoin(url, tag['href']))]


async def fetch_async(url, depth=3):
    global url_list_recursive
    url_list_recursive = []
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as session:
            async with session.get(url) as resp:
                for link in parse_for_links(url, await resp.text()):

                    if link not in links:
                        links.add(link)
                        url_list_recursive.append(link)
                if depth > 0:
                    for item in url_list_recursive:
                        await write_to_disk(item + '\n')
                        await fetch_async(item, depth=depth - 1)
                    url_list_recursive.clear()
    except:
        pass


async def wrap_tasks(urls_list: list):
    tasks = []
    for url in urls_list:
        tasks.append(asyncio.ensure_future(fetch_async(url)))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time()
    asyncio.run(wrap_tasks(url_list))
    print(f'Время выполнения: {round((time() - start_time) / 60, 2)} min')
