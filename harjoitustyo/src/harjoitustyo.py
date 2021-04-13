from signin import SignIn

COMMANDS = {
    "lopeta": "Lopeta ohjelman suorittaminen.",
    #"kirjaudu": "Kirjaudu sisään olemassaolevalla tunnuksella.",
    "luo tunnus": "Luo uusi tunnus ja salasana kirjautuaksesi sisään."
}

class PracticeWork:

    def __init__(self):
        signin = SignIn()

        self._commands = {
            #"lopeta": CommandStop(),
            #"kirjaudu": LogIn.CommandLogIn(),
            "luo tunnus": signin,
        }

    def start(self):
        print(COMMANDS)
        while True:
            command = input("Anna komento: ")

            if command == "lopeta":
                break

            if command not in self._commands:
                print("Virheellinen komento.")
                command = input("Tulostetaanko komennot uudestaan? y/n")

                if command == "Y" or command == "y":
                    print("Komennot: ", COMMANDS)
                elif command == "N" or command == "n":
                    continue


            chosen_command = self._commands[command]
            chosen_command.perform()

if __name__ == "__main__":
    work = PracticeWork()
