# -*- coding: utf-8 -*-
from random import *
"""
"Exercice 1"
pi=3.14
r=float(input("Rayon : "))
h=float(input("hauteur : "))
resultat=(pi*(r**2)*h)/3
print("resultat :",resultat)
 

"____________________________________"
"Exercice 2"
gagner=0
rep=randint(0,100)

nbre=0
while gagner !=1 :
    userep=int(input("Quelle le nombre generer ?"))
    if userep>rep:
        print("Nombre trop grand !");
        nbre=nbre+1
    if userep<rep : 
        print("Nombre trop petit !");
        nbre=nbre+1
    if userep==rep :
        print("Gagner ! Nombre de tentative : ",nbre)
        gagner=1
"_______________________________________"

"Exercice 3"


taille=int(input("Taille du Sapin : "));
for i in range(taille):
    print(' '*(taille-1-i)+'^'*(1+2*i))
    
"""    
def amende(poule,chiens,vache,ami) :
    pointperdu=poule*1+chiens*3+vache*5+ami*10
    point=pointperdu/100
    print(point)
    if point<1:
        return 0
    elif point>1 :
        return 200*int(point)
    else :
        return 200


po=int(input("Combien de poules tuées ?"))
ch=int(input("Combien de chiens tués ?"))
va=int(input("Combien de vaches tuées ? "))
ami=int(input("Combien d'amis tués ? "))
print("Il faudrat payer :"+str(amende(po,ch,va,ami))+"€ d'amende.")
    