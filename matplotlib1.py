# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

'''
plot(x,y) trace une courbe en reliant les points
où x est la liste des abscisses et y celles des ordonnées
x et y DOIVENT avoir la même taillz
'''
plt.plot([1,2,7,8,9,13], [3,7,-1,0,2,3])

'''
On peut spécifier la couleur, le type de trait et la forme des points
avec un troisième paramètre de type str

Premier caractère : couleur (r,g,b,y,k, ....)
Deuxième caractère : forme des symboles (+,x,o,^,....)
Enfin, le type de trait (- trait plein, -- pointillés)
'''
plt.plot([1,2,3,4,5,6],[5,3,0,5,8,4], "rx--")

# To Show
plt.show()