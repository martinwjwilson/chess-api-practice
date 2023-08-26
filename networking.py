import requests


class Networking:

    @staticmethod
    def get_player(player_username: str):
        response = requests.get(f'https://api.chess.com/pub/player/{player_username}').json()
        return response

    @staticmethod
    def get_player_rating(player_username: str, game_type: str) -> int:
        response = requests.get(f'https://api.chess.com/pub/player/{player_username}/stats').json()
        player_rating = response[game_type]['last']['rating']
        print(f"Your rating is: {player_rating}")
        return int(player_rating)
