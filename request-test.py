from datetime import datetime
import matplotlib.pyplot as plt
import pprint
import requests

printer = pprint.PrettyPrinter()
username = "p1u95"
year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%m")
time_class = "blitz"


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
    games = response["games"]
    return games


def get_rating_changes(games: dict, time_class: str) -> list:
    """
    Return a list of ratings from a list of games
    """
    list_of_ratings = []
    for game in games:
        if game['time_class'] == time_class:
            if game['white']['username'] == username:
                rating_after_game = game['white']['rating']
                list_of_ratings.append(rating_after_game)
                print(f"Rating for {username}: {rating_after_game}")
            else:
                rating_after_game = game['black']['rating']
                list_of_ratings.append(rating_after_game)
                print(f"Rating for {username}: {rating_after_game}")
    return list_of_ratings


def get_player_game_results(player_username: str, date: datetime, time_class: str):
    """
    Get a player's game results for a given time class on the specified day
    """
    games = get_player_game_archives(player_username=player_username,
                                             selected_year=date.strftime("%Y"),
                                             selected_month=date.strftime("%m"))
    wins = 0
    losses = 0
    for game in games:
        if game['time_class'] == time_class:
            if date.day == datetime.fromtimestamp(game['end_time']).day:
                if game['white']['username'] == username:
                    if game['white']['result'] == "win":
                        wins += 1
                    else:
                        losses += 1
                else:
                    if game['black']['result'] == "win":
                        wins += 1
                    else:
                        losses += 1
    print(f"{username} stats in {time_class} on {date.strftime('%d/%m/%Y')}\nWins: {wins}\nLosses: {losses}")


get_player_game_results(player_username=username,
                        date=datetime.now(),
                        time_class=time_class)

# player_games = get_player_game_archives(username, year, month)
# rating_changes = get_rating_changes(player_games, time_class)
# plt.plot(rating_changes)
# plt.title(f"{time_class.capitalize()} rating across {month}/{year}")
# plt.ylabel('Rating')
# plt.show()
