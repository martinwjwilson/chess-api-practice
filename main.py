from chessdotcom import get_leaderboards, get_player_profile
import pprint
import json
import discord
from discord.ext import commands

printer = pprint.PrettyPrinter()

# load bot token
with open("token.json", 'r') as f:
    token = json.load(f)['TOKEN']

# intents
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=">", intents=intents)


@client.event
async def on_ready():
    print(f"{client.user.name} - {client.user.id}")  # name of bot and ID
    print(discord.__version__)  # current version of discord.py
    print("Ready...")


@client.command()
async def foo(ctx, arg):
    await ctx.send(arg)


@client.command()
async def print_leaderboards(ctx):
    data = get_leaderboards().json
    leaderboard = data.get('leaderboards')
    # printer.pprint(leaderboard)
    for category in leaderboard:
        print('Category: ', category)
        for idx, entry in enumerate(leaderboard[category]):
            print(entry)


@client.command()
async def get_player(ctx, username: str):
    data = get_player_profile(username).json
    # printer.pprint(data)
    player = data.get('player')
    name = player['name']
    location = player['location']
    print(f'{name} lives in {location}')


if __name__ == '__main__':
    client.run(token)
