class ShowPlayerList:
    @staticmethod
    def show_players(player):
        print(
            f"ID:{player.player_id} "
            f"{player.last_name}, {player.first_name} "
            f"({player.gender}) - "
            f"Born: {player.birth_date} - "
            f"Rank: {player.rank}"
        )

    @staticmethod
    def show_players_headline_az():
        print("\nAll the players in the database (A - Z):\n")

    @staticmethod
    def show_players_headline_rank():
        print("\nAll the players in the database (Rank):\n")

    @staticmethod
    def show_players_az(player):
        print(
            f"{player.last_name}, {player.first_name} "
            f"({player.gender}) - "
            f"Born: {player.birth_date} - "
            f"Rank: {player.rank}"
        )

    @staticmethod
    def show_players_rank(player):
        print(
            f"Rank: {player.rank} - "
            f"{player.first_name} {player.last_name} "
            f"({player.gender}) - "
            f"Born: {player.birth_date}"
        )

    @staticmethod
    def show_player_in_tournament_az(player):
        print(
            f"{player['last_name']} {player['first_name']} - Rank: {player['rank']} - "
            f"Total points: {player['points']}"
        )

    @staticmethod
    def show_player_in_tournament_rank(player):
        print(
            f"Rank: {player['rank']} - {player['first_name']} {player['last_name']} - "
            f"Total points: {player['points']}"
        )

    @staticmethod
    def show_player_in_tournament_points(player):
        print(
            f"Total points: {player['points']} - "
            f"{player['first_name']} {player['last_name']} - "
            f"Rank: {player['rank']}"
        )
