import requests


class Networking:
    # PUBLIC METHODS

    @staticmethod
    def player_rating(player_username: str) -> int:
        player_data = Networking.get_player(player_username=player_username)
        player_rating = player_data['name']
        print(player_rating)
        return 1

    # PRIVATE METHODS

    @staticmethod
    def get_player(player_username: str):
        response = requests.get(f'https://api.chess.com/pub/player/{player_username}').json()
        print(response)
        return response
