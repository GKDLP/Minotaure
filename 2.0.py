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

def Afficher():    # Afficher le labyrinthe
    n = 0
    print("---------------------------------")
    for i in range(20):
        print(" ".join(Labyrinthe[n]))
        n = n + 1
    print("---------------------------------")
    return

Afficher()
LigneT = 4
ColoneT = 0

def FilsAD():       # Fils d'Arianne Droit
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT] == "~":
        print("Vous revenez sur vos pas")
        Labyrinthe[LigneT][ColoneT] = re.sub("~", "T", Labyrinthe[LigneT][ColoneT]) # Diego c'est une poukave
        if Labyrinthe[LigneT][ColoneT + 1] == "~":
            Labyrinthe[LigneT][ColoneT + 1] = re.sub("~", "_", Labyrinthe[LigneT][ColoneT]) # C'est ici que sa marche pas 
    return LigneT, ColoneT

def FilsAG():       # Fils d'Arianne Gauche
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT] == "~":
        print("Vous revenez sur vos pas")
        Labyrinthe[LigneT][ColoneT] = re.sub("~", "T", Labyrinthe[LigneT][ColoneT]) # Diego c'est une poukave
        if Labyrinthe[LigneT][ColoneT - 1] == "~":
            Labyrinthe[LigneT][ColoneT - 1] = re.sub("~", "_", Labyrinthe[LigneT][ColoneT])
    return LigneT, ColoneT

def FilsAH():       # Fils d'Arianne Haut
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT] == "~":
        print("Vous revenez sur vos pas")
        Labyrinthe[LigneT][ColoneT] = re.sub("~", "T", Labyrinthe[LigneT][ColoneT]) # Diego c'est une poukave
        if Labyrinthe[LigneT - 1][ColoneT] == "~":
            Labyrinthe[LigneT - 1][ColoneT] = re.sub("~", "_", Labyrinthe[LigneT][ColoneT])
    return LigneT, ColoneT

def FilsAB():       # Fils d'Arianne Bas
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT] == "~":
        print("Vous revenez sur vos pas")
        Labyrinthe[LigneT][ColoneT] = re.sub("~", "T", Labyrinthe[LigneT][ColoneT]) # Diego c'est une poukave
        if Labyrinthe[LigneT + 1][ColoneT] == "~":
            Labyrinthe[LigneT + 1][ColoneT] = re.sub("~", "_", Labyrinthe[LigneT][ColoneT])
    return LigneT, ColoneT

def AvancerD(Labyrinthe): # Avancer à droite de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT + 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "~", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        ColoneT = ColoneT + 1
        FilsAD()
        if Labyrinthe[LigneT][ColoneT] == "_":
            Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    Afficher()
    return ColoneT,

def AvancerG(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT][ColoneT - 1] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else:
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "~", Labyrinthe[LigneT][ColoneT]) 
        #Labyrinthe[LigneT][ColoneT] ==  "_" or "M" or ":" 
        ColoneT = ColoneT - 1 
        FilsAG()
        if Labyrinthe[LigneT][ColoneT] == "_":
            Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    Afficher()
    return ColoneT,

def AvancerH(Labyrinthe): # Avancer à gauche de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT - 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "~", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        LigneT = LigneT - 1
        FilsAH()
        if Labyrinthe[LigneT][ColoneT] == "_":
            Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    Afficher()
    return LigneT,

def AvancerB(Labyrinthe): # Avancer en bas de 1
    global ColoneT, LigneT
    if Labyrinthe[LigneT + 1][ColoneT] == '+': # blocage si il y a un mur 
        print("vous ne pouvez pas avancer, les murs du labyrinthe sont bien trop grand")
    else: 
        Labyrinthe[LigneT][ColoneT] = re.sub("T", "~", Labyrinthe[LigneT][ColoneT])
        #Labyrinthe[LigneT][ColoneT] ==  "" or "M" or ":"
        LigneT = LigneT + 1
        FilsAB()
        if Labyrinthe[LigneT][ColoneT] == "_":
            Labyrinthe[LigneT][ColoneT] = re.sub("_", "T", Labyrinthe[LigneT][ColoneT])
    Afficher()
    return LigneT,

Minotaure = False 

def VerifierM():    #Vérification du Minotaure
    global Minotaure
    if Labyrinthe[LigneT][ColoneT] == "M":
        Minotaure = True
        Labyrinthe[LigneT][ColoneT] = re.sub("M", "%", Labyrinthe[LigneT][ColoneT])

def VerifierS():    #Vérification Sortie
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

