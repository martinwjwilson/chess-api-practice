import pprint
import requests

printer = pprint.PrettyPrinter()


class Networking:

    def get_player(self, player_username: str):
        url = f'https://api.chess.com/pub/player/{player_username}'
        response = self._perform_request(url=url)
        printer.pprint(response)
        return response

    @staticmethod
    def get_player_rating(player_username: str, game_type: str) -> int:
        response = requests.get(f'https://api.chess.com/pub/player/{player_username}/stats').json()
        player_rating = response[game_type]['last']['rating']
        print(f"Your rating is: {player_rating}")
        return int(player_rating)

    @staticmethod
    def _perform_request(url):
        return requests.get(url, headers={'User-Agent': 'username: p1u95, email: martinwjwilson@gmail.com'}).json()
