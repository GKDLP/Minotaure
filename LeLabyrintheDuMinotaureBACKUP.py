import re
import sys
Labyrinthe = [["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "_", "_", "_", "_", "_", "+", "+", "+"],
              ["+", "+", "+", "+", "_", "_", "_", "+", "_", "_", "_", "_", "_", "_", "+", "_", "_", "_", "+", "_", "+", "_", "+", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "_", "+", "+", "+", "+", "_", "+", "+", "+", "_", "+", "M", "+", "_", "+", "+", "+"],
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
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"]]

def Afficher():
    n = 0
    print("---------------------------------")
    for i in range(24):
        print(" ".join(Labyrinthe[n]))
        n = n + 1
    print("---------------------------------")
    return

#Afficher()

LigneT = 6
ColoneT = 3       

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

AfficherFogue()

def AvancerD(Labyrinthe): # Avancer à droite de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT + 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        ColoneT = ColoneT + 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    AfficherFogue()
    return ColoneT,

def AvancerG(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT - 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else:
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT]) 
        ColoneT = ColoneT - 1 
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    AfficherFogue()
    return ColoneT,

def AvancerH(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT - 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        LigneT = LigneT - 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    AfficherFogue()
    return LigneT,

def AvancerB(Labyrinthe): # Avancer en bas de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT + 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        LigneT = LigneT + 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    AfficherFogue()
    return LigneT,

Minotaure = False 
Score = 100

def VerifierM(): # Cette fonction vérifie le Minotaure
    global Minotaure, Score
    if Labyrinthe[LigneT][ColoneT] == "M":
        Minotaure = True
        Labyrinthe[LigneT][ColoneT] = re.sub("M", "%", Labyrinthe[LigneT][ColoneT])
        Score = Score + 50
        print(Score)
        print("Vous avez battue le Minotaure vous gagnez 50 point supplémentaire")
    return Score

def VerifierS():  # Cette fonction vérifie la sortie 
    global Minotaure
    if Minotaure == True:
        print("Vous avez Vaincu le Minotaure")
        print("Vous avez Gagner ! Bravo !")
        return Minotaure
    else: 
        print("Vous n'avez pas Vaincu le Minotaure, La sortie n'est pas ouvert.")
        
print("------------------------------------------------------------------")
print("")
print("Bienvenu dans le labyrinthe de Dédale")
print("")
print("Dans se jeu vous incarnerai Thésée, votre but est de vaincre 'Minos' le minotaure du labyrinthe puis de vous echapper du Labyrinthe")
print("")
game = input("Voulez-vous entrer dans le Labyrinthe ?   Y/N ")
print("------------------------------------------------------------------")
while game != "Y":
    print("Zoulette reviens quand tu sera prêt")
    game = input("Voulez-vous entrer dans le Labyrinthe ?   Y/N ")
else:
    AfficherFogue()
    while True:   #Le joueur entre la direction de son choix
        direction = input("Entrez la direction du joueur(Z,D,Q,S):")
        if direction == "Z":
            AvancerH(Labyrinthe)
            Score = Score - 1
            VerifierM()
        elif direction == "D":
            AvancerD(Labyrinthe)
            Score = Score - 1
            VerifierM()
        elif direction == "Q":
            AvancerG(Labyrinthe)
            Score = Score - 1
            VerifierM()
        elif direction == "S":
            AvancerB(Labyrinthe)
            Score = Score - 1
            VerifierM()
        else:
            print("Veuillez entrez une des directions(Z,D,Q,S):")
        if Score == 50:
            print(Score)
        if Score == 0:
            print("-------------------------------------------")
            print("Vous avez passer trop de temps dans le Labyrinthe, vous etes épuisé, vous sentez vos forces vous abandonnez ... BOO t nul ")
            print("-------------------------------------------")
            break
        if Labyrinthe[LigneT][ColoneT] == ":":
            VerifierS()
            break
