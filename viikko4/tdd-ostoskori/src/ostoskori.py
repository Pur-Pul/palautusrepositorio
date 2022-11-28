from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        summa = 0
        for ostos in self.__ostokset.values():
            summa+=ostos.lukumaara()
        return summa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.__ostokset.values():
            summa+=ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self.__ostokset:
            self.__ostokset[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self.__ostokset[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() in self.__ostokset:
            self.__ostokset[poistettava.nimi()].muuta_lukumaaraa(-1)
            if self.__ostokset[poistettava.nimi()].lukumaara() == 0:
                self.__ostokset.pop(poistettava.nimi())

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.__ostokset = {}

    def ostokset(self):
        return list(self.__ostokset.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
