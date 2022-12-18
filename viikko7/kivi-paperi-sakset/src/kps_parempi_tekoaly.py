from peli import Peli
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(Peli):
    def __init__(self):
        super().__init__()
        self._tekoaly_parannettu = TekoalyParannettu(10)
    
    def _toisen_siirto(self):
        valinta = self._tekoaly_parannettu.anna_siirto()
        print(f"Tietokone valitsi: {valinta}")
        return valinta
    
    def _aseta_siirto(self, siirto):
        self._tekoaly_parannettu.aseta_siirto(siirto)
