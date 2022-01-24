import views
import controllers


class PlayerMenu:
    def __init__(self):
        self.view = views.PlayerMenuView()
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.command = controllers.General()
        self.create_player = controllers.CreatePlayer()
        self.show_player = controllers.ShowPlayerDB()
        self.edit_player = controllers.EditPlayer()

    def display_menu(self):
        self.show_menu()
        menu_choice = input(self.inputs.user_choice_input())
        if menu_choice == "1":
            self.create_player.get_information()
            return 1
        elif menu_choice == "2":
            self.show_player.show_players_in_db()
            input(self.inputs.press_key_input())
            return 1
        elif menu_choice == "3":
            self.edit_player.edit_player_rank()
            input(self.inputs.press_key_input())
            return 1
        elif menu_choice == "9":
            # self.db.delete_players_db()
            return 1
        elif menu_choice == "0":
            return 99
        else:
            self.messages.invalid_input()
            input(self.inputs.press_key_input())

    def show_menu(self):
        self.command.clear_screen()
        self.view.show_menu()
