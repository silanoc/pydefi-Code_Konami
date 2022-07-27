#! /usr/bin/env python3
# coding: utf-8

import code_konami 
import pytest

class Test_konami:
    """Classe de test, pour tester les fonction du programme code_konami
    il y a 'test_' devant le nom de la méthode à tester
    """
            
    def test_zone_dico(self):
        """on sais que le dictionnaire doit faire 36 caractères."""
        self.code_a_tester = code_konami.Resoudre_le_defis()
        i = ['a'] * 100
        retour = self.code_a_tester.extraire_zone_dico(i)
        assert len (retour) == 36
        
    def test_construire_dico(self):
        """transforme une liste en dictionnaire"""
        self.code_a_tester = code_konami.Resoudre_le_defis()
        assert self.code_a_tester.construire_dico(['↓A -> n', '↓B -> u']) == {'↓A' : 'n', '↓B' : 'u'}
        
    def test_construire_message(self):
        """transforme une liste en chaine de caractère"""
        self.code_a_tester = code_konami.Resoudre_le_defis()
        assert self.code_a_tester.construire_message(['az','er']) == 'azer'
        
    def test_traduction(self):
        """teste la traduction en fonction de l'exemple du défi"""
        self.code_a_tester = code_konami.Resoudre_le_defis()
        assert self.code_a_tester.traduction('↑↑↓↓←→←→BA',{'BA' : 'e', '←→' : 'm', '↓↓' : 'o', '↑↑' : 'p'}) == 'pomme'
          
    def tout_tester(self):
        """lance tous les tests"""
        self.test_zone_dico()
        self.test_construire_dico()
        self.test_construire_message()
        self.test_traduction()
        


