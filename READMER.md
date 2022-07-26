#Date : 26 juillet 2022
#author : silanoc

Code permettant de réoudre le défis 'code Konami' sur le site pydefis.callicode
https://pydefis.callicode.fr/defis/C22_KonamiCode/txt

En plus de répondre simplement au défi, il a été construit avec le module de test 'Pytest'.

En s'inspirant de la méthode 'Test-Driven Development'
- A quasi chaque méthode, j'ai d'abord mis un test avant de la développer. Ce qui donne des red flag
- le code fonctionnant, c'est du green.
- une fois que tous les tests sont au vert, j'ai refactorisé.

fichiers joints :
- code_konami.py : le code principal
- test_code_konami.py : le fichier de test
- require.txt : issus de pip freeze (environnement avec venv)

