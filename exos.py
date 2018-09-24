# -*- coding: cp1252 -*-
import random
## random.randint(1,1000)

##Ecrire une méthode tirer(mini, maxi) qui tire un nombre au hasard
##entre mini et maxi

def tirer(min, max):
    if min >=1 and max >=1:
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
    print message

##Plus ou moins ?
##Faire une méthode qui tire un nombre cible au hasard sur
##un intervalle donné puis demande à un joueur un nombre pour lui indiquer si
##la cible est plus petite ou plus grande que sa proposition.

def plusOuMoins():
    nombreCible = tirerD6()
    nombreJoueur = lireChiffreClavier()
    comparer(nombreJoueur, nombreCible)

## plusOuMoins()


##Faire un programme qui boucle jusqu'à ce que la cible ait été trouvée

def plusOuMoinsUntilVictory():
    nombreCible = tirerD6()
    nombreJoueur = lireChiffreClavier()
    while(nombreJoueur != nombreCible):
        comparer(nombreJoueur, nombreCible)
        nombreJoueur = lireChiffreClavier()
    comparer(nombreJoueur, nombreCible)

## plusOuMoinsUntilVictory()

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


def rechercheDichotomie(min, max):
    nombreADeviner = tirer(min,max)
    rechercheNombreMin = min
    rechercheNombreMax = max
    rechercheNombre = tirer(rechercheNombreMin,rechercheNombreMax)

    compteur = 1
    while(nombreADeviner != rechercheNombre):
        if(estPlusGrand(nombreADeviner, rechercheNombre)):
            rechercheNombreMin = rechercheNombre
            compteur += 1
        else:
            rechercheNombreMax = rechercheNombre
            compteur += 1
        rechercheNombre = tirer(rechercheNombreMin,rechercheNombreMax)
    else:
        print "Trouve apres " + str(compteur) + " fois."
        return compteur #ajout pour la suite

# rechercheDichotomie(1,100)

##Bonus, regarder combien de coups, en moyenne, le programme utilise pour
##trouver la réponse. Tester sur 100000 parties.

def moyenneCompteurVictoire():
    countCompteurs = 0
    for i in range (100000) :
        countCompteurs += rechercheDichotomie(1,100)
    moyenne = countCompteurs / 100000
    print "En moyenne pour min 1 et max 100, l'ordinateur trouve en " + str(moyenne) + " coups"

# moyenneCompteurVictoire()

##Faire une méthode qui affiche un chiffre sous la forme d'un dé sur trois lignes.
##      *     *     * *   * *   * *
## *           *           *    * *
##        *     *   * *   * *   * *

##Yams / Yathzee
##Faire une méthode qui génère une liste de 5 chiffres correspondant à un jet
##de 5 dés
##Faire une méthode estYams(liste) qui indique si une liste de 5 chiffres
##contient 5 fois le même chiffre
##Faire une méthode compter(liste, valeur) qui compte le nombre d'apparition de
##"valeur" dans la liste de dés
##Faire une méthode sommeValeurs(liste, valeur) qui retourne la somme des
##dés de la liste de "valeur"
##Faire une méthode qui indique si la liste contient au moins un brelan (3)
##Faire une méthode qui indique si la liste contient au moins un carré (4)
##Faire une méthode qui indique si la liste contient au moins un full (3 et 2)
##Faire une méthode qui indique si la liste contient une petite suite (4 valeurs)
##Faire une méthode qui indique si la liste contient une grande suite (5 valeurs)
##Faire une méthode change(liste, position) qui permet de relancer le dé situé en
##"position" dans la liste.
##Faire une méthode changeCertains(liste, listeDePositions) qui permet de relancer les
##dés situé aux positions indiquées par listeDePositions.
##Faire une méthode nouveauLance(liste) qui présente à un utilisateur une liste de dé et lui
##demande lesquels il souhaite relancer et retourne cette nouvelle liste.
##Faire une méthode jouer(nbFois) qui appelle "nbFois" la méthode nouveauLance(liste)
##Faire une méthode qui permet de faire un jet de dés, de le relancer
##partiellement trois fois et qui retourne les combinaisons obtenues sur ce lancer

##Faire une méthode qui joue au Yams en solitaire. La feuille de points peut
##être représentée par un dictionnaire Python qui associe une mission à une
##valeur qui par défaut vaut -1. Faire une méthode pour jouer au Yamsà plusieurs
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