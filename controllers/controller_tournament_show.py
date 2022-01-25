from tinydb import TinyDB
import views
import models

db = TinyDB("chess.json")
db_table_player = db.table("players")
db_table_tournament = db.table("tournaments")


class ShowTournamentDB:
    def __init__(self):
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.show_list = views.ShowTournamentList()
        self.show_player_list = views.ShowPlayerList()

    def show_tournament_in_db(self):
        available_tournaments = []
        for tournaments in db_table_tournament.all():
            available_tournaments.append(models.Tournament.deserialize_tournament(tournaments))
        for tournament in available_tournaments:
            self.show_list.show_tournament(tournament)
        return len(available_tournaments)

    @staticmethod
    def show_player_in_db(player_id):
        player_from_db = db_table_player.get(doc_id=int(player_id))
        player = models.Player.deserialize_player(player_from_db)
        return player

    def show_player_in_tournament(self, method):
        tournament = self.select_tournament()
        rounds_in_tournament = tournament.rounds
        rounds_serialized = []
        for i in range(len(rounds_in_tournament)):
            rounds_serialized.append(rounds_in_tournament[i].serialize_round())
        listed_players = tournament.players
        players_updated = self.calculate_points(rounds_serialized, listed_players)
        for i in range(8):
            if method == "rank":
                players_sorted = sorted(players_updated, key=lambda contestant: contestant[method])
                self.show_player_list.show_player_in_tournament_rank(players_sorted[i])
            elif method == "last_name":
                players_sorted = sorted(players_updated, key=lambda contestant: contestant[method])
                self.show_player_list.show_player_in_tournament_az(players_sorted[i])
            else:
                players_sorted = sorted(players_updated, key=lambda contestant: contestant[method], reverse=True)
                self.show_player_list.show_player_in_tournament_points(players_sorted[i])

    def show_rounds_in_tournament(self):
        tournament = self.select_tournament()
        rounds_in_tournament = tournament.rounds
        for i in range(len(rounds_in_tournament)):
            self.show_list.show_tournament_rounds(rounds_in_tournament[i])

    def show_matches_in_tournament(self):
        tournament = self.select_tournament()
        rounds_in_tournament = tournament.rounds
        rounds_serialized = []
        self.messages.blank_line()
        for i in range(len(rounds_in_tournament)):
            rounds_serialized.append(rounds_in_tournament[i].serialize_round())
        for i in range(len(rounds_serialized)):
            matches = rounds_serialized[i]["matches"]
            self.show_list.show_tournament_rounds(rounds_in_tournament[i])
            for n in range(len(matches)):
                status_one = None
                status_two = None
                player_id_one = matches[n][0][0]
                player_id_two = matches[n][1][0]
                player_one = self.show_player_in_db(player_id_one)
                player_two = self.show_player_in_db(player_id_two)
                if matches[n][0][1] == 1:
                    status_one = "won"
                    status_two = "lost"
                elif matches[n][0][1] == 0:
                    status_one = "lost"
                    status_two = "won"
                elif matches[n][0][1] == 0.5:
                    status_one = "draw"
                    status_two = "draw"
                self.show_list.show_matches_tournament(player_one, player_two, status_one, status_two)
            self.messages.blank_line()

    def select_tournament(self):
        self.show_tournament_in_db()
        tournament_id = input(self.inputs.select_tournament())
        if tournament_id.isdigit():
            result = db_table_tournament.get(doc_id=int(tournament_id))
            tournament = models.Tournament.deserialize_tournament(result)
            return tournament
        else:
            self.messages.invalid_input()

    @staticmethod
    def calculate_points(rounds_serialized, listed_players):
        players = []
        for i in range(len(listed_players)):
            players.append(db_table_player.get(doc_id=int(listed_players[i])))
        available_players = []
        for player in players:
            available_players.append(models.Player.deserialize_player(player))
        for player in available_players:
            total_points = 0
            for i in range(len(rounds_serialized)):
                matches = rounds_serialized[i]["matches"]
                for n in range(len(matches)):
                    if matches[n][0][0] == player.player_id:
                        total_points = total_points + matches[n][0][1]
                    elif matches[n][1][0] == player.player_id:
                        total_points = total_points + matches[n][1][1]
            player.points = float(total_points)
            db_table_player.update({"points": player.points}, doc_ids=[player.player_id])
            players = []
            for i in range(len(listed_players)):
                players.append(db_table_player.get(doc_id=int(listed_players[i])))
        return players
