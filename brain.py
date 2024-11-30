from game import Game
from networking import Networking

networking = Networking()

# TODO: Rename brain to something more meaningful
class Brain:

    @staticmethod
    def get_player_game_archives(player_username: str) -> [str]:
        return networking.get_player_game_archives(player_username=player_username)

    @staticmethod
    def convert_archive_to_games(archive_url: str) -> list[Game]:
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
    def get_rating_changes_for_time_class(username: str, games: list[Game], time_class: str) -> list[int]:
        list_of_ratings = []
        for game in games:
            if game.time_class == time_class:
                player_rating_in_game = game.get_player_rating_from_username(username=username)
                list_of_ratings.append(player_rating_in_game)
        return list_of_ratings
