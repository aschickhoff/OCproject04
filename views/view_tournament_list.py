class ShowTournamentList:
    @staticmethod
    def show_tournament(tournament):
        print(
            f"Tournament ID: {tournament.tournament_id}\n"
            f"Name: {tournament.tournament_name}\n"
            f"Venue: {tournament.venue}\n"
            f"Start date: {tournament.start_date}\n"
            f"End date: {tournament.end_date}\n"
            f"Time Control: {tournament.time_control}\n"
            f"Amount of rounds: {tournament.amount_of_rounds}\n"
            f"Description: {tournament.description}\n"
        )

    @staticmethod
    def show_tournament_rounds(active_round):
        print(f"{active_round.round_name} - From: {active_round.start_time} "
              f"to {active_round.end_time}")

    @staticmethod
    def show_matches_tournament(player_one, player_two, status_one, status_two):
        print(f"{player_one.first_name} {player_one.last_name} "
              f"({status_one}) vs {player_two.first_name} "
              f"{player_two.last_name} ({status_two})"
              )

    @staticmethod
    def current_match(
            player_one_first_name,
            player_one_last_name,
            player_two_first_name,
            player_two_last_name
    ):
        print(f"{player_one_first_name} {player_one_last_name} "
              f"vs "
              f"{player_two_first_name} {player_two_last_name}")
