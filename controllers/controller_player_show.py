from tinydb import TinyDB
import views
import models

db = TinyDB("chess.json")
db_table_player = db.table("players")


class ShowPlayerDB:
    def __init__(self):
        self.messages = views.Messages()
        self.show_list = views.ShowPlayerList()

    def show_players_in_db(self):
        available_players = []
        for players in db_table_player.all():
            available_players.append(models.Player.deserialize_player(players))
        for player in available_players:
            self.show_list.show_players(player)

    def show_players_alphabetical(self):
        available_players = []
        players = db_table_player.all()
        players_sorted = sorted(
            players, key=lambda contestant: contestant["last_name"]
        )
        self.show_list.show_players_headline_az()
        for player in players_sorted:
            available_players.append(models.Player.deserialize_player(player))
        for player in available_players:
            self.show_list.show_players_az(player)

    def show_players_by_rank(self):
        available_players = []
        players = db_table_player.all()
        players_sorted = sorted(
            players, key=lambda contestant: contestant["rank"], reverse=False
        )
        self.show_list.show_players_headline_rank()
        for player in players_sorted:
            available_players.append(models.Player.deserialize_player(player))
        for player in available_players:
            self.show_list.show_players_rank(player)
