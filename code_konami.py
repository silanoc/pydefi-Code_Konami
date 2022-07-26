#! /usr/bin/env python3
# coding: utf-8

#Pour lire la page internet avec les données d'entrée
import requests 

class Resoudre_le_defis():
    def __init__(self):
        """il n'y a rien à initialiser. 
        Il n'y a pas de self.variable, que des variables privées.
        Chaque méthode retourne une valeur qui est utilisé dans ubne autre.
        Tous est dans la méthode 'enchainer'
        """
        pass
    
    def lire_page(self, url):
        """ arg :
        - url (str) : l'url contenant les données du defis
        return :
        - lst_ligne (liste) : chaque élèment de la liste correspond à une ligne de l'url"""
        
        # Mettre le contenu de la page dans une chaine de caractère. Celle ci contient des \n
        lst_ligne = []
        r = requests.get(url)
        page = r.text 
        # coupe la chaine en liste exploitable à chaque saut de ligne (\n)
        lst_ligne = page.split('\n')
        
        #print(lst_ligne)
        return lst_ligne
    
    def extraire_zone_dico(self, lst_totale):
        """retire tous ce qui correspond au début de la page html et garde tout jusqu'à la ligne de séparation
        arg :
        - lst_totale (liste) : chaque élèment correspond à une ligne de la page
        return:
        - lst_final (liste) : chaque élèment correspond à une des ligne avec les correspondance entre les bigrammes chiffré et le caractère déchiffré.
        """
        
        lst_final = lst_totale[11:47]
        #print(lst_final)
        return lst_final
    
    def construire_dico(self, lst_entree):
        """les élèments transmis n'étant pas exploitable, il s'agit de transformer les élèments en dico. 
        La clé étant la partie codé
        arg :
        - lst_entree (liste) : une liste de 36 chaine de caractère contenant le bigramme et le caratère correspondant
        return :
        - dico_retour (dictionnaire) : un dictionnaire de 36 éléments. 
        La clef étant le bigramme (deux premiers caractères), 
        et la valeur le caractère (dernier caractère)"""
        
        dico_retour = {}
        for element in lst_entree:
            dico_retour[element[0:2]] = element[-1:]
        #print(dico_retour)
        return dico_retour
    
    def extraire_zone_message(self, lst_totale):
        """Met dans une liste les élèments correspondants aux ligne sdu message codé"""
        lst_final = lst_totale[48:-4]
        #print(lst_final)
        return lst_final
    
    def construire_message(self, lst_entre):
        """simple concaténation des éléments de la liste en une chaine de caratère à traduire"""
        txt_message = "".join(lst_entre)
        #print(txt_message)
        return txt_message
        
    def traduction(self, message_code, dico):
        """la partie centrale du programme. Elle applique sur le message chiffré un déchiffrage par susbtitution, la clé étant dans le dictionnaire
        arg :
        - message_code (str) : le message à déchiffrer
        - dico (dictionnaire) : le dictionnaire faisant la correspondance entre le bigramme chiffré et le caractère déchiffré
        return :
        message_traduit (str) : le message déchiffré"""
        
        message_traduit = ""
        for bigramme in range(0,len(message_code)//2):
            duo_code = message_code[bigramme * 2 : bigramme * 2 + 2]
            message_traduit += (dico[duo_code])
        return message_traduit
    
    def enchainer(self):
        """enchaine toutes les méthodes et retourne la réponse attendue.
        return :
        - ma traduction (str) : le message en clair"""
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