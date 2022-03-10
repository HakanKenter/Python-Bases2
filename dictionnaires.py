# -*- coding: utf-8 -*-

'''
Lezs dictionnaires permettent de stocker des données repérés par des clés
'''

repertoire = {
    "Toto": "0132698425",
    "Alice": "065894268",
    "Bob": "0713239840"
}

print("Tout le repertoire", repertoire)

'''
Exercice:
- Afficher le numéro d'Alice
- Afficher tous les noms du repertoire
- Afficher tous les numéros
- Ajouter le numéro de Charlie (mettez le numéro que vous voulez)
- Modifiez le numéro de Bob
'''

# - Afficher le numéro d'Alice
print("Numéro d'Alice", repertoire["Alice"])

# - Afficher tous les noms du repertoire
print("Tous les noms du repertoire", repertoire.keys())

# - Afficher tous les numéros
print("Tous les numéros", repertoire.values())

# - Ajouter le numéro de Charlie (mettez le numéro que vous voulez)
repertoire["Charlie"] = "0762286565"
print("Ajout du numéros de Charlie", repertoire)

# - Modifiez le numéro de Bob
repertoire["Bob"] = "0762286568"
print("Modofication du numéro de Bob", repertoire)



# _____________________________________________________________________________________

'''
Exercice:
Créer un dictionnaire avec 6 élements 
dont les clés sont des noms (str)
et les valeurs des notes (float)
Mettez les noms et les notes que vous voulez
Puis afficher la moyenne de la classe
Afficher ensuite la liste des élèves classée du meilleur
au moin bon
'''

eleves = {
    "Bob": 12.8, 
    "Julien": 14.2, 
    "Moise": 18.1, 
    "Marc": 7.5, 
    "Saly": 11.5, 
    "Fred": 6.7, 
}

# afficher la moyenne de la classe
# liste = []
# for key, value in eleves.items():
#     liste.append(value)
# print("Moyenne de la classe", sum(liste)/len(eleves))

# CORRECTION
moyenne = sum(eleves.values())/len(eleves)
print("moyenne", moyenne)

# la liste des élèves classée du meilleur
# au moin bon
# for k, v in sorted(eleves.items(), key=lambda x: x[1]):
#     print("%s: %s" % (k, v))

# CORRECTION
# fonction qui prend en paramètre un couple
# qui renvoi le second element
def second(couple):
    return couple[1]

'''
On crée une liste de couples (nom, note) avec eleves.items()
et on trie cette liste dans l'ordre décroissant avec reverse=True
en utilisant la fonction second() comme critère de tri
On stocke le résultat du tri sous forme de dictionnaire
'''
notes_triees=dict(sorted(eleves.items(), key=second, reverse=True))
print("notes_triees", notes_triees)
print("classement", list(notes_triees.keys()))

# _____________________________________________________________________________________

'''
Exercice:
Afficher le diagramme en barres des notes des élèves avec matplotlib
Afficher également la moyenne sous forme de trait horizontal
'''

import matplotlib.pyplot as plt

x=list(range(6))
y=list(eleves.values())
plt.bar(x,y)
plt.xlabel("Eleves")
plt.ylabel("Note")
plt.plot(x, [moyenne for i in x], "-r")

'''
Il est possible que vous deviez ajouter cette instruction pour afficher 
le graphe'''
plt.show()
# fig = plt.figure()