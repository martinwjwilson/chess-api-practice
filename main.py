from chessdotcom import get_leaderboards, get_player_profile
import pprint
import json
import typing

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
async def player_rating(ctx, username: typing.Optional[str] = "", game_type: typing.Optional[str] = ""):
    # ask for username if one wasn't provided
    if username == "":
        await ctx.send("What is your username?")
        msg = await client.wait_for('message',
                                    check=lambda message: message.author == ctx.author)
        username = msg.content
        # check that there is a username
        if username == "":
            return

    # ask for game type if one wasn't provided
    if game_type == "":
        await ctx.send("What game type do you want to check?")
        msg = await client.wait_for('message',
                                    check=lambda message: message.author == ctx.author)
        # TODO: Convert input to possible game types
        game_type = msg.content
        # check that there is a game_type
        if game_type == "":
            return

    print(f"username is now {username}")
    network_client = Networking()
    rating = network_client.get_player_rating(player_username=username, game_type=game_type)
    await ctx.send(f"The rating for **{username}** in **{game_type}** is **{rating}**")


# TODO: Implement set_player function
# @client.command()
# async def set_player(ctx):
#     await ctx.send("What is your username on chess.com?")
#     message = await client.wait_for('message')
#     # await print_leaderboards(ctx)
#     print(Networking.test_method())
#     await ctx.send(f"You are now linked to: {message.content}")


if __name__ == '__main__':
    client.run(token)
