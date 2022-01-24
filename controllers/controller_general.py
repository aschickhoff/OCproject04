import os


class General:

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
