#! /usr/bin/env python3
# coding: utf-8

import code_konami as script

class Test_konami:
    def __init__(self):
        self.code_a_tester = script.Resoudre_le_defis()
    
    def test_traduction(self):
        assert self.code_a_tester.traduction('↑↑↓↓←→←→BA',{'BA' : 'e', '←→' : 'm', '↓↓' : 'o', '↑↑' : 'p'}) == 'pomme'
        
    def test_enchainer(self):
        pass
        

testeur = Test_konami()
testeur.test_traduction()

