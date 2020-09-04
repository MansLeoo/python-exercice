# -*- coding: utf-8 -*-
from random import *
pi=3.14
r=float(input("Rayon : "))
h=float(input("hauteur : "))
resultat=(pi*(r**2)*h)/3
print("resultat :",resultat)
 

"____________________________________"
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