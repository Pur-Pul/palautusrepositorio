
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.ljono:
            return True
        return False

    def ljono_taynna(self):
        return self.alkioiden_lkm == len(self.ljono)

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.ljono_taynna():
                self.ljono += [0]*self.kasvatuskoko

    def poista(self, luku):
        if luku in self.ljono:
            self.ljono.remove(luku)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
        
    def yhdista(self, int_list):
        for luku in int_list:
            self.lisaa(luku)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[0:self.alkioiden_lkm]

    def yhdiste(joukko_a, joukko_b):
        joukko_a.yhdista(joukko_b.to_int_list())
        return joukko_a

    def leikkaus(joukko_a, joukko_b):
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()
        for luku in a_taulu:
            if luku not in b_taulu:
                joukko_a.poista(luku)
        return joukko_a

    def erotus(joukko_a, joukko_b):
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()
        for luku in a_taulu:
            if luku in b_taulu:
                joukko_a.poista(luku)
        return joukko_a

    def __str__(self):
        return str(self.to_int_list()).replace("[", "{").replace("]", "}")
