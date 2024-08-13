"""
Hello, I made this file to explain what's going on roughly

Firstly I import my Brain class, I've just put all of my logic in here for now

The rest of the logic is explained in if __name__ == "__main__": at the bottom

This is an explanation of something I do underneath
The reason for extending the list is this...
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
b.append(a)
b
[4, 5, 6, [1, 2, 3]]

But if you extend...
c.extend(a)
c
[7, 8, 9, 1, 2, 3]
"""

from brain import Brain

if __name__ == "__main__":
    # Set up some variables for testing with like your name and the game format you want to look for
    brain = Brain()  # Create an instance of the Brain class
    test_username = "DemonChild2290"
    test_time_class = "blitz"

    all_archives = brain.get_player_game_archives(player_username=test_username)  # Get a list of your game archives
    print(f"All of your archives look like: \n{all_archives[0:3]}\n")

    # Go through each of my game archives, which is just a big list of strings, and convert those archives into a
    # game object.
    all_games = []
    for url in all_archives:
        converted_game = brain.convert_archive_to_games(archive_url=url)  # Convert the url to a Game object
        # Add the game to a list containing all the games. Reason for extending included at the top
        all_games.extend(converted_game)
    print(f"All of your games look like: \n{all_games[0:3]}\n")

    # From the list of games, create a list of ratings. Obviously this doesn't have the data included at the moment
    # but this can easily be added to the Game class :)
    all_ratings = brain.get_rating_changes(username=test_username,
                                           games=all_games,
                                           time_class=test_time_class)
    print(f"All of your ratings are: \n{all_ratings}")

