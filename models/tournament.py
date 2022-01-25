from tinydb import TinyDB

import models

db = TinyDB("chess.json")
db_table_tournament = db.table("tournaments")


class Tournament:
    def __init__(
            self,
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
    ):
        self.tournament_name = tournament_name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.rounds = rounds
        self.pairings = pairings
        self.amount_of_rounds = amount_of_rounds
        self.tournament_id = tournament_id
        self.players = players

    def __repr__(self):
        return(
            f"Tournament("
            f"{self.tournament_name},"
            f"{self.venue},"
            f"{self.start_date},"
            f"{self.end_date},"
            f"{self.time_control},"
            f"{self.description},"
            f"{self.rounds},"
            f"{self.pairings},"
            f"{self.amount_of_rounds},"
            f"{self.tournament_id},"
            f"{self.players}"
            f")"
        )

    def serialize_tournament(self):
        return self.__dict__

    @classmethod
    def deserialize_tournament(cls, serialized_tournament):
        tournament_name = serialized_tournament["tournament_name"]
        venue = serialized_tournament["venue"]
        start_date = serialized_tournament["start_date"]
        end_date = serialized_tournament["end_date"]
        time_control = serialized_tournament["time_control"]
        description = serialized_tournament["description"]
        rounds = [
            models.Round.deserialize_round(serialized_round)
            for serialized_round in serialized_tournament["rounds"]
        ]
        pairings = serialized_tournament["pairings"]
        amount_of_rounds = serialized_tournament["amount_of_rounds"]
        tournament_id = serialized_tournament["tournament_id"]
        players = serialized_tournament["players"]
        return Tournament(
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

    def save_to_tournament_db(self):
        db_table_tournament.insert(self.serialize_tournament())
