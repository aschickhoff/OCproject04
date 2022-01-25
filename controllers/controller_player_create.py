from tinydb import TinyDB
import views
import models

GENDERS = ("m", "f")

db = TinyDB("chess.json")
db_table_player = db.table("players")


class CreatePlayer:

    def __init__(self):
        self.messages = views.Messages()
        self.inputs = views.Inputs()

    def get_information(self):
        try:
            last_db_entry = db_table_player.all()[-1]
            last_id = last_db_entry.doc_id
            new_player_id = last_id + 1
        except IndexError:
            new_player_id = 1
        last_name = self.input_last_name()
        first_name = self.input_first_name()
        birth_date = self.input_birth_date()
        gender = self.input_gender()
        player_id = new_player_id
        player = models.Player(last_name, first_name, birth_date, gender, player_id, rank=0, points=0)
        player.save_to_player_db()

    def input_last_name(self):
        last_name = input(self.inputs.enter_last_name())
        if isinstance(last_name, str) and last_name.isalpha():
            return last_name
        else:
            self.messages.invalid_input()
            return self.input_last_name()

    def input_first_name(self):
        first_name = input(self.inputs.enter_first_name())
        if isinstance(first_name, str) and first_name.isalpha():
            return first_name
        else:
            self.messages.invalid_input()
            return self.input_first_name()

    def input_birth_date(self):
        birth_date = input(self.inputs.enter_birth_date())
        return birth_date

    def input_gender(self):
        gender = input(self.inputs.enter_gender())
        if gender.lower() in GENDERS:
            return gender
        else:
            self.messages.invalid_input()
            return self.input_gender()
