# -*- coding: cp1252 -*-
import random
## random.randint(1,1000)

##Ecrire une méthode tirer(mini, maxi) qui tire un nombre au hasard
##entre mini et maxi

def tirer(min, max):
    if min >=0 and max >=1:
        return random.randint(min, max)

## print tirer(1,100)

##Ecrire une méthode tirerD6 qui fait tirer un dé à 6 faces
def tirerD6():
    return tirer(1,6)

## print tirerD6()

##Ecrire une boucle de 100 tests de la fonction tirer
##Elle affiche False si la valeur aléatoire tirée n'est pas comprise
##dans l'intervalle souhaité et affiche la valeur obtenue quand
##celle-ci est une des valeurs extrêmes

def boucleDeTest():
    for i in range(100):
        tirerD6

##Faire une méthode qui lit un nombre saisi au clavier
## input("entrez un nombre")

def lireChiffreClavier():
    nombreChoisit = input("Entrez un nombre ")
    print "Le nombre choisit est " , nombreChoisit
    return nombreChoisit

##Faire une méthode comparer(nombre, cible) qui retourne une chaine de caractères
##indiquant si la cible est "plus petit" "plus grand" ou "égal" à nombre

def comparer(nombre, cible):
    message = "Le nombre de l'ordinateur est plus grand que celui du joueur"
    if cible < nombre:
        message = "Le nombre de l'ordinateur est plus petit que celui du joueur"
    elif cible == nombre:
        message = "Le nombre de l'ordinateur est egal a celui du joueur"
    return message

##Plus ou moins ?
##Faire une méthode qui tire un nombre cible au hasard sur
##un intervalle donné puis demande à un joueur un nombre pour lui indiquer si
##la cible est plus petite ou plus grande que sa proposition.

def plusOuMoins():
    nombreCible = tirerD6()
    nombreJoueur = lireChiffreClavier()
    print comparer(nombreJoueur, nombreCible)

##Faire un programme qui boucle jusqu'à ce que la cible ait été trouvée

def plusOuMoinsUntilVictory():
    nombreCible = tirerD6()
    nombreJoueur = lireChiffreClavier()
    while(nombreJoueur != nombreCible):
        comparer(nombreJoueur, nombreCible)
        nombreJoueur = lireChiffreClavier()
    comparer(nombreJoueur, nombreCible)

# plusOuMoinsUntilVictory()

##Faire un programme qui retourne, en plus, le nombre de tentatives effectuées

def plusOuMoinsUntilVictoryCount():
    nombreCible = tirerD6()
    nombreJoueur = lireChiffreClavier()
    tentative = 1
    while(nombreJoueur != nombreCible):
        tentative += 1
        comparer(nombreJoueur, nombreCible)
        nombreJoueur = lireChiffreClavier()
    comparer(nombreJoueur, nombreCible)
    print str(tentative) + " tentative(s)"

# plusOuMoinsUntilVictoryCount()

##Faire une méthode qui recherche par dichotomie la valeur tirée au hasard sur
##un intervalle donné en affichant chaque proposition faite et en affichant
##le nombre d'essais.

def estPlusGrand(aDeviner,rechercheNombre):
    print "Le nombre a deviner est egal a " + str(aDeviner) + " alors que le nombre trouve est egal a " + str(rechercheNombre) 
    return (aDeviner > rechercheNombre)


def rechercheDichotomiePourrie(min, max):
    if(min < max):
        nombreADeviner = tirer(min,max)
        rechercheNombreMin = min
        rechercheNombreMax = max
        rechercheNombre = tirer(rechercheNombreMin,rechercheNombreMax)

        compteur = 1
        while(nombreADeviner != rechercheNombre):
            if(estPlusGrand(nombreADeviner, rechercheNombre)):
                rechercheNombreMin = rechercheNombre
                rechercheNombre = tirer(rechercheNombreMin +1,rechercheNombreMax)
            else:
                rechercheNombreMax = rechercheNombre
                rechercheNombre = tirer(rechercheNombreMin,rechercheNombreMax -1)
            compteur += 1

        else:
            print "Trouve apres " + str(compteur) + " fois."
            return compteur #ajout pour la suite

# rechercheDichotomiePourrie(1,100)

def rechercheDichotomie(min, max):
    if(min < max):
        nombreADeviner = tirer(min,max)
        rechercheNombreMin = min
        rechercheNombreMax = max
        rechercheNombre = (rechercheNombreMin + rechercheNombreMax) / 2
        compteur = 1
        while(nombreADeviner != rechercheNombre):
            if(estPlusGrand(nombreADeviner, rechercheNombre)):
                rechercheNombreMin = rechercheNombre +1
            else:
                rechercheNombreMax = rechercheNombre -1
            rechercheNombre = (rechercheNombreMin + rechercheNombreMax) / 2
            compteur += 1

        else:
            print "Trouve apres " + str(compteur) + " fois."
            return compteur #ajout pour la suite

rechercheDichotomie(0,100)

##Bonus, regarder combien de coups, en moyenne, le programme utilise pour
##trouver la réponse. Tester sur 100000 parties.

def moyenneCompteurVictoire():
    countCompteurs = 0
    for i in range (100) :
        countCompteurs += rechercheDichotomie(1,100)
    moyenne = countCompteurs / 100
    print "En moyenne pour min 1 et max 100, l'ordinateur trouve en " + str(moyenne) + " coups"

# moyenneCompteurVictoire()

##Faire une méthode qui affiche un chiffre sous la forme d'un dé sur trois lignes.
##      *     *     * *   * *   * *
## *           *           *    * *
##        *     *   * *   * *   * *

def afficherChiffre(valeur):
    if(valeur >= 1 and valeur <=6):
        chiffre = "\n *\n"
        if(valeur == 2):
            chiffre = "*\n\n  *"
        elif(valeur == 3):
            chiffre = "*\n *\n  *"
        elif(valeur == 4):
            chiffre = "* *\n\n* *"
        elif(valeur == 5):
            chiffre = "* *\n *\n* *"
        elif(valeur == 6):
            chiffre = "* *\n* *\n* *"
    print chiffre

# afficherChiffre(tirerD6())


##Yams / Yathzee
##Faire une méthode qui génère une liste de 5 chiffres correspondant à un jet
##de 5 dés

def liste5Des():
    liste = []
    for i in range(5):
        liste.append(tirerD6())
    print liste
    return liste

# liste5Des()

##Faire une méthode estYams(liste) qui indique si une liste de 5 chiffres
##contient 5 fois le même chiffre

def estYams(liste):
    chiffreRef = liste[0]
    estYams = True
    for i in range(1,len(liste)):
        if(chiffreRef != liste[i] and estYams):
            estYams = False
    return estYams

# print estYams(liste5Des())

##Faire une méthode compter(liste, valeur) qui compte le nombre d'apparition de
##"valeur" dans la liste de dés

def countValeur(liste, valeur):
    if(valeur >= 1 and valeur <= 6):
        compteur = 0
        for i in range (0, len(liste)):
            if(liste[i] == valeur):
                compteur +=1
        print "On retourve la valeur " + str(valeur) + " ce nombre de fois : " + str(compteur)
        return compteur

# countValeur(liste5Des(), 2)

##Faire une méthode sommeValeurs(liste, valeur) qui retourne la somme des
##dés de la liste de "valeur"

def sommeValeur(liste, valeur):
    compteur =  countValeur(liste, valeur)
    somme = compteur * valeur
    print "La somme des valeurs vaut " + str(somme)
    return somme

# sommeValeur(liste5Des(), 2)

##Faire une méthode qui indique si la liste contient au moins un brelan (3)

def brelan(liste):
    estBrelan = False
    chiffreBrelan = 0
    for i in range(1, 7):
        if(countValeur(liste, i) == 3 and not estBrelan):
            estBrelan = True
            chiffreBrelan = i
    if(estBrelan):
        print "Il y a un brelan de " + str(chiffreBrelan)
    return (estBrelan, chiffreBrelan)
    
# print brelan(liste5Des())[0]

##Faire une méthode qui indique si la liste contient au moins un carré (4)

def carre(liste):
    estCarre = False
    chiffreCarre = 0
    for i in range(1, 7):
        if(countValeur(liste, i) == 4 and not estCarre):
            estCarre = True
            chiffreCarre = i
    if(estCarre):
        print "Il y a un brelan de " + str(chiffreCarre)
    return estCarre

# carre(liste5Des())

##Faire une méthode qui indique si la liste contient au moins un full (3 et 2)

def full(liste):
    estFull2 = False
    estFull3 = False
    chiffreFull2 = 0
    chiffreFull3 = 0
    for i in range(1, 7):
        if(countValeur(liste, i) == 3 and not estFull3):
            estFull3 = True
            chiffreFull3 = i
        if(countValeur(liste, i) == 2 and not estFull2):
            estFull2 = True
            chiffreFull2 = i
    if(estFull2 and estFull3):
        print "Il y a un full : 2 des " + str(chiffreFull2) + " et 3 des " + str(chiffreFull3)
        print "-------------------------------------------------------------------------------"
    return (estFull2 and estFull3)

# full(liste5Des())

##Faire une méthode qui indique si la liste contient une petite suite (4 valeurs)
def petitSuite(liste):
    listeDansOrdre = sorted(liste)
    chiffreRef  = liste[0]
    compteur = 1
    estPetitSuite = False
    for i in range(1, len(listeDansOrdre)):
        if(chiffreRef +1 == listeDansOrdre[i]):
            chiffreRef += 1
            compteur += 1
        elif(chiffreRef == listeDansOrdre[i]):
            pass
        else:
            compteur = 0
    if(compteur == 4):
        estPetitSuite = True
    return estPetitSuite

# print petitSuite(liste5Des())

##Faire une méthode qui indique si la liste contient une grande suite (5 valeurs)

def grandeSuite(liste):
    listeDansOrdre = sorted(liste)
    chiffreRef  = liste[0]
    compteur = 1
    estGrandeSuite = False
    for i in range(1, len(listeDansOrdre)):
        if(chiffreRef +1 == listeDansOrdre[i]):
            chiffreRef += 1
            compteur += 1
        elif(chiffreRef == listeDansOrdre[i]):
            pass
        else:
            compteur = 0
    if(compteur == 5):
        estGrandeSuite = True
    return estGrandeSuite

# print grandeSuite(liste5Des())

##Faire une méthode change(liste, position) qui permet de relancer le dé situé en
##"position" dans la liste.

def change(liste,position):
    if (position >= 1 and position <= 5):
        nouvelleListe = liste
        nouvelleListe[position - 1] = tirerD6()
        return nouvelleListe

# print change(liste5Des(), 2)

##Faire une méthode changeCertains(liste, listeDePositions) qui permet de relancer les
##dés situé aux positions indiquées par listeDePositions.

def changerCertaine(liste, listeDePositions):
    if(len(listeDePositions) >=1 and len(listeDePositions) <=5):
        nouvelleListe = liste
        for i in (listeDePositions):
            nouvelleListe = change(liste, i)
        return nouvelleListe

# liste = [1,4,5]
# print changerCertaine(liste5Des(), liste)

##Faire une méthode nouveauLance(liste) qui présente à un utilisateur une liste de dé et lui
##demande lesquels il souhaite relancer et retourne cette nouvelle liste.

def nouveauLance(liste):
    listeDe5Des = liste
    combien = 0
    while(combien <1 or combien >5):
        combien = input("Combien de des voulez vous changer [1 ou 5] ? ")
    listeDePositions = []
    for i in range (combien):
        lequel = input("A quelle position est le des que vous voulez relancer ? ")
        while(lequel in listeDePositions):
            lequel = input("Position deje occupe : quel des voulez vous relancer ? ")
        listeDePositions.append(lequel)

    listeDe5Des = changerCertaine(listeDe5Des, listeDePositions)
    print listeDe5Des 
    return listeDe5Des

# print nouveauLance(liste5Des())

##Faire une méthode jouer(nbFois) qui appelle "nbFois" la méthode nouveauLance(liste)

def jouer(nbFois):
    if(nbFois >=1):
        liste = liste5Des()
        for i in range(nbFois):
            liste = nouveauLance(liste)

# jouer(2)

##Faire une méthode qui permet de faire un jet de dés, de le relancer
##partiellement trois fois et qui retourne les combinaisons obtenues sur ce lancer

def relancer3fois():
    liste = liste5Des()
    compteur = 0
    lancerEncore = True
    OuiOuNon = ""
    print " Vous ne pouvez relancer que 3 fois"
    while(compteur < 3):
        OuiOuNon = raw_input("Voulez vous quitter [N/Q pour quitter]" )
        if(OuiOuNon.lower() == "n" or OuiOuNon.lower() == "q"):
            lancerEncore = False
        if(lancerEncore):   
            liste = nouveauLance(liste)
            compteur +=1
            print "Vous avez relancer " + str(compteur) + " fois"
    return liste

# print relancer3fois()

dictionnaire = {
    "1" : 100,
    "5" : 50,
    "BrelanDe1" : 1000,
    "BrelanAutre" : 100,
    "PetiteSuite" : 1250,
    "GrandeSuite" : 1500,
    "5Valeur5" : 5000
}

##Faire une méthode qui joue au Yams en solitaire. 
def Yams():
    score = 0
    liste = []
    while (score < 5000):
        liste = relancer3fois()
        if(full(liste)):
            pass
        if(brelan(liste)[0]):
            if(brelan(liste)[1] == 1):
                score += 1000
            else:
                score += 100

# La feuille de points peut
##être représentée par un dictionnaire Python qui associe une mission à une
##valeur qui par défaut vaut -1. 
# 
# Faire une méthode pour jouer au Yamsà plusieurs
##joueurs.

##Une version simplifiée du jeu du 5000 se joue avec 5 dés qu'on jette au
##maximum trois fois par tour pour être le premier à obtenir 5000points.
##A chaque tour, on peut relancer tout ou partie de ses dés. On compte les
##points obtenus au dernier jet selon les règles suivantes :
##chaque 1 = 100 points,  chaque 5 = 50 points,
##brelan de 1 = 1000 points, autre brelan = valeur du dé x 100
##Grande suite = 1500 points
##5 dés de valeur 5 = 5000 points, victoire immédiate.
##Ainsi, une fin de tour avec 4 4 4 1 1 fait 400 + 100 + 100 = 600 points.
##Coder le jeu du 5000 en solitaire en indiquant le nombre de tours effectués
##Coder le jeu à plusieurs joueurs.