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
        #print(tab_ligne)
        return tab_ligne
    
    def extraire_zone_dico(self, lst_totale):
        lst_final = lst_totale[11:47]
        #print(lst_final)
        return lst_final
    
    def construire_dico(self, lst_entree):
        dico_retour = {}
        for i in lst_entree:
            dico_retour[i[0:2]] = i[-1:]
        #print(dico_retour)
        return dico_retour
    
    def extraire_zone_message(self, lst_totale):
        lst_final = lst_totale[49:-4]
        #print(lst_final)
        return lst_final
    
    def construire_message(self, lst_entre):
        txt_message = "".join(lst_entre)
        #print(txt_message)
        return txt_message
        
    def traduction(self, message_code, dico):
        message_traduit = ""
        for i in range(0,len(message_code)//2):
            duo_code = message_code[i * 2 : i * 2 + 2]
            message_traduit += (dico[duo_code])
        return message_traduit
    
    def enchainer(self):
        ma_page = self.lire_page('https://pydefis.callicode.fr/defis/C22_KonamiCode/input')
        mon_pre_dico = self.extraire_zone_dico(ma_page)
        mon_dico = self.construire_dico(mon_pre_dico)
        mon_pre_message = self.extraire_zone_message(ma_page)
        mon_message = self.construire_message(mon_pre_message)
        ma_traduction = self.traduction(mon_message, mon_dico)
        return ma_traduction
        

if __name__ == "__main__":
    go = Resoudre_le_defis()
    print(go.enchainer())
    #go.traduction('↑↑↓↓←→←→BA',{'BA' : 'e', '←→' : 'm', '↓↓' : 'o', '↑↑' : 'p'})
    
