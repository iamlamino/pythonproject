# Mouhamadou Lamine THIAM EXAMEN PRATIQUE python  MAI 2022
import random


# Exercice  1
def bissextile():
    annee = int(input("Veuillez renseigner une année\n"))

    if annee % 4 == 0  and annee % 100 != 0:

        print(f"{annee} est bissextile")
    elif annee % 100 == 0  and annee % 400 == 0:
        print(f"{annee} est bissextile")

    else:
        print(f"{annee} est  non bissextile")

# Exercice  2


def lancerDe():

    nmbre1 = random.randit(1,7)
    print(f"premier lancer \n {nmbre1}")
    nmbre2 = random.randit(1,7)
    print(f"Second lancer \n {nmbre2}")
    print(f"la somme de {nmbre1} et de {nmbre2} est de : {nmbre1+nmbre2}")

# Exercice  2.2


def lancerDes(nombre_lancers):
    somme = 0
    print (f"nombre de lancers total : {nombre_lancers}")
    for i in range (nombre_lancers):
        lancer =random.randint(1,7)
        somme += lancer
        print(f"lancer n° {i+1} : {lancer} ")
         
    print (somme)
lancerDes(2)
lancerDes(3)

    



# Exercice  3

def suiteCarres():
    n= int(input("veuillez choisir un entier n"))
    for i in range(n+1):
        print(i*i,end='-')
    print("fin") 

# Exercice  4

def produit(n1,n2):
    if not n2>n1>1:
        print("assurez vous que le premier nombre est plus grand que le second qui est a son tour plus grand que 1")
        exit()
    result = 1
    for token in range  (n1,n2+1):
        result = result*token
    print (result)
        

# Exercice  5

def comptage(tableau):
    paires = 0 
    impaires = 0
    for elements in tableau:
        if elements % 2 == 0 :
            paires += 1
        else :
            impaires += 1 
    print(f"nombres d'éléments paires = {paires}\n nombres d'éléments impaires = {impaires}")

# Exercice  6

def decaleCircDroite(tab):
    tampon = tab[len(tab)-1]
    for i in range(len(tab)-1,0,-1):
        tab[i] = tab[i-1]
    tab[0] = tampon
    return tab



# Exercice  7

def bin2Dec(nBin):
    total = 0
    for i in range (len(nBin)) : 
            total += int(nBin[i])*2**(len(nBin)-i-1)
    print (total)
# On pourrait aussi utiliser la fonction int en mettant en paramètre la base voulue :
def bin2DecWithFunction(nBin):

    return int(nBin,base=2)
# Exercice  7.2

def dec2Bin(nDec):
    resultat = ""
    while nDec >= 2 :
        if nDec % 2 == 0:
            nDec = nDec/2
            resultat+="1"
        else : 
            nDec = (nDec-1)/2 + 1
            resultat += "0"
    match nDec :
        case 1: 
            resultat += "1"
        case 0:
            resultat += "0"
#Pareillement on peut utiliser la fonction bin ici : 

def dec2BinWithFunction(nDec):
    return bin(nDec)

# Exercice 8

def sommeRecursive():
    entier=int(input("Veuillez entrez un entier: "))
    if entier == 1:
        return 1
    else:
        return entier + sommeRecursive(entier-1)

    
        

# Exercice  9

def puissance (n,x):
    if n==0:
        return 1
    else: 
        return x*puissance(x,n-1)

# Exercice  10
def fibonacci():
    entier = int(input("Veuillez entrer un entier: "))
    if entier <= 0:
        return 0
    elif entier == 1:
        return 1
    else:
        return fibonacci(entier-1) + fibonacci(entier-2)

# Exercice  11

tableau1 = [1,2,3,4,5,6,7,8,9,10]
print(';'.join(map(str,tableau1)))

# Exercice  12

import random
def switchNumb(tab,a,b):
    if tab[b]>tab[a]:
        tampon=b
        b=a
        a=tampon
tableau2 = []
for i in range(10):
    tableau2.append(random.randint(1,100))
print(tableau2)

for i in range (len(tableau2)):
    for j in range (i+1, len(tableau2)):
        switchNumb(tableau2,i,j)
        
print (tableau2) 

# Exercice  13

def facto():
    entier = int(input("veuillez entrer un entier: "))
    if entier == 0 :
        return 1 
    else :
        return entier + facto(entier-1)
# Exercice  14
import random
def deplayWordRandomly(tab):
    sentence = ''
    for j in (tab):
        if not j in sentence:
            sentence += " "+ random.choice(tab)
    print(sentence)

