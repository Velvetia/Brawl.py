import aiohttp
import asyncio
import json


class Client:
    # It'd possibly be easier here if you had to set your API key before using
    # the class, like so:
    # brawl = Brawlthon.Brawlthon(key="examplekey")
    def __init__(self, key: str = None, second=10, fivemin=180):
        # As of Febuary 23, 2017, the amount of requests you can use per second
        # is 10. The amount of requests you can use per 5 minutes is 180.
        self.key = key
        self.second = second
        self.fivemin = fivemin
        # I'm not quite sure how to correctly implement this, however...
        # I'm thinking maybe set a var for calls, and increment that by one for each usage?

    async def get_user_id(self, steam: str):
        """Finds the user's current name and Brawlhalla ID. The Steam parameter is a int of the Steam account's
        ID64. """
        param = {'steamid': steam, 'api_key': self.key}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.brawlhalla.com/search', params=param) as resp:
                # I didn't know response.json() was a coro, so it returned a generator instead of actual JSON
                steam_info = await resp.json()
                return steam_info  # This correctly returns the JSON.

    async def get_user_stats(self, brawlid: str):
        """Gets a user's stats based on their Brawlhalla ID. It returns a bunch of information, especially if the
        searched user has played a lot of legends. """
        param = {'api_key': self.key}
        async with aiohttp.ClientSession() as session:
            # The offical GET url is https://api.brawlhalla.com/player/{brawlhalla_id}/stats, but how do I use it?
            async with session.get('https://api.brawlhalla.com/player/{}/stats'.format(brawlid), params=param) as resp:
                # Format really is a lifesaver sometimes
                user_stats = await resp.json()
                return user_stats  # Correctly returns a JSON.

    async def get_rank_stats(self, brawlid: str):
        """Gets RANKED stats based on Brawlhalla ID. Don't confuse this with user stats. Returns a bunch of
        information, especially if they play on a lot of 2s teams. """
        param = {'api_key': self.key}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.brawlhalla.com/player/{}/ranked'.format(brawlid), params=param) as resp:
                rank_stats = await resp.json()
                return rank_stats

    async def get_clan_stats(self, clanid: str):
        """Retrieves stats on a clan. Count on this one being large too; it gives information on each member."""
        param = {'api_key': self.key}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.brawlhalla.com/clan/{}'.format(clanid), params=param) as resp:
                clan_stats = await resp.json()
                return clan_stats

    async def get_legend_info(self, legend: str):
        """Gets info about a legend based on it's ID."""
        param = {'api_key': self.key}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.brawlhalla.com/legend/{}'.format(legend), params=param) as resp:
                legend_info = await resp.json()
                return legend_info
