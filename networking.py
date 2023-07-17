import requests


class Networking:

    @staticmethod
    def test_method():
        return 1

    @staticmethod
    def get_player(player_username: str):
        response = requests.get(f'https://api.chess.com/pub/player/{player_username}').json()
        return response
