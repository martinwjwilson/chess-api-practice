from datetime import datetime
from game import Game
from networking import Networking
import pprint

networking = Networking()


class Brain:

    @staticmethod
    def get_player_game_archives(player_username: str) -> [str]:
        return networking.get_player_game_archives(player_username=player_username)

    @staticmethod
    def convert_archive_to_games(archive_url: str) -> list[Game]:
        """
        Convert an archive url into a list of game data for that month
        """
        archived_games = networking.get_games_from_archive(archive_url=archive_url)
        converted_list_of_games = []
        for archived_game in archived_games:
            converted_list_of_games.append(Game(black_username=archived_game["black"]["username"],
                                                white_username=archived_game["white"]["username"],
                                                black_rating=archived_game["black"]["rating"],
                                                white_rating=archived_game["white"]["rating"],
                                                time_class=archived_game["time_class"],
                                                timestamp=archived_game['end_time']))
        return converted_list_of_games

    @staticmethod
    def get_rating_changes(username: str, games: list[Game], time_class: str) -> list[int]:
        """
        Return a list of ratings from a list of games
        """
        list_of_ratings = []
        for game in games:  # Go through each game
            if game.time_class == time_class:  # Check the game is the correct time class. e.g. bullet or blitz
                # Determine the player's colour, get their rating and add it to the list of ratings
                list_of_ratings.append(game.get_player_rating_from_username(username=username))
        return list_of_ratings
