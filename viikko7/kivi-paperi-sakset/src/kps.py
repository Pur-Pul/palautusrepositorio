from peli import Peli
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class KPS(Peli):
    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def luo_helppo_yksinpeli():
        return KPSTekoaly()
    
    @staticmethod
    def luo_vaikea_yksinpeli():
        return KPSParempiTekoaly()