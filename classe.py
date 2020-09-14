# -*- coding: utf-8 -*-

#classe
from math import *
class Chrono:
    def __init__(self,h,m,s):
        "temps"
        self.heures=h
        self.minutes=m
        self.secondes=s
    def afficher(self):
        "affichage du temps"
        return (str(self.heures)+"h"+str(self.minutes)+"m"+str(self.secondes)+"s")
    
t=Chrono(21,34,55)
print(t.afficher())

class Dinosaure:
    def __init__(self,long,haut,poid,vitesseM):
        self.__longueur=long
        self.__hauteur=haut
        self.__poids=poid
        self.__vitesseMax=vitesseM
    def carac(self):
        print("\nLongueur: "+str(self.__longueur)+" \n"+  
              "Hauteur: "+str(self.__hauteur)+" \n"+ 
              "Poids: "+str(self.__hauteur)+" \n"+ 
              "Vitesse Max: "+str(self.__vitesseMax)+" km/h ")
    def get_long(self):
        return self.__longueur
    def set_long(self,l):
        self.__longueur=l
    def get_haut(self):
        return self.__hauteur
    def set_haut(self,h):
        self.__hauteur=h
    def get_poid(self):
        return self.__poids
    def set_poid(self,p):
        self.__poids=p
    def get_vitesseM(self):
        return self.__vitesseMax
    def set_vitessM(self,v):
        self.__vitesseMax=v
"""   
triceratops=Dinosaure(9,3,9,32)
triceratops.carac()
tyranosaurus=Dinosaure(13,8,6,27)
tyranosaurus.carac()
print(triceratops.get_long())
triceratops.set_long(3)
print(triceratops.get_long())
"""








class Point :
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rho=self.calcul_rho()
        self.theta=self.calcul_Theta()
        
    def calcul_rho(self):
        self.rho=sqrt(self.x**2+self.y**2)
    
            
    def calcul_Theta(self):
        if self.x>0:
            self.theta=atan(self.y/self.x)
            print(self.theta)
        if self.x<0 and self.y>=0:
            self.theta=atan(self.y/self.x)+pi
        if self.x<0 and self.y<0:
            self.theta=atan(self.y/self.x)-pi
        if self.x==0 and self.y>0:
            self.theta=pi/2
        if self.x==0 and self.y>0:
            self.theta=-pi/2
        if self.x==0 and self.y==0:
            self.theta=0
    def get_x(self):
       return self.x
    def get_y(self):
        return self.y
    def get_theta(self):
        return self.theta
    def get_rho(self):
        return self.rho
result=Point(10,50)

print(result.get_theta())
print(result.get_x())
print(result.get_y())
print(result.get_rho())