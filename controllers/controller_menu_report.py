import controllers
import views


class ReportMenu:
    def __init__(self):
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.command = controllers.General()
        self.view = views.ReportMenuView()
        self.player_db = controllers.ShowPlayerDB()
        self.tournament_db = controllers.ShowTournamentDB()

    def display_menu(self):
        self.show_menu()
        menu_choice = input(self.inputs.user_choice_input())
        if menu_choice == "1":
            self.player_db.show_players_alphabetical()
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "2":
            self.player_db.show_players_by_rank()
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "3":
            method = "last_name"
            self.tournament_db.show_player_in_tournament(method)
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "4":
            method = "rank"
            self.tournament_db.show_player_in_tournament(method)
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "5":
            method = "points"
            self.tournament_db.show_player_in_tournament(method)
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "6":
            self.tournament_db.show_tournament_in_db()
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "7":
            self.tournament_db.show_rounds_in_tournament()
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "8":
            self.tournament_db.show_matches_in_tournament()
            input(self.inputs.press_key_input())
            return 9
        elif menu_choice == "0":
            return 99
        else:
            input(self.inputs.press_key_input())

    def show_menu(self):
        self.command.clear_screen()
        self.view.show_menu()
