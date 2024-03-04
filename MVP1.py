import re
import sys
import random
Labyrinthe = [["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "_", "_", "+", "_", "_", "_", "_", "_", "_", "+", "_", "_", "_", "+", "_", "+", "_", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "_", "+", "+", "+", "+", "_", "+", "+", "+", "_", "_", "_", "+", "_", "+", "+", "+"],
              ["+", "+", "+", "T", "_", "_", "_", "+", "_", "+", "+", "+", "_", "_", "+", "_", "+", "_", "+", "+", "+", "_", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "_", "_", "_", "+", "+", "_", "_", "+", "+", "_", "+", "_", "_", "_", "_", "_", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "_", "+", "_", "+", "_", "_", "+", "_", "_", "_", "+", "_", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "_", "_", "+", "_", "+", "_", "+", "+", "_", "+", "+", "+", "_", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "_", "_", "_", "+", "_", "+", "_", "_", "_", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "+", "+", "_", "+", "_", "+", "_", "+", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "+", "+", "_", "_", "_", "+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "+", "_", "_", "+", "+", "+", "+", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "_", "+", "+", "_", "+", "+", "+", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "_", "_", "+", "+", "_", "_", "_", "_", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "_", "+", "+", "_", "+", "_", "+", "_", "_", "_", "+", "+", "_", "+", "_", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "_", "_", "_", "_", "_", "+", "_", "+", "_", "+", "+", "+", "+", "_", "+", "_", ":", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "+", "+", "_", "+", "+", "+", "_", "+", "+", "+", "_", "_", "_", "_", "+", "_", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "_", "_", "+", "+", "+", "_", "_", "_", "_", "_", "+", "+", "+", "+", "_", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"]
              ]

def Afficher():
    print("---------------------------------")
    for ligne in Labyrinthe:
        print(ligne)
    print("---------------------------------")
    return

#Afficher()

LigneT = 6
ColoneT = 3       
LigneM = 6
ColoneM = 19
def get_cases_non_visitée(a,b):# Definition d'une methode pour faire bouger le minotaure aléatoirement
    cases = []
    if a > 0:
        cases.append((a -1,b))
    if a < 25:
        cases.append((a + 1, b))
    if b > 0:
        cases.append((a,b -1))
    if b < 25:
        cases.append((a, b +1))
    cases_non_visitée = []
    for case in cases:
        if Labyrinthe[case[1]][case[0]] != "+":
            cases_non_visitée.append(case)
    return cases_non_visitée

def AfficherFogue():         # C'est la fonction afficher juste 3 case autour du J
    x = -3
    z = -3 
    while x != 4:
        while z != 4:
             sys.stdout.write(" ".join(Labyrinthe[LigneT + x][ColoneT + z]))
             z = z + 1
        z = -3    
        print(" ".join(Labyrinthe[LigneT + x][ColoneT + z]))
        x = x + 1
    return

#AfficherFogue()

def AvancerD(Labyrinthe): # Avancer à droite de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT + 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        ColoneT = ColoneT + 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    #AfficherFogue()
    return ColoneT,

def AvancerG(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT - 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else:
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT]) 
        #Labyrinthe[LigneT][ColoneT] ==  "_" or "M" or ":" 
        ColoneT = ColoneT - 1 
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    #AfficherFogue()
    return ColoneT,

def AvancerH(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT - 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        LigneT = LigneT - 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    #AfficherFogue()
    return LigneT,

def AvancerB(Labyrinthe): # Avancer en bas de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT + 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        LigneT = LigneT + 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    #AfficherFogue()
    return LigneT,

minotaure_capture = False

def VerifierM():
    global minotaure_capture
    if (ColoneT,LigneT)==(ColoneM,LigneM):
        minotaure_capture = True
        return True


def VerifierS():
    global minotaure_capture
    if minotaure_capture == True:
        print("Vous avez Vaincu le Minotaure")
        print("Vous avez Gagner ! Bravo !")
        return minotaure_capture
    else: 
        print("Vous n'avez pas Vaincu le Minotaure, La sortie n'est pas ouvert.")


def afficher_labyrinthe():
    labyrinthe_affiche = ""
    for b, ligne in enumerate(Labyrinthe):
        for a, car in enumerate(ligne):
            if (a, b) == (ColoneT, LigneT):
                labyrinthe_affiche += "T"
            elif (a, b) == (ColoneM, LigneM) and not minotaure_capture:
                labyrinthe_affiche += "M"
            elif (a, b) == (ColoneM, LigneM) and minotaure_capture:
                labyrinthe_affiche += "%"
            else:
                labyrinthe_affiche += car
        labyrinthe_affiche += "\n"
    return labyrinthe_affiche

while True:
    print(afficher_labyrinthe())
    if VerifierM():
        print("Félicitations !Vous avez capturez le minotaure! .")
        #Le joueur entre la direction de son choix
    direction = input("Entrez la direction du joueur(Z,D,Q,S):")
    if direction == "Z":
        AvancerH(Labyrinthe)
        #VerifierM()
    elif direction == "D":
        AvancerD(Labyrinthe)
        #VerifierM()
    elif direction == "Q":
        AvancerG(Labyrinthe)
        #VerifierM()
    elif direction == "S":
        AvancerB(Labyrinthe)
        #VerifierM()
    else:
        print("Veuillez entrez une des directions(Z,D,Q,S):")

    # Mise à jour des coordonnées du minotaure
    if  minotaure_capture == False:
        cases_non_visitée = get_cases_non_visitée(ColoneM,LigneM)
        cases_non_visitée_sans_murs =[(a,b) for a,b in cases_non_visitée if Labyrinthe[b][a] != "+"]
        if cases_non_visitée_sans_murs :
            ColoneM , LigneM = random.choice(cases_non_visitée_sans_murs)

    # Le joueur rencontre la sortie
    if Labyrinthe[LigneT][ColoneT] == ":":
        VerifierS()
        break