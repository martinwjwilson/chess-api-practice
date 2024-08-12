from datetime import datetime
from dateutil.relativedelta import relativedelta
from networking import Networking
import pprint
import requests

printer = pprint.PrettyPrinter()
networking = Networking()
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


def get_player_game_archives(player_username: str) -> [str]:
    return networking.get_player_game_archives(player_username=player_username)


def convert_archive_to_games(archive_url: str):
    """
    Convert an archive url into a list of game data for that month
    :return:
    """
    return networking.get_games_from_archive(archive_url=archive_url)


# def get_rating_changes(games: dict, time_class: str) -> list:
#     """
#     Return a list of ratings from a list of games
#     """
#     list_of_ratings = []
#     for game in games:
#         if game['time_class'] == time_class:
#             if game['white']['username'] == username:
#                 rating_after_game = game['white']['rating']
#                 list_of_ratings.append(rating_after_game)
#                 print(f"Rating for {username}: {rating_after_game}")
#             else:
#                 rating_after_game = game['black']['rating']
#                 list_of_ratings.append(rating_after_game)
#                 print(f"Rating for {username}: {rating_after_game}")
#     return list_of_ratings
#
#
# def get_player_game_results(player_username: str, date: datetime, time_class: str):
#     """
#     Get a player's game results for a given time class on the specified day
#     """
#     games = get_player_game_archives(player_username=player_username,
#                                      selected_year=date.strftime("%Y"),
#                                      selected_month=date.strftime("%m"))
#     wins = 0
#     losses = 0
#     for game in games:
#         if game['time_class'] == time_class:
#             if date.day == datetime.fromtimestamp(game['end_time']).day:
#                 if game['white']['username'] == username:
#                     if game['white']['result'] == "win":
#                         wins += 1
#                     else:
#                         losses += 1
#                 else:
#                     if game['black']['result'] == "win":
#                         wins += 1
#                     else:
#                         losses += 1
#     print(f"{username} stats in {time_class} on {date.strftime('%d/%m/%Y')}\nWins: {wins}\nLosses: {losses}")
#
#
# def get_player_rating_change(player_username: str, date: datetime, time_control: str):
#     """
#     Get the rating changes across a single day for the given player
#     :param player_username: The username of the player whose games to get
#     :param date: The date to check for the rating change
#     :param time_control: The time control to get such as blitz or bullet
#     :return:
#     """
#     game_month = date.strftime("%m")
#     game_year = date.strftime("%Y")
#     games = get_player_game_archives(player_username=player_username,
#                                      selected_year=game_year,
#                                      selected_month=game_month)
#     # TODO: Check that the games aren't empty
#     # Get the player's rating at the end of that day
#     player_rating_at_end_of_day = 0
#     for game in games:
#         if game['time_class'] == time_control:
#             if date.day == datetime.fromtimestamp(game['end_time']).day:
#                 if game['white']['username'] == username:
#                     player_rating_at_end_of_day = game['white']['rating']
#                 else:
#                     player_rating_at_end_of_day = game['black']['rating']
#     if player_rating_at_end_of_day == 0:
#         print(f"The rating for {username} has not changed on the given date")
#         return
#     # Get the player's rating from the closest previous game. This is because each game doesn't show the player's
#     # rating before the results, so there's no way to tell how much they gained or lost without getting their rating
#     # from the most recent previous game (if there is one)
#     previous_player_rating = get_player_previous_rating(player_username=player_username,
#                                                         date=date,
#                                                         time_control=time_control,
#                                                         games=games)
#     # TODO: Check that there is a previous rating
#     player_rating_change = player_rating_at_end_of_day - previous_player_rating
#     print(f"{player_username} rating change for {date.strftime('%d/%m/%Y')}\n{player_rating_change}")
#
#
# def get_player_previous_rating(player_username: str, date: datetime, time_control: str, games: list):
#     # Work backwards from the given date to find and return the closest previous game rating
#     # If there isn't one in the given month then go back a month and get another archive until there aren't
#     # any more months to go
#     for game in reversed(games):
#         # remove everything after the days on the game date
#         given_date = date.replace(hour=0, minute=0, second=0, microsecond=0)
#         current_game_date = datetime.fromtimestamp(game['end_time']).replace(hour=0, minute=0, second=0, microsecond=0)
#         if given_date > current_game_date:  # only check games played before the given date
#             if game['time_class'] == time_control:
#                 if game['white']['username'] == player_username:
#                     return game['white']['rating']
#                 else:
#                     return game['black']['rating']
#     # If you reach here then there was no game in the month archives
#     # See if there is a previous month and try again
#     altered_date = date - relativedelta(months=1)
#     older_games = get_player_game_archives(player_username=player_username,
#                                            selected_year=altered_date.strftime("%Y"),
#                                            selected_month=altered_date.strftime("%m"))
#     # TODO: Check that the game isn't nil
#     return get_player_previous_rating(player_username=player_username,
#                                       date=date,
#                                       time_control=time_control,
#                                       games=older_games)
#
#
# get_player_rating_change(player_username=username,
#                          date=datetime.now(),
#                          time_control=time_class)

# get_player_game_results(player_username=username,
#                         date=datetime.now(),
#                         time_class=time_class)

archives = get_player_game_archives(username)
test_archive = archives[-1]
print(test_archive)
games = convert_archive_to_games(archive_url=test_archive)
printer.pprint(games)

# printer.pprint(player_games)
# rating_changes = get_rating_changes(player_games, time_class)
# plt.plot(rating_changes)
# plt.title(f"{time_class.capitalize()} rating across {month}/{year}")
# plt.ylabel('Rating')
# plt.show()
