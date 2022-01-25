from datetime import datetime
from tinydb import TinyDB

import controllers
import views
import models

db = TinyDB("chess.json")
db_table_player = db.table("players")
db_table_tournament = db.table("tournaments")


class RunTournament:
    def __init__(self):
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.view = views.TournamentMenuView()
        self.commands = controllers.General()
        self.show_tournament = controllers.ShowTournamentDB()
        self.edit_player = controllers.EditPlayer()
        self.show_list = views.ShowTournamentList()

    def start_tournament(self):
        amount = db_table_tournament.all()
        if len(amount) == 0:
            self.messages.create_tournament_first()
            input(self.inputs.press_key_input())
            return
        rounds_played, players, tournament = self.select_tournament()
        if rounds_played == 0:
            self.create_first_round(players, rounds_played + 1, tournament)
        elif rounds_played < 4:
            self.create_next_round(players, rounds_played + 1, tournament)
        elif rounds_played == 4:
            self.messages.tournament_ended()
            input()

    def select_tournament(self):
        self.show_tournament.show_tournament_in_db()
        tournament_id = input(self.inputs.tournament_for_round())
        number_of_rounds = None
        available_players = None
        tournament = None
        if tournament_id.isdigit():
            result = db_table_tournament.get(doc_id=int(tournament_id))
            tournament = models.Tournament.deserialize_tournament(result)
            available_rounds = tournament.rounds
            number_of_rounds = len(available_rounds)
            available_players = tournament.players
        else:
            self.messages.invalid_input()
        return number_of_rounds, available_players, tournament

    def check_round_status(self):
        self.show_tournament.show_tournament_in_db()
        tournament_id = input(self.inputs.tournament_for_round())
        number_of_rounds = None
        available_players = None
        tournament = None
        if tournament_id.isdigit():
            result = db_table_tournament.get(doc_id=int(tournament_id))
            tournament = models.Tournament.deserialize_tournament(result)
            available_rounds = tournament.rounds
            number_of_rounds = len(available_rounds)
            available_players = tournament.players
        else:
            self.messages.invalid_input()
        return number_of_rounds, available_players, tournament

    def create_first_round(self, players, round_number, tournament):
        """
        Creation of first round:
        Players are sorted by rank and then matched:
        player[0] - player[4]
        player[1] - player[5]
        player[2] - player[6]
        player[3] - player[7]
        for later use the pairings are stored in the database
        """
        start_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        listed_players = players
        players_to_match = []
        matches = []
        pairings = []
        name_of_round = "Round " + str(round_number)
        for i in range(len(listed_players)):
            players_to_match.append(db_table_player.get(doc_id=int(listed_players[i])))
        players_sorted_by_rank = sorted(players_to_match, key=lambda contestant: contestant["rank"], reverse=False)
        for i in range(4):
            match = (
                [players_sorted_by_rank[i]["player_id"], players_sorted_by_rank[i]["points"]],
                [players_sorted_by_rank[i + 4]["player_id"], players_sorted_by_rank[i + 4]["points"]]
            )
            matches.append(match)
            pairing = (
                [players_sorted_by_rank[i]["player_id"], players_sorted_by_rank[i + 4]["player_id"]],
                [players_sorted_by_rank[i + 4]["player_id"], players_sorted_by_rank[i]["player_id"]]
            )
            pairings.append(pairing)
        results = self.round_results(matches)
        end_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        active_round = models.Round(name_of_round, start_time, end_time, results)
        round_serialized = [active_round.serialize_round()]
        tournament.rounds = round_serialized
        db_table_tournament.update({"rounds": tournament.rounds}, doc_ids=[int(tournament.tournament_id)])
        db_table_tournament.update({"pairings": pairings}, doc_ids=[int(tournament.tournament_id)])

    def create_next_round(self, players, round_number, tournament):
        """
        Creation of rounds after first round:
        Players are sorted by points and then by rank, in case possible opponents got the same amount of points
        player[0] - player[1]
        player[2] - player[3]
        player[4] - player[5]
        player[6] - player[7]
        If Player 1 has already played Player 2, Player 3 will be used etc.
        """
        start_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        listed_players = players
        players_to_be_matched = []
        matches = []
        pairings = []
        name_of_round = "Round " + str(round_number)
        for i in range(len(listed_players)):
            players_to_be_matched.append(db_table_player.get(doc_id=int(listed_players[i])))
        players_sorted_by_points = self.sort_player_by_points_and_rank(tournament)
        current_pairings = []
        for i in range(len(players_sorted_by_points)):
            while players_sorted_by_points[i].player_id not in current_pairings:
                n = i + 1
                while (
                        n < len(players_sorted_by_points)
                        and players_sorted_by_points[n].player_id in current_pairings
                        or any([players_sorted_by_points[i].player_id, players_sorted_by_points[n].player_id]
                               in x for x in tournament.pairings
                               )
                ):
                    n += 1
                match = (
                    [players_sorted_by_points[i].player_id, players_sorted_by_points[i].points],
                    [players_sorted_by_points[n].player_id, players_sorted_by_points[n].points]
                )
                current_pairings.append(players_sorted_by_points[i].player_id)
                current_pairings.append(players_sorted_by_points[n].player_id)
                matches.append(match)
                pairing = (
                    [players_sorted_by_points[i].player_id, players_sorted_by_points[n].player_id],
                    [players_sorted_by_points[n].player_id, players_sorted_by_points[i].player_id]
                )
                pairings.append(pairing)
            i += 1
        results = self.round_results(matches)
        end_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        active_round = models.Round(name_of_round, start_time, end_time, results)
        round_serialized = [active_round.serialize_round()]
        temp_round = tournament.rounds
        temp_round_serialized = []
        for i in range(len(temp_round)):
            temp_round_serialized.append(temp_round[i].serialize_round())
        temp_round_serialized.extend(round_serialized)
        db_table_tournament.update({"rounds": temp_round_serialized}, doc_ids=[int(tournament.tournament_id)])
        temp_pairings = tournament.pairings
        temp_pairings.extend(pairings)
        db_table_tournament.update({"pairings": temp_pairings}, doc_ids=[int(tournament.tournament_id)])

    @staticmethod
    def sort_player_by_points_and_rank(tournament):
        listed_players = tournament.players
        players = []
        rounds_in_tournament = tournament.rounds
        rounds_serialized = []
        for i in range(len(rounds_in_tournament)):
            rounds_serialized.append(rounds_in_tournament[i].serialize_round())
        for i in range(len(listed_players)):
            players.append(db_table_player.get(doc_id=int(listed_players[i])))
        available_players = []
        for player in players:
            available_players.append(models.Player.deserialize_player(player))
        available_players_with_points = []
        for player in available_players:
            total_points = 0
            for i in range(len(rounds_serialized)):
                matches = rounds_serialized[i]["matches"]
                for n in range(len(matches)):
                    if matches[n][0][0] == player.player_id:
                        total_points = total_points + matches[n][0][1]
                    elif matches[n][1][0] == player.player_id:
                        total_points = total_points + matches[n][1][1]
            player.points = total_points
            available_players_with_points.append(player)
        players_sorted_new = sorted(
            sorted(available_players_with_points, key=lambda contestant: contestant.rank),
            key=lambda contestant: contestant.points, reverse=True
        )
        return players_sorted_new

    def round_results(self, matches):
        round_matches = []
        for i in range(len(matches)):
            player_one_id = db_table_player.get(
                doc_id=int(matches[i][0][0]))["player_id"]
            player_two_id = db_table_player.get(
                doc_id=int(matches[i][1][0]))["player_id"]
            player_one_first_name = db_table_player.get(
                doc_id=int(matches[i][0][0]))["first_name"]
            player_one_last_name = db_table_player.get(
                doc_id=int(matches[i][0][0]))["last_name"]
            player_two_first_name = db_table_player.get(
                doc_id=int(matches[i][1][0]))["first_name"]
            player_two_last_name = db_table_player.get(
                doc_id=int(matches[i][1][0]))["last_name"]
            self.show_list.current_match(
                player_one_first_name, player_one_last_name, player_two_first_name, player_two_last_name
            )
            point_distribution = True
            while point_distribution:
                result = input(self.inputs.ask_for_result(player_one_first_name, player_one_last_name))
                if result == "w":
                    current_match = ([player_one_id, 1], [player_two_id, 0])
                    point_distribution = False
                elif result == "l":
                    current_match = ([player_one_id, 0], [player_two_id, 1])
                    point_distribution = False
                elif result == "d":
                    current_match = ([player_one_id, 0.5], [player_two_id, 0.5])
                    point_distribution = False
                else:
                    self.messages.invalid_input()
                    continue
                round_matches.append(current_match)
        return round_matches

    def delete_tournament_db(self):
        safety_check = input(self.inputs.verify_input()).lower()
        if safety_check == "y":
            db_table_tournament.truncate()
