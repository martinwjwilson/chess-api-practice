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
    # Set up some variables for testing with like your name and the game format you want to look for
    brain = Brain()  # Create an instance of the Brain class
    test_username = "p1u95"
    test_time_class = "blitz"

    archives_start_time = time.time()
    all_archives = brain.get_player_game_archives(player_username=test_username)  # Get a list of your game archives
    print(f"All of your archives look like: \n{all_archives[0:3]}")
    print("Time to get archives")
    print(f"--- {time.time() - archives_start_time} seconds ---\n")

    # Go through each of my game archives, which is just a big list of strings, and convert those archives into a
    # game object.
    ratings_start_time = time.time()
    all_games = []
    for url in all_archives:
        converted_game = brain.convert_archive_to_games(archive_url=url)  # Convert the url to a Game object
        # Add the game to a list containing all the games. Reason for extending included at the top
        all_games.extend(converted_game)
    print(f"All of your games look like: \n{all_games[0:3]}\n")

    # From the list of games, create a list of ratings. Obviously this doesn't have the data included at the moment
    # but this can easily be added to the Game class :)
    all_ratings = brain.get_rating_changes(username=test_username,
                                           games=all_games,
                                           time_class=test_time_class)
    print(f"All of your ratings are: \n{all_ratings}")
    print("Time to get list of ratings")
    print(f"--- {time.time() - ratings_start_time} seconds ---")


if __name__ == '__main__':
    # For testing networking
    # network_test()

    # For testing the brain
    brain_test()

    # For running the bot
    # bot.run(token)
