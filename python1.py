# -*- coding: utf-8 -*-
from random import *

"Exercice 1 calcule volume"
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
        nbre=nbre+1
        print("Gagner ! Nombre de tentative : ",nbre)
        gagner=1
"_______________________________________"

"Exercice 3"


taille=int(input("Taille du Sapin : "));
for i in range(taille):
    print(' '*(taille-1-i)+'^'*(1+2*i))

"_______________________________________"
"Exercie 4"
priceht=int(input("Prix HT :"));
while priceht!=0:
    print("Prix TTC = ",str(priceht*1,2))
    priceht=int(input("Prix HT :"));
"_______________________________________"


"Exercice 5"
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
print("Il faudrat payer : "+str(amende(po,ch,va,ami))+"€ d'amende.")
"_______________________________________"
"Exercice 6"

carac=[]
compt2=0
harp=int(input("Poid de Haruchi : "))
harno=int(input("Quantité de nourriture que Haruchi mange par jour : "))
anim=int(input("Nombre d'animaux : "))
ratiob=harno/harp
for e in range (anim) :
    numa=e+1
    caracval=str(input("Carac animaux n°"+str(numa)+" "))
    carac.append(caracval.split(" "));
for f in range (len(carac)):
     rationa=int(carac[f][1])/int(carac[f][0])
     if rationa>ratiob :
         compt2=compt2+1
print("Il y a "+str(compt2)+" d'animaux qui mangent plus que Haruhi par rapport à leurs poids.")
"_______________________________________"
