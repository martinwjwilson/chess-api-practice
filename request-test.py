import matplotlib.pyplot as plt
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


def get_rating_changes(games: dict, time_class: str):
    """
    Return a list of ratings from a list of games
    """
    # specify the game type
    games = games['games']
    list_of_ratings = []
    for game in games:
        if game['white']['username'] == username:
            rating_after_game = game['white']['rating']
            list_of_ratings.append(rating_after_game)
            print(f"Rating for {username}: {rating_after_game}")
        else:
            rating_after_game = game['black']['rating']
            list_of_ratings.append(rating_after_game)
            print(f"Rating for {username}: {rating_after_game}")
    plt.plot(list_of_ratings)
    plt.ylabel('Rating')
    plt.savefig("mygraph.png")


player_games = get_player_game_archives(username, year, month)
get_rating_changes(player_games, 'blitz')
