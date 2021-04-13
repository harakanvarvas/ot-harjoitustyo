import hashlib
from passlib.hash import sha256_crypt
class Securing:
    def __init__(self): #lista salatuista käyttäjänimistä ja salasanoista
        self.__securedUsernamesAndPasswords = []
        with open (".hashed.csv") as datafile: #avataan tiedosto, jossa käyttäjätunnukset ja salasanat ovat hashattuina
            for line in datafile: 
                parts = line.split(";")
                self.__securedUsernamesAndPasswords.append((parts[0], parts[1]))

    def hashing(self, username, password):
        self.__hash1 = sha256_crypt.encrypt(username)
        self.__hash2 = sha256_crypt.encrypt(password)

        if self.__hash1 not in self.__securedUsernamesAndPasswords:
            Securing.saving(self, self.__hash1, self.__hash2)
        #elif self.__hash1 in self.__securedUsernamesAndPasswords and self.__hash2 not in self.__securedUsernamesAndPasswords:
            #Muuta salasanaa, ominaisuus tehtäväksi myöhemmässä vaiheessa

    def saving(self, username, password):
        with open (".hashed.csv", "a") as datafile:
            datafile.write(f"{username};{password}\n")

        #print("Käyttäjänimen ja salasanan tallentaminen onnistui!")


    def verifying(self, username, password):
        self.__hash1 = sha256_crypt.encrypt(username)
        for user in self.__securedUsernamesAndPasswords:
            if self.__hash1 == user[0]:
                if sha256_crypt.verify(password, user[1]) == True:
                    return True
                else:
                    return False
