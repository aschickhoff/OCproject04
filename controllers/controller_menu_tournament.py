import controllers
import views


class TournamentMenu:
    def __init__(self):
        self.view = views.TournamentMenuView()
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.command = controllers.General()
        self.create_tournament = controllers.CreateTournament()
        self.start_tournament = controllers.RunTournament()

    def display_menu(self):
        self.show_menu()
        menu_choice = input(self.inputs.user_choice_input())
        if menu_choice == "1":
            self.create_tournament.get_information()
            return 2
        elif menu_choice == "2":
            self.start_tournament.start_tournament()
            return 2
        elif menu_choice == "9":
            self.start_tournament.delete_tournament_db()
            return 2
        elif menu_choice == "0":
            return 99
        else:
            self.messages.invalid_input()
            input(self.inputs.press_key_input())

    def show_menu(self):
        self.command.clear_screen()
        self.view.show_menu()
