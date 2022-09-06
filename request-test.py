import pprint
import requests

printer = pprint.PrettyPrinter()
username = "p1u95"
year = "2022"
month = "09"


def print_leaderboards():
    data = requests.get('https://api.chess.com/pub/leaderboards').json()
    categories = data.keys()

    for category in categories:
        print(f'Category: {category}')
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player(player_username: str):
    response = requests.get(f'https://api.chess.com/pub/player/{player_username}').json()
    printer.pprint(response)


def get_player_game_archives(player_username: str, selected_year: str, selected_month: str):
    """
    Returns a json of games for the player for the given year and month
    """
    response = requests.get(f"https://api.chess.com/pub/player/{player_username}"
                            f"/games/{selected_year}/{selected_month}").json()
    return response


player_games = get_player_game_archives(username, year, month)
printer.pprint(player_games)
