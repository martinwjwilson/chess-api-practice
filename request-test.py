import pprint
import requests

printer = pprint.PrettyPrinter()
username = "p1u95"


def print_leaderboards():
    data = requests.get('https://api.chess.com/pub/leaderboards').json()
    categories = data.keys()

    for category in categories:
        print(f'Category: {category}')
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player(username: str):
    response = requests.get(f'https://api.chess.com/pub/player/{username}').json()
    printer.pprint(response)


def get_player_game_archives():
    year = "2022"
    month = "09"
    response = requests.get(f"https://api.chess.com/pub/player/{username}/games/{year}/{month}").json()
    printer.pprint(response)


get_player_game_archives()
