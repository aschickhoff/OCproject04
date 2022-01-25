from datetime import datetime, timedelta
from tinydb import TinyDB

import controllers
import views
import models

TIME_CONTROL = ("a", "b", "c")

db = TinyDB("chess.json")
db_table_player = db.table("players")
db_table_tournament = db.table("tournaments")


class CreateTournament:
    def __init__(self):
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.view = views.TournamentMenuView()
        self.commands = controllers.General()
        self.players_list = controllers.ShowPlayerDB()

    def get_information(self):
        try:
            last_db_entry = db_table_tournament.all()[-1]
            last_id = last_db_entry.doc_id
            new_tournament_id = last_id + 1
        except IndexError:
            new_tournament_id = 1
        tournament_name = self.input_tournament_name()
        venue = self.input_venue()
        start_date = (datetime.now()).strftime("%d/%m/%Y")
        end_date = self.input_duration()
        time_control = self.input_time_control()
        description = self.input_description()

        self.commands.clear_screen()
        self.view.show_menu()

        players = self.add_players_from_list()
        rounds = []
        pairings = []
        amount_of_rounds = 4
        tournament_id = new_tournament_id
        tournament = models.Tournament(
            tournament_name,
            venue,
            start_date,
            end_date,
            time_control,
            description,
            rounds,
            pairings,
            amount_of_rounds,
            tournament_id,
            players
        )
        tournament.save_to_tournament_db()
        self.messages.tournament_created()
        input(self.inputs.press_key_input())

    def add_players_from_list(self):
        last_db_entry = db_table_player.all()[-1]
        last_id = last_db_entry.doc_id
        self.players_list.show_players_in_db()
        players_added = []
        amount_of_participants = 0
        while amount_of_participants <= 7:
            participant_id = input(self.inputs.player_to_add())
            if participant_id.isdigit() and int(participant_id) <= last_id:
                if participant_id in players_added:
                    self.messages.player_already_added()
                    continue
                players_added.append(participant_id)
                amount_of_participants += 1
            else:
                self.messages.invalid_input()
                continue
        return players_added

    def input_tournament_name(self):
        tournament_name = input(self.inputs.enter_tournament_name())
        return tournament_name

    def input_venue(self):
        venue = input(self.inputs.enter_venue())
        return venue

    def input_duration(self):
        temp_duration = input(self.inputs.enter_duration())
        if temp_duration.isdigit():
            duration = int(temp_duration)
            end_date = (datetime.now() + timedelta(days=duration)).strftime("%d/%m/%Y")
            return end_date
        else:
            self.messages.invalid_input()
            return self.input_duration()

    def input_time_control(self):
        time_control = input(self.inputs.enter_time_control())
        if time_control.lower() in TIME_CONTROL:
            if time_control.lower() == "a":
                time_control = "Bullet"
            elif time_control.lower() == "b":
                time_control = "Blitz"
            elif time_control.lower() == "c":
                time_control = "Rapid"
            return time_control
        else:
            self.messages.invalid_input()
            return self.input_time_control()

    def input_description(self):
        description = input(self.inputs.enter_description())
        return description
