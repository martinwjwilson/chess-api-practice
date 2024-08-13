from datetime import datetime
from dateutil.relativedelta import relativedelta
from game import Game
from networking import Networking
import pprint
import requests
import time

printer = pprint.PrettyPrinter()
networking = Networking()
test_username = "p1u95"
year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%m")
test_time_class = "blitz"


def get_player_game_archives(player_username: str) -> [str]:
    return networking.get_player_game_archives(player_username=player_username)


def convert_archive_to_games(archive_url: str):
    """
    Convert an archive url into a list of game data for that month
    :return:
    """
    archived_games = networking.get_games_from_archive(archive_url=archive_url)
    converted_list_of_games = []
    for archived_game in archived_games:
        converted_list_of_games.append(Game(black_username=archived_game["black"]["username"],
                                            white_username=archived_game["white"]["username"],
                                            black_rating=archived_game["black"]["rating"],
                                            white_rating=archived_game["white"]["rating"],
                                            time_class=archived_game["time_class"]))
    return converted_list_of_games


def get_rating_changes(username: str, games: list[Game], time_class: str) -> list:
    """
    Return a list of ratings from a list of games
    """
    list_of_ratings = []
    for game in games:
        if game.time_class == time_class:
            player_colour = "white" if game.white_username == username else "black"
            rating_after_game = game.white_rating if player_colour == "white" else game.black_rating
            list_of_ratings.append(rating_after_game)
            # print(f"Rating for {username} after the game: {rating_after_game}")
    return list_of_ratings


start_time = time.time()
archives = get_player_game_archives(test_username)
print("Time to get archives")
print(f"--- {time.time() - start_time} seconds ---")
start_time = time.time()
list_of_games = []
for archive in archives:
    converted_games = convert_archive_to_games(archive_url=archive)
    for game in converted_games:
        list_of_games.append(game)
list_of_ratings = get_rating_changes(username=test_username, games=list_of_games, time_class=test_time_class)
print("Time to get list of ratings")
print(f"--- {time.time() - start_time} seconds ---")
