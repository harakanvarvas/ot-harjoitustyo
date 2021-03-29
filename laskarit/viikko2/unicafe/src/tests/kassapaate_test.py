import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_saldo_on_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_myytyja_edullisia_lounaita_oikein(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_myytyja_maukkaita_lounaita_oikein(self):
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_kateisosto_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_kateisosto_edullinen_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")


    def test_kateisosto_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_kateisosto_maukkaat_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")


    def test_korttiosto_edullinen(self):
        self.kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_korttiosto_edullinen_ei_tarpeeksi_rahaa(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_korttiosto_maukas(self):
        self.kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_korttiosto_maukas_ei_tarpeeksi_rahaa(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_ladataan_kortille_rahaa(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 2000)
        
    def test_ladataan_kortille_negatiivista_rahaa(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -2000)