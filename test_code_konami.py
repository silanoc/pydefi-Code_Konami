#! /usr/bin/env python3
# coding: utf-8

import code_konami as script

class Test_konami:
    def __init__(self):
        self.code_a_tester = script.Resoudre_le_defis()
        
    def test_zone_dico(self):
        i = ['a'] * 100
        retour = self.code_a_tester.extraire_zone_dico(i)
        assert len (retour) == 36
        
    def test_construire_dico(self):
        assert self.code_a_tester.construire_dico(['↓A -> n', '↓B -> u']) == {'↓A' : 'n', '↓B' : 'u'}
        
    def test_construire_message(self):
        assert self.code_a_tester.construire_message(['az','er']) == 'azer'
        
    
    def test_traduction(self):
        assert self.code_a_tester.traduction('↑↑↓↓←→←→BA',{'BA' : 'e', '←→' : 'm', '↓↓' : 'o', '↑↑' : 'p'}) == 'pomme'
        
    def test_enchainer(self):
        pass
    
    def tout_tester(self):
        self.test_zone_dico()
        self.test_construire_dico()
        self.test_construire_message()
        self.test_traduction()
        
if __name__ == "__main__":     
    testeur = Test_konami()
    testeur.tout_tester()


