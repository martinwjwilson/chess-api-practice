from chessdotcom import get_leaderboards, get_player_profile
import pprint

printer = pprint.PrettyPrinter()


def print_leaderboards():
    data = get_leaderboards().json
    leaderboard = data.get('leaderboards')
    # printer.pprint(leaderboard)
    for category in leaderboard:
        print('Category: ', category)
        for idx, entry in enumerate(leaderboard[category]):
            print(entry)


def get_player(username: str):
    data = get_player_profile(username).json
    # printer.pprint(data)
    player = data.get('player')
    name = player['name']
    location = player['location']
    print(f'{name} lives in {location}')


username = input('What is the username whose data you want to steal? ')
get_player(username)
