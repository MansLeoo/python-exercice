# -*- coding: utf-8 -*-
def somme(n:int)->int:
        """
        Renvois la somme des n premier entiers.
        """
        assert type(n)==int,"n doit être un entier"
        assert n<0,"n doit être superieur à zero."
        somme=0
        if n==0:
             return 0
        else :
             for i in range(1,n+1):
                 somme+=i
             return somme

def somme2(n:int)->int:
    if n==0:
        return 0
    else :
        return n+somme2(n-1)


def fact(n:int)->int :
    """
     fonction qui correspond au calcul de la fonction factorielle n! 
    """
    assert type(n)==int,"n doit être un entier"
    assert n<0,"n doit être superieur à zero."
    for i in range(1, n):
         if n==0:
             return 0
         else :
             n=n*i
    return n
def fact2(n:int)->int :
    """
     fonction qui correspond au calcul de la fonction factorielle n! 
    """
    assert type(n)==int,"n doit être un entier"
    assert n<0,"n doit être superieur à zero."
    if n==0:
             return 1
    else :
             return n*fact2(n-1)


def boucle(de:int,arr:int)->list:
    n=[]
    for i in range(de,arr+1):
       n.append(i)
    return n
def boucle2(de:int,arr:int):
    if de==arr:
             print(de)
    else :
            boucle2(de+1,arr)
            print(de)
    return 



#exerciceC5

def fibonacci(f0:int, f1:int):
    if f1 < 7502 :
        a = f1
        f1 = f0 + f1
        f0 = a
        return fibonacci(f0,f1)
    else :
        return f0,f1
def fibonacci2(f0:int,f1:int,n:int):
    for i in range(2,n+1):
        a=f1
        f1 = f0 + f1
        f0 = a
        print("f",str(i),":",f1)
def fibo_rec(n): 
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

    
    
    
    
f0 = 0
f1 = 1
fibonacci2(f0,f1,25)
print(fibonacci(f0,f1))

def multiplication(x,y):
    if x==0 :
        return 0
    elif x % 2 == 0:
        return multiplication((x//2),(y+y))
    else:
        return multiplication((x//2),(y+y)+y)
    