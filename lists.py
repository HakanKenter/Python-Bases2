# -*- coding: utf-8 -*-

import statistics

'''
premiere collection de données : les listes
'''

liste = [8, 1, 7, 6, 9, 8, 4, 8, 7, 2, 0, 1]
print(liste)
print(liste[0])

'''
Exercice
- afficher le dernier element
- afficher les 5 premier elements
- afficher la somme des elements
- afficher la moyenne
- afficher le plus grand element (le maximum)
- afficher le nombre d'elements egaux à 8
- ajouter la valeur 5 à la fin de la liste
- ajouter la valeur 4 au debut de la lsite
- changer l'element d'indice 4 et le remplacer par la valeur 5
- tirer la liste dans l'ordre croissant
'''

# - afficher le dernier element
print("dernier",liste[-1])

# - afficher les 5 premier elements
print("5 premiers",liste[:5])

# - afficher la somme des elements
print("somme", sum(liste))

# - afficher la moyenne
print("moyenne", sum(liste)/len(liste))

# - afficher le plus grand element (le maximum)
print("max",max(liste))

# - afficher le nombre d'elements egaux à 8
print("nombre de 8", liste.count(8))

# - ajouter la valeur 5 à la fin de la liste
liste.append(5)
print(liste)

# - ajouter la valeur 4 au debut de la lsite
liste.insert(0, 4)
print(liste)

# - changer l'element d'indice 4 et le remplacer par la valeur 5
liste[4] = 5
print(liste)

# - tirer la liste dans l'ordre croissant
liste.sort()
print(liste)



