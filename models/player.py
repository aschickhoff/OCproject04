from tinydb import TinyDB

db = TinyDB("chess.json")
db_table_player = db.table("players")


class Player:
    def __init__(
            self,
            last_name,
            first_name,
            birth_date,
            gender,
            player_id,
            rank,
            points
    ):
        self.last_name = last_name.capitalize()
        self.first_name = first_name.capitalize()
        self.birth_date = birth_date
        self.gender = gender.lower()
        self.rank = rank
        self.points = points
        self.player_id = player_id

    def __repr__(self):
        return(
            f"Player("
            f"{self.last_name},"
            f"{self.first_name},"
            f"{self.birth_date},"
            f"{self.gender},"
            f"{self.player_id},"
            f"{self.rank},"
            f"{self.points}"
            f")"
        )

    def serialize_player(self):
        return self.__dict__

    @classmethod
    def deserialize_player(cls, serialized_player):
        last_name = serialized_player["last_name"]
        first_name = serialized_player["first_name"]
        birth_date = serialized_player["birth_date"]
        gender = serialized_player["gender"]
        player_id = serialized_player["player_id"]
        rank = serialized_player["rank"]
        points = serialized_player["points"]
        return Player(
            last_name,
            first_name,
            birth_date,
            gender,
            player_id,
            rank,
            points
        )

    def save_to_player_db(self):
        db_table_player.insert(self.serialize_player())
