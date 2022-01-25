from tinydb import TinyDB
import views
import controllers
import models

db = TinyDB("chess.json")
db_table_player = db.table("players")


class EditPlayer:
    def __init__(self):
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.show_list = controllers.ShowPlayerDB()

    def edit_player_rank(self):
        self.show_list.show_players_in_db()
        userid = input(self.inputs.player_to_edit())
        if userid.isdigit():
            result = db_table_player.get(doc_id=int(userid))
            player = models.Player.deserialize_player(result)
            new_rank = input(self.inputs.enter_new_rank())
            if new_rank.isdigit():
                player.rank = new_rank
                db_table_player.update({"rank": int(player.rank)}, doc_ids=[int(userid)])
            else:
                self.messages.invalid_input()
                return self.edit_player_rank()
        else:
            self.messages.invalid_input()
