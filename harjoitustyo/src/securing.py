from passlib.hash import pbkdf2_sha256

class Securing:
    def __init__(self): #lista salatuista käyttäjänimistä ja salasanoista
        self.__securedUsernamesAndPasswords = []
        with open ("hashed.csv") as datafile: #avataan tiedosto, jossa käyttäjätunnukset ja salasanat ovat hashattuina
            for line in datafile: 
                parts = line.split(";")
                self.__securedUsernamesAndPasswords.append((parts[0], parts[1]))

    def hashing(self, username, password):
        self.__hash1 = pbkdf2_sha256.hash(username)
        self.__hash2 = pbkdf2_sha256.hash(password)

        print(self.__hash1)
        print(self.__hash2)

        if self.__hash1 not in self.__securedUsernamesAndPasswords:
            print("Not in list, let's save")
            Securing.saving(self, self.__hash1, self.__hash2)
        #elif self.__hash1 in self.__securedUsernamesAndPasswords and self.__hash2 not in self.__securedUsernamesAndPasswords:
            #Muuta salasanaa, ominaisuus tehtäväksi myöhemmässä vaiheessa

    def saving(self, username, password):
        with open ("hashed.csv", "a") as datafile:
            datafile.write(f"{username};{password}")

        with open("hashed.csv") as datafile:
            tiedosto = datafile.read()

        #print(tiedosto)

        print("Käyttäjänimi ja salasana tallennettu tiedostoon!")

    def verifying(self, username, password):  #tämän kanssa toistaiseksi ongelmia
        for user in self.__securedUsernamesAndPasswords:
            print(f"user[0] {user[0]}\n")
            if pbkdf2_sha256.verify(username, user[0]) == True:
                if pbkdf2_sha256.verify(password, user[1]) == True:
                    print("True")
                    return True
                else:
                    print("False")
                    return False

if __name__ == "__main__":
    secure = Securing()
    secure.hashing("nimi", "salasana")
    secure.verifying("nimi", "salasana")
