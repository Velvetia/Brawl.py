import aiohttp
import asyncio
import json
from . import errors

base_endpoint = 'https://api.brawlhalla.com'

class Client:
    # It'd possibly be easier here if you had to set your API key before using
    # the class, like so:
    # brawl = brawlpy.Client(key='examplekey')
    def __init__(self, key: str = None, second=10, fivemin=180):
        # As of Febuary 23, 2017, the amount of requests you can use per second
        # is 10. The amount of requests you can use per 5 minutes is 180.
        self.key = key
        self.second = second
        self.fivemin = fivemin
        self.base_endpoint = base_endpoint
        self.session = aiohttp.ClientSession()
        self.key_param = {'api_key' : self.key}
        # I'm not quite sure how to correctly implement this, however...
        # I'm thinking maybe set a var for calls, and increment that by one for each usage?


    async def get_user_id(self, steam: str):
        """Gets the user's most recent gameplay name and their Brawlhalla ID.
        Params: steam = String of a user's Steam ID64."""
        param = {'steamid' : steam, 'api_key' : self.key}
        async with self.session.get('{}/search/'.format(self.base_endpoint), params=param) as resp:
            return await resp.json()

    async def get_user_stats(self, brawlid: str):
        """Gets gameplay stats for a user.
        Params: brawlid = String of user's Brawlhalla ID. Found using get_user_id."""
        async with self.session.get('{}/player/{}/stats'.format(self.base_endpoint, brawlid), params=self.key_param) as resp:
            return await resp.json()

    async def get_rank_stats(self, brawlid: str):
        """Gets ranked stats for a user.
        Params: brawlid = String of user's Brawlhalla ID. Found using get_user_id."""
        async with self.session.get('{}/player/{}/ranked'.format(self.base_endpoint, brawlid), params=self.key_param) as resp:
            return await resp.json()

    async def get_clan_stats(self, clanid: str):
        """Retrieves stats on a clan.
        Params: clanid = String of clan ID. Can be found using get_user_stats."""
        async with self.session.get('{}/clan/{}'.format(self.base_endpoint, clanid), params=self.key_param) as resp:
            return await resp.json()

    async def get_legend_info(self, legend: str):
        """Gets info about a legend based on it's ID.
        Params: legend = String of legend number. Starts at 3 (Bodvar)."""
        async with self.session.get('{}/legend/{}'.format(self.base_endpoint, legend), params=self.key_param) as resp:
            return await resp.json()
