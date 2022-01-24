import views
import controllers


class Application:
    def __init__(self):
        self.running = True
        self.current_menu = controllers.MainMenu()

    def application_start(self):
        while self.running:
            menu_option = self.current_menu.display_menu()
            self.menu_choice(menu_option)

    def menu_choice(self, menu_option):
        if menu_option == 1:
            self.current_menu = controllers.PlayerMenu()
        elif menu_option == 2:
            self.current_menu = controllers.TournamentMenu()
        elif menu_option == 9:
            self.current_menu = controllers.ReportMenu()
        elif menu_option == 99:
            self.current_menu = controllers.MainMenu()
        elif menu_option == 0:
            views.Messages.exit_message()
            self.running = False
        else:
            return
