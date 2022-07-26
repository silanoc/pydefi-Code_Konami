**Date** : 26 juillet 2022

**author** : silanoc

## Description
Code permettant de résoudre le défi 'code Konami' sur le site pydefis.callicode
https://pydefis.callicode.fr/defis/C22_KonamiCode/txt

## Méthodologie
En plus de répondre simplement au défi, il a été construit avec le module de test 'Pytest'.
https://openclassrooms.com/fr/courses/4425126-testez-votre-projet-avec-python/4435144-ajoutez-des-tests-avec-pytest

En s'inspirant de la méthode 'Test-Driven Development'
https://openclassrooms.com/fr/courses/4425126-testez-votre-projet-avec-python/4435374-decouvrez-le-test-driven-development
- À quasi chaque méthode, j'ai d'abord mis un test avant de la développer. Ce qui donne des red flag
- le code fonctionnant, c'est du green flag.
- une fois que tous les tests sont au vert, j'ai refactorisé.

## fichiers joins :
- code_konami.py : le code principal
- test_code_konami.py : le fichier de test
- require.txt : issus de pip freeze (environnement avec venv)

