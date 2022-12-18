from tekoaly import Tekoaly
from peli import Peli

class KPSTekoaly(Peli):
    def __init__(self):
        super().__init__()
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self):
        valinta = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {valinta}")
        return valinta
