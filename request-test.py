import pprint
import requests

printer = pprint.PrettyPrinter()


def get_player(username: str):
    response = requests.get(f'https://api.chess.com/pub/player/{username}').json()
    printer.pprint(response)


username = input('What is the username whose data you want to steal? ')
get_player(username)
