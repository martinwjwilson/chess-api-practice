from datetime import datetime
from game import Game
from networking import Networking
import pprint

printer = pprint.PrettyPrinter()
networking = Networking()
test_username = "p1u95"
year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%m")
test_time_class = "blitz"


class Brain:

    @staticmethod
    def get_player_game_archives(player_username: str) -> [str]:
        return networking.get_player_game_archives(player_username=player_username)

    @staticmethod
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

    @staticmethod
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
