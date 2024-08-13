# Archived Methods
# Old unused code or code that's not been updated yet

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


# TODO: Do this method for a specific year and month?
# def get_player_game_archives(self, player_username: str, selected_year: str, selected_month: str):
#     """
#     Returns a json of game archives
#     """
#     https: // api.chess.com / pub / player / p1u95 / games / archives
#     url = f'https://api.chess.com/pub/player/{player_username}/games/{selected_year}/{selected_month}'
#     response = self.__perform_request(url=url)
#     # TODO: Error handling - Put a check in here for if the response fails
#     games = response["games"]
#     return games


# Code for printing out a graph of the user's ratings
# printer.pprint(player_games)
# rating_changes = get_rating_changes(player_games, time_class)
# plt.plot(rating_changes)
# plt.title(f"{time_class.capitalize()} rating across {month}/{year}")
# plt.ylabel('Rating')
# plt.show()