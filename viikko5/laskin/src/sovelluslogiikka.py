class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.viimeinen = 0

    def miinus(self, arvo):
        self.aseta_arvo(self.tulos - arvo)

    def plus(self, arvo):
        self.aseta_arvo(self.tulos + arvo)

    def nollaa(self, *args):
        self.aseta_arvo(0)
    
    def kumoa(self, *args):
        self.aseta_arvo(self.viimeinen)

    def aseta_arvo(self, arvo):
        self.viimeinen = self.tulos
        self.tulos = arvo
