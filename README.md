## Harjoitustyö

Tämän toistaiseksi nimettömän harjoitustyön tarkoitus on helpottaa huonekasvien ylläpitoa ja hoitoa.
Harjoitustyön käyttäjä voi viikolla 3 luoda käyttäjätunnuksen ja salasanan ohjelmaan, muttei voi
toistaiseksi kirjautua ohjelmaan sisään. Sekä käyttäjätunnukset että salasanat tallennetaan hashattuna 
parina tietokoneelle erilliseen tiedostoon. Useamman henkilön tulisi myöhemmässä vaiheessa olla mahdollista 
käyttää ohjelmaa, ja määritellä, voivatko muut samalla koneella ohjelmaa käyttävät henkilöt nähdä
hänen huonekasvinsa ja/tai myös muokata niiden tietoja.


# Toiminnan testaus

Tällä hetkellä sovelluksen toimintaa voi testata komennolla "python3 -m poetry run invoke test".

Testikattavuuden näkee komennolla "python3 -m poetry run invoke coverage-percent". Html-
tiedoston saa erikseen komennolla "python3 -m poetry run invoke coverage-report".


# Dokumentaatio

[Linkki tiedostoon maarittelydokumentti.md](https://github.com/harakanvarvas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/maarittelydokumentti.md)

[Linkki tiedostoon tyoaikakirjanpito.md](https://github.com/harakanvarvas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)
