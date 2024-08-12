import pprint
import requests

printer = pprint.PrettyPrinter()


class Networking:

    def get_player(self, player_username: str):
        url = f'https://api.chess.com/pub/player/{player_username}'
        response = self.__perform_request(url=url)
        printer.pprint(response)
        return response

    def get_player_rating(self, player_username: str, game_type: str) -> int:
        url = f'https://api.chess.com/pub/player/{player_username}/stats'
        response = self.__perform_request(url=url)
        printer.pprint(response)
        player_rating = response[game_type]['last']['rating']
        printer.pprint(f"Your rating for {game_type} is: {player_rating}")
        return int(player_rating)

    def get_player_game_archives(self, player_username: str):
        """
        Returns a list of game archives
        """
        url = f'https://api.chess.com/pub/player/{player_username}/games/archives'
        response = self.__perform_request(url=url)
        # TODO: Error handling - Put a check in here for if the response fails
        return games

    @staticmethod
    def __perform_request(url):
        return requests.get(url, headers={'User-Agent': 'username: p1u95, email: martinwjwilson@gmail.com'}).json()
