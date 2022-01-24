class Inputs:
    @staticmethod
    def press_key_input():
        return "(Press any key)"

    @staticmethod
    def user_choice_input():
        return "Your choice? "

    @staticmethod
    def verify_input():
        return "Are you sure (Y/N)? "

    @staticmethod
    def player_to_edit():
        return "What player do you want to edit (ID)? "

    @staticmethod
    def select_tournament():
        return "Please select the tournament (ID): "

    @staticmethod
    def tournament_for_round():
        return "You want to start/continue which tournament (ID)? "

    @staticmethod
    def player_to_add():
        return "What player do you want to add to the tournament (ID)? "

    @staticmethod
    def win_or_lose(first_name, last_name):
        return f"Was it a " \
               f"(w)in, " \
               f"(l)ose or " \
               f"(d)raw for {first_name} {last_name}? "

    @staticmethod
    def enter_last_name():
        return "Last name: "

    @staticmethod
    def enter_first_name():
        return "First name: "

    @staticmethod
    def enter_birth_date():
        return "Birthdate (DD/MM/YYYY): "

    @staticmethod
    def enter_gender():
        return "Gender (m/f): "

    @staticmethod
    def enter_rank():
        return "Rank: "

    @staticmethod
    def enter_new_rank():
        return "New Rank?: "

    @staticmethod
    def enter_tournament_name():
        return "Tournament name: "

    @staticmethod
    def enter_venue():
        return "Venue: "

    @staticmethod
    def enter_duration():
        return "How many days?: "

    @staticmethod
    def enter_start_date():
        return "Date (DD/MM/YY): "

    @staticmethod
    def enter_time_control():
        return "Choose time control:\n(a) Bullet\n(b) Blitz\n(c) Rapid" \
               "\nYour choice? "

    @staticmethod
    def enter_description():
        return "Description: "

    @staticmethod
    def ask_for_result(player_one_first_name, player_one_last_name):
        return f"Did {player_one_first_name} {player_one_last_name} " \
               f"(w)in, (l)ose or was it a (d)raw? "
