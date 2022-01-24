import views
import controllers


class MainMenu:
    def __init__(self):
        self.view = views.MainMenuView()
        self.messages = views.Messages()
        self.inputs = views.Inputs()
        self.command = controllers.General()

    def display_menu(self):
        self.show_menu()
        menu_choice = input(self.inputs.user_choice_input())
        if menu_choice == "1":
            return 1
        elif menu_choice == "2":
            return 2
        elif menu_choice == "9":
            return 9
        elif menu_choice == "0":
            return 0
        else:
            self.messages.invalid_input()
            input(self.inputs.press_key_input())

    def show_menu(self):
        self.command.clear_screen()
        self.view.show_menu()
