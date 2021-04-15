# Harjoitustyön alustava määrittelydokumentti



__Ohjelma:__ Huonekasvien tarkkailussa ja hoidossa hyödynnettävä ohjelma, johon voi lisätä muistutuksia esimerkiksi kasvin kastelusta ja lannoituksesta.

__Ohjelmointikieli:__ Python

__Ohjelmointisuunnitelma:__ Aluksi tekstikäyttöliittymä. Kun perusominaisuudet toimivat halutusti, luodaan graafinen käyttöliittymä.

__Tiedon tallennus:__ Tiedosto, tai todennäköisemmin tietokanta. Tieto tallennetaan paikallisen koneen levylle.

__Testaus:__ Komennolla "python3 -m poetry run invoke test" tai poetry shellissä komennolla "invoke test"




## __Vaatimusmäärittely:__ 

-Ohjelman tulee toimia Linux-käyttöjärjestelmällä

-Käyttäjärooleja on vain peruskäyttäjä

-Käyttäjä voi luoda tunnuksen ohjelmaan ja määrittää salasanan tunnukselleen


-Sisäänkirjautuneena käyttäjä voi:

-Lisätä ohjelmaan kasvin, jolla on nimi tai muu ID

-Merkitä, milloin kasvi on esimerkiksi viimeksi kasteltu ja päivittää tiedon

-Poistaa huonekasvin

-Kirjautua ulos järjestelmästä

-Poistaa tunnuksensa



## __Jatkokehitysideoita:__

-Käyttäjä voi:

-Luoda huoneen ja halutessaan määritellä huoneen ominaisuudet (ikkunan suunta, valon määrä (tunnit), suora auringonvalo)

-Lisätä huonekasvin huoneeseen

-Salasanasuojata huoneensa ja/tai kasvinsa

-Lisätä huonekasville erilaisia tarpeita, mm. valo, vesi, lannoite, ilmankosteus

-Tehdä kasville ns. "vianmäärityksen" ja saada hoito-ohjeen yleisimpiin ongelmiin: kellastuneet tai nuupallaan olevat lehdet, vihannespunkit, jne.

-Mahdollisesti pitää kirjaa kuolleista kasveista ja kuolinsyystä?

-Mahdollisesti kasvinlisäysvaiheessa valita kasvin tyypin muutamasta yleisimmästä kategoriasta ja saada oletusarvoiset hoito-ohjeet kasville? 





