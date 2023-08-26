from chessdotcom import get_leaderboards, get_player_profile
import pprint
import json
import requests

from networking import Networking
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
async def print_leaderboards(ctx):
    data = get_leaderboards().json
    leaderboard = data.get('leaderboards')
    for category in leaderboard:
        print('Category: ', category)
        for idx, entry in enumerate(leaderboard[category]):
            print(entry)


@client.command()
async def player_rating(ctx, username: str):
    if username == "":
        # TODO: ask for the players username
        return
    network_client = Networking()
    rating = network_client.get_player_rating(player_username=username, game_type="chess_blitz")
    await ctx.send(f"The rating for **{username}** rating is **{rating}**")


# TODO: Implement set_player function
# @client.command()
# async def set_player(ctx):
#     await ctx.send("What is your username on chess.com?")
#     message = await client.wait_for('message')
#     # await print_leaderboards(ctx)
#     print(Networking.test_method())
#     await ctx.send(f"You are now linked to: {message.content}")


# main

if __name__ == '__main__':
    client.run(token)
