#from securing import Securing

class SignIn:

    def __init__(self):

        #self.securing = Securing() #salasanojen salaus tulee ominaisuudeksi myöhemmin

        with open ("usernames.txt") as datafile: 
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
                    print("Asetetaan käyttäjätunnukselle salasana.")
                    SignIn.signInSetPassword(self, username)
                    print("Käyttäjätunnus ja salasana asetettu onnistuneesti!")
                    break


                    
    def signInSetPassword(self, username):
        #secure = Securing()
        while True:
            password = input("Anna salasana (väh. 8 merkkiä): ")
            if len(password) < 8:
                print("Salasana ei ollut vaaditun pituinen. Yritä uudestaan.")
            else:
                #secure.hashing(username, password)
                while True:
                    password_again = input("Anna salasana uudestaan: ")
                    if password_again == password:
                        with open ("usernames.txt", "a") as datafile:
                            datafile.write(f"{username};{password}\n")
                        break
                    else:
                        print("Salasana ei ollut sama. Yritä uudelleen.")
                
                break
                
                #value = secure.verifying(username, password_again)
                #print(value)
                #if value == True:
                #    print("Käyttäjätunnuksen ja salasanan asettaminen onnistui!")


#if __name__ == "__main__":
#    kirjaudu = SignIn()
#    kirjaudu.perform()