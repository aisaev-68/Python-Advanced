import asyncio
import random
from pprint import pprint
from typing import List, Dict, Any

import aiohttp


async def get_data(client: aiohttp.ClientSession, url: str) -> dict:
    async with client.get(url) as response:
        result = await response.json()
        return result


async def get_users(url: str) -> list:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_data(client, url) for _ in range(10)]
        result = await asyncio.gather(*tasks)

        list_user = []
        id = 1
        for user in result:
            addr = user['address']
            address = {"country": addr['country'], "city": addr['city'],
                       "street_name": addr['street_name'], "street_address": addr['street_address'],
                       "state": addr['state'], "zip_code": addr['zip_code']}
            has_sale = random.choice([True, False])
            coffee_id = random.choice(list(range(1, 11)))
            dict_user = {'id': id, 'name': f"{user['first_name']} {user['last_name']}",
                         'has_sale': has_sale, 'address': address,
                         'coffee_id': coffee_id}
            list_user.append(dict_user)
            id += 1

        return list_user


async def get_coffees(url: str) -> list:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_data(client, url) for _ in range(10)]
        result = await asyncio.gather(*tasks)

        list_coffee = []
        id = 1
        for coffee in result:
            dict_coffee = {'id': id, 'title': coffee['blend_name'],
                           'origin': f"{coffee['origin']}",
                           'intensifier': coffee['intensifier'],
                           'notes': [c.strip() for c in coffee['notes'].split(',')]}
            list_coffee.append(dict_coffee)
            id += 1

        return list_coffee


def main() -> dict:
    dict_data = {}
    url_user = 'https://random-data-api.com/api/users/random_user'
    url_coffee = 'https://random-data-api.com/api/coffee/random_coffee'
    dict_data['user'] = asyncio.run(get_users(url_user))
    dict_data['coffees'] = asyncio.run(get_coffees(url_coffee))
    return dict_data
