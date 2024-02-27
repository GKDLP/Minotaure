import re
Labyrinthe = [["+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "_", "_", "_", "+"],
              ["+", "_", "_", "_", "+", "_", "_", "_", "_", "_", "_", "+", "_", "_", "_", "+", "_", "+", "_", "+"],
              ["+", "+", "+", "+", "+", "_", "+", "+", "+", "+", "_", "+", "+", "+", "_", "+", "M", "+", "_", "+"],
              ["T", "_", "_", "_", "+", "_", "+", "+", "+", "_", "_", "+", "_", "+", "_", "+", "+", "+", "_", "+"],
              ["+", "_", "+", "_", "_", "_", "+", "+", "_", "_", "+", "+", "_", "+", "_", "_", "_", "_", "_", "+"],
              ["+", "_", "+", "_", "+", "_", "+", "_", "_", "+", "_", "_", "_", "+", "_", "+", "+", "+", "+", "+"],
              ["+", "_", "_", "_", "+", "_", "+", "_", "+", "+", "_", "+", "+", "+", "_", "+", "+", "+", "+", "+"],
              ["+", "_", "+", "_", "_", "_", "+", "_", "+", "_", "_", "_", "_", "_", "_", "+", "+", "+", "+", "+"],
              ["+", "_", "+", "+", "+", "_", "+", "_", "+", "_", "+", "_", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "_", "+", "+", "+", "_", "_", "_", "+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "_", "+", "+", "_", "_", "+", "+", "+", "+", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "_", "_", "+", "+", "_", "+", "+", "+", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
              ["+", "+", "_", "_", "+", "+", "_", "_", "_", "_", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+"],
              ["+", "+", "+", "_", "+", "+", "_", "+", "_", "+", "_", "_", "_", "+", "+", "_", "+", "_", "+", "+"],
              ["+", "_", "_", "_", "_", "_", "_", "+", "_", "+", "_", "+", "+", "+", "+", "_", "+", "_", "_", ":"],
              ["+", "_", "+", "+", "_", "+", "+", "+", "_", "+", "+", "+", "_", "_", "_", "_", "+", "_", "+", "+"],
              ["+", "+", "+", "_", "_", "+", "+", "+", "_", "_", "_", "_", "_", "+", "+", "+", "+", "_", "+", "+"],
              ["+", "_", "_", "_", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "_", "_", "_", "+", "+"],
              ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+"]]

def Afficher():
    n = 0
    print("---------------------------------")
    for i in range(20):
        print(" ".join(Labyrinthe[n]))
        n = n + 1
    print("---------------------------------")
    return

LigneT = 4
ColoneT = 0

def AfficherFogue():
    global ColoneT, LigneT
    x = 3
    z = 3 
    border = Labyrinthe[LigneT - x][ColoneT - z]
    for I in range(6):
        for i in range(6):
            print(" ".join(Labyrinthe[LigneT - x][ColoneT - z]))
            z = z + 1
    print(" ".join(Labyrinthe[LigneT - x][ColoneT - z]))
    x = x + 1 
    return

AfficherFogue()

def AvancerD(Labyrinthe): # Avancer à droite de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT + 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        ColoneT = ColoneT + 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    Afficher()
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
    Afficher()
    return ColoneT,

def AvancerH(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT - 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "_", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        LigneT = LigneT - 1
        Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    Afficher()
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
    Afficher()
    return LigneT,

Minotaure = False 

def VerifierM():
    global Minotaure
    if Labyrinthe[LigneT][ColoneT] == "M":
        Minotaure = True
        Labyrinthe[LigneT][ColoneT] = re.sub("M", "%", Labyrinthe[LigneT][ColoneT])

def VerifierS():
    global Minotaure
    if Minotaure == True:
        print("Vous avez Vaincu le Minotaure")
        print("Vous avez Gagner ! Bravo !")
        return Minotaure
    else: 
        print("Vous n'avez pas Vaincu le Minotaure, La sortie n'est pas ouvert.")
        
while True:   #Le joueur entre la direction de son choix
    direction = input("Entrez la direction du joueur(Z,D,Q,S):")
    if direction == "Z":
        AvancerH(Labyrinthe)
        VerifierM()
    elif direction == "D":
        AvancerD(Labyrinthe)
        VerifierM()
    elif direction == "Q":
        AvancerG(Labyrinthe)
        VerifierM()
    elif direction == "S":
        AvancerB(Labyrinthe)
        VerifierM()
    else:
        print("Veuillez entrez une des directions(Z,D,Q,S):")
    if Labyrinthe[LigneT][ColoneT] == ":":
        VerifierS()
        break