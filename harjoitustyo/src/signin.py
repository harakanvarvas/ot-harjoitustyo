from securing import Securing

class SignIn:

    def __init__(self):

        with open ("usernames.txt") as datafile: #Salaamattomat käyttäjänimet
            self.__usernames_list = datafile.read()

    def perform(self):
        SignIn.commandSignIn(self)


    def commandSignIn(self): #käyttäjätunnuksen ja salasanan valinnasta omat metodinsa
        while True:

            username = input("Anna käyttäjänimi: ")
            if username in self.__usernames_list:
                print("Käyttäjänimi on varattu.")
                continue

            elif username not in self.__usernames_list:
                print("Käyttäjänimi on vapaa. \n")
                command = input("Valitaanko käyttäjätunnus? y/n ")
                if command == "n" or command == "N":
                    command2 = input("Valitaanko toinen käyttäjätunnus? y/n ")
                    if command2 == "y" or command2 == "Y":
                        continue
                    elif command2 == "n" or command2 == "N":
                        print("Käyttäjätunnuksen luominen peruutettiin.")
                        break

                elif command == "y" or command == "Y":
                    with open ("usernames.txt", "a") as datafile:
                        datafile.write(f"{username}\n")

                    print("Asetetaan käyttäjätunnukselle salasana.")
                    SignIn.signInSetPassword(self, username)
                    break


                    
    def signInSetPassword(self, username):
        while True:
            password = input("Anna salasana (väh. 8 merkkiä): ")
            if len(password) < 8:
                print("Salasana ei ollut vaaditun pituinen. Yritä uudestaan.")
            else:
                Securing.hashing(self, username, password)
                password_again = input("Anna salasana uudestaan: ")
                value = Securing.verifying(self, username, password_again)
                if value == True:
                    print("Käyttäjätunnuksen ja salasanan asettaminen onnistui!")
