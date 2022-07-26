#! /usr/bin/env python3
# coding: utf-8

import requests

class Resoudre_le_defis():
    def __init__(self):
        pass
    
    def lire_page(self, url):
        tab_ligne = []
        r = requests.get(url)
        page = r.text
        
        tab_ligne = page.split('\n')

        print(tab_ligne)
        return tab_ligne
    
    def extraire_zone_dico(self):
        pass
    
    def construire_dico(self):
        pass
    
    def extraire_zone_message(self):
        pass
        
    def traduction(self, message_code, dico):
        message_traduit = ""
        for i in range(0,len(message_code)//2):
            duo_code = message_code[i * 2 : i * 2 + 2]
            message_traduit += (dico[duo_code])
        return message_traduit
    
    def enchainer(self):
        ma_page = self.lire_page('https://pydefis.callicode.fr/defis/C22_KonamiCode/input')
        mon_pre_dico = self.extraire_zone_dico()
        mon_dico = self.construire_dico()
        mon_message = self.extraire_zone_message()
        ma_traduction = self.traduction(mon_message, mon_dico)
        return ma_traduction
        

if __name__ == "__main__":
    go = Resoudre_le_defis()
    go.lire_page('https://pydefis.callicode.fr/defis/C22_KonamiCode/input')
    #go.traduction('↑↑↓↓←→←→BA',{'BA' : 'e', '←→' : 'm', '↓↓' : 'o', '↑↑' : 'p'})
    
