from pprint import PrettyPrinter
import requests

response = requests.get('https://api.chess.com/pub/player/p1u95').json()
PrettyPrinter().pprint(response)
