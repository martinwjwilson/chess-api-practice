from brain import Brain
import pprint
import json
import typing
from networking import Networking
import discord
from discord.ext import commands
import time

printer = pprint.PrettyPrinter()

# load bot token
with open("token.json", 'r') as f:
    token = json.load(f)['TOKEN']

# intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} - {bot.user.id}")  # name of bot and ID
    print(discord.__version__)  # current version of discord.py
    print("Ready...")


@bot.command()
async def hello(ctx):
    print("Someone said hello")
    await ctx.send("Hi there :3")


@bot.command()
async def player_rating(ctx, username: typing.Optional[str] = "", game_type: typing.Optional[str] = ""):
    # ask for username if one wasn't provided
    if username == "":
        # TODO: create constants file for questions
        question = "What is your username?"
        username = get_input_from_question(ctx, question=question)
        if username == "":
            # TODO: throw error?
            await ctx.send("Error")
            return

    # ask for game type if one wasn't provided
    if game_type == "":
        question = "What game type do you want to check?"
        game_type = get_input_from_question(ctx, question=question)
        if game_type == "":
            # TODO: throw error?
            await ctx.send("Error")
            return
    # TODO: Convert input to possible game types

    print(f"username is now {username}")
    network_bot = Networking()
    rating = network_bot.get_player_rating(player_username=username, game_type=game_type)
    await ctx.send(f"The rating for **{username}** in **{game_type}** is **{rating}**")


async def get_input_from_question(ctx, question: str) -> str:
    await ctx.send(question)
    msg = await bot.wait_for('message',
                             check=lambda message: message.author == ctx.author)
    return msg.content


# TODO: Implement set_player function
# @bot.command()
# async def set_player(ctx):
#     await ctx.send("What is your username on chess.com?")
#     message = await bot.wait_for('message')
#     # await print_leaderboards(ctx)
#     print(Networking.test_method())
#     await ctx.send(f"You are now linked to: {message.content}")


def network_test():
    networking = Networking()
    networking.get_player(player_username="p1u95")
    networking.get_player_rating(player_username="p1u95", game_type="chess_blitz")


def brain_test():
    # Set up
    brain = Brain()
    test_username = "p1u95"
    test_time_class = "blitz"

    start_time = time.time()
    archives = brain.get_player_game_archives(test_username)
    print("Time to get archives")
    print(f"--- {time.time() - start_time} seconds ---")
    start_time = time.time()
    list_of_games = []
    for archive in archives:
        converted_games = brain.convert_archive_to_games(archive_url=archive)
        for game in converted_games:
            list_of_games.append(game)
    list_of_ratings = brain.get_rating_changes(username=test_username, games=list_of_games, time_class=test_time_class)
    print(list_of_ratings)
    print("Time to get list of ratings")
    print(f"--- {time.time() - start_time} seconds ---")


if __name__ == '__main__':
    # For testing networking
    # network_test()

    # For testing the brain
    brain_test()

    # For running the bot
    # bot.run(token)
