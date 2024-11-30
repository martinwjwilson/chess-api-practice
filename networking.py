import pprint
import requests

printer = pprint.PrettyPrinter()


class Networking:

    def get_player(self, player_username: str):
        url = f'https://api.chess.com/pub/player/{player_username}'
        response = self.__perform_request(url=url)
        return response

    def get_player_rating(self, player_username: str, game_type: str) -> int:
        url = f'https://api.chess.com/pub/player/{player_username}/stats'
        response = self.__perform_request(url=url)
        player_rating = response[game_type]['last']['rating']
        return int(player_rating)

    def get_player_game_archives(self, player_username: str):
        url = f'https://api.chess.com/pub/player/{player_username}/games/archives'
        response = self.__perform_request(url=url)
        archives = response["archives"]
        # TODO: Error handling - Put a check in here for if the response fails
        return archives

    def get_games_from_archive(self, archive_url: str):
        response = self.__perform_request(url=archive_url)
        return response['games']

    @staticmethod
    def __perform_request(url):
        """
        Takes a URL and performs a network call with the relevant headers
        :param url: The URL to use in the call
        """
        return requests.get(url, headers={'User-Agent': 'username: p1u95, email: martinwjwilson@gmail.com'}).json()
