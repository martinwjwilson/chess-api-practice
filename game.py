class Game:
    def __init__(self, black_username: str, white_username: str, black_rating: int, white_rating: int, time_class: str,
                 timestamp: int):
        self.black_username = black_username
        self.white_username = white_username
        self.black_rating = black_rating
        self.white_rating = white_rating
        self.time_class = time_class
        self.timestamp = timestamp

    def get_player_rating_from_username(self, username: str) -> int:
        player_colour = "white" if self.white_username == username else "black"
        return self.white_rating if player_colour == "white" else self.black_rating
