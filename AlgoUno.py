import random

carte_special,carte_normal = [], []
nb_carte_pose = 0
changement = True
def genDeckUno():
    '''
    Spécification
    Genere aléatoirement les cartes du uno
    précondition:
        - aucune

    post conditions:
        - deck (list) : liste des cartes mélanger aléatoirement
        - carte_special (lis) : liste des cartes spécial (+4,+2, changement de couleur)

    '''
    global carte_special,carte_normal
    carte_normal = []       #Va contenir les cartes normal (numero + couleur)
    carte_special = []      # contient les cartes spécial (+4,+2,joker,inversement de sens,passe ton tour)
    for couleur in range(4):
        for nombre in range(2):
            for numero in range(1,10):
                if couleur == 0:
                    carte_normal.append("carte_"+str(numero)+"_vert")
                elif couleur == 1:
                    carte_normal.append("carte_"+str(numero)+"_jaune")
                elif couleur == 2:
                    carte_normal.append("carte_"+str(numero)+"_bleu")
                else:
                    carte_normal.append("carte_"+str(numero)+"_rouge")
            if couleur == 0:
                carte_special.append("carte_p2_vert"),carte_special.append("carte_in_vert")
            elif couleur == 1:
                carte_special.append("carte_p2_jaune"),carte_special.append("carte_in_jaune")
            elif couleur == 2:
                carte_special.append("carte_p2_bleu"),carte_special.append("carte_in_bleu")
            else:
                carte_special.append("carte_p2_rouge"),carte_special.append("carte_in_rouge")
        carte_special.append("carte_chcouleur"),carte_special.append("carte_p4")
    carte_normal.append("carte_0_vert"),carte_normal.append("carte_0_jaune"),carte_normal.append("carte_0_bleu"),carte_normal.append("carte_0_rouge")
    deck = carte_normal + carte_special
    random.shuffle(deck)
    return deck,carte_special



def distribution(nbJoueurs) :
    '''
    Spécification
    Distribue les cartes aux joueurs
    précondition:
        - nbJoueurs (int) : Choix du nombres de joueurs (ordinateurs)

    post conditions:
        - deckJoueurs (dict) : dictionnaire des cartes de chaques joueurs
        - pioche (list) : renvoie toutes les cartes restantes
        - premiere_carte (str) : renvoie la premiere carte qui va etre jouer

    '''
    deck,carte_special = genDeckUno()

    deckJoueurs = {}
    for joueur in range(nbJoueurs) :
        deckJoueurs["joueur" + str(joueur+1)] = []
    for nbCartes in range(7):       #nombre de carte à distribuer par joueur
        for joueur in range(nbJoueurs):     #nombre de joueur
            deckJoueurs["joueur" + str(joueur+1)].append(deck.pop())
    premiere_carte = deck[0]
    index = 0
    while deck[index] in carte_special: #on verifie que la premiere carte ne soit pas un joker
        index  += 1
    premiere_carte = deck.pop(index)
    pioche = deck       #reste des cartes du deck
    return deckJoueurs,pioche,premiere_carte


def ajouter_carte(nb_cartes,deck_joueur,pioche):
    '''
    Spécification
    Permet d'ajouter des cartes au deck du joueur
    précondition:
        - nb_cartes (int) : nombre de cartes que l'on va ajouter au joueur
        - deck_joueur (list) : deck du joueur  à qui ont doit ajouter les cartes
        - pioche (list) : la pioche du jeu

    post conditions:
        - deck_joueur > renvois le deck du joueur avec les cartes en plus
        - pioche > renvoie la pioche avec les cartes en moins

    '''
    if len(pioche) <= 4:
        pioche = genDeckUno()[0]
    for i in range(nb_cartes):
        deck_joueur.append(pioche.pop())
    return deck_joueur,pioche

def verification_carte(carte,carte_jeu,nb_carte_pose):
    '''
    Spécification
    Permet de vérifier si un joueur peux ou non poser une carte
    précondition:
        - carte (str) : carte à verifier
        - carte_jeu (str) : carte qui est sur le plateau (la derniere joue)
        - nb_carte_pose (int) : nombre de fois que le joueur à posé des cartes pendant son tour

    post conditions:
        - True > peux posé la carte
        - False > ne peux pas posé la carte
        - +4 > peux poser et doit exectuer le code pour un +4
        - +2 > peux poser et doit exectuer le code pour un +2


    '''
    global carte_special,carte_normal
    if carte in carte_normal:
        if nb_carte_pose == 0:
            if carte[6] == carte_jeu[6] or carte[8:] == carte_jeu[8:] :

                return True
            elif carte_jeu[6:8] == "sc" and carte[8:] == carte_jeu[9:]:
                return True
            elif carte_jeu[6:8] == "p2" or carte_jeu[6:8] == "in":
                if carte[8:] == carte_jeu[9:]:
                    return True

            else:
                return False
        else:
            if carte[6] == carte_jeu[6]:
                return True
            elif carte_jeu[6:8] == "sc" and carte[8:] == carte_jeu[9:]:
                return True
            else:
                return False
    elif carte in carte_special:
        if nb_carte_pose == 0:
            if carte == "carte_p4":
                test_fdt()
                return "+4"
            elif carte== "carte_chcouleur":
                test_fdt()
                return "changement_couleur"
            elif carte[6:8] == "p2":
                if carte[9:] == carte_jeu[8:] or carte[9:] == carte_jeu[9:] or carte[6:8] == carte_jeu[6:8] :

                    return "+2"
            elif carte[6:8] == "in":
                if carte[9:] == carte_jeu[8:] or carte[9:] == carte_jeu[9:] or carte[6:8] == carte_jeu[6:8] :

                    sens(True)
                    return True
            elif carte[6:13] == "pasTour":
                return False

        else:
            if carte[6:8]=="p2" and carte_jeu[6:8] == "p2":
                return "+2"
            elif carte[6:8]=="in" and carte_jeu[6:8] == "in":
                sens(True)
                return True



def test_fdt():
    return False


def sens(changer):
    '''
    Spécification
    Permet de récuperer ou changer le sens
    précondition:
        - changer (Bool)
            True > change le sens
            False > renvoie juste le sens

    post conditions:
        - inverse (str) > le sens est celui à l'inverse des aiguilles d'une montre
        - normal (str) > le sens est celui des aiguilles d'une montre

    '''

    global changement
    if changer:
        if changement == True:
            changement = False
            return "inverse"
        else:
            changement = True
            return "normal"
    else:
        if changement == True:
            return "normal"
        else:
            return "inverse"




def couleur_aleatoire():
    '''
    Spécification
    Genere une couleur aléatoire entre (bleu,rouge,jaune,vert)
    précondition:
        - aucune

    post conditions:
        - derniere_carte_pose (str) : renvoie la derniere carte qui va etre pose sur le jeu suivant la couleur choisis aléatoirement

    '''
    couleur = random.choice(["bleu","rouge","vert","jaune"])
    if couleur == "bleu":
        derniere_carte_pose = "carte_sc_bleu"
    elif couleur == "rouge":
        derniere_carte_pose = "carte_sc_rouge"
    elif couleur == "vert":
        derniere_carte_pose = "carte_sc_vert"
    elif couleur == "jaune":
        derniere_carte_pose = "carte_sc_jaune"
    return derniere_carte_pose





def IA_ORDI(deck_ordi,carte_jeu,nb_carte_pose):
    '''
    Spécification
    Permet de savoir si l'ordinateur peux ou pas poser la carte
    précondition:
        - deck_ordi (liste) > deck de l'ordinateur
        - carte_jeu (str) > derniere carte jouer (qui est sur le plateau)
        - nb_carte_pose > nombre de carte pose pendant le tour de l'ordinateur

    post conditions:
        - carte_a_place > renvoie la carte que l'ordinateur peut poser si egal à "" ne peux pas poser
        - deck_ordi > renvoie le deck de l'ordinateur
        - type_carte > renvoie le type de carte (+4,+2,inversement etc..)

    '''

    carte_a_place = ""
    i = 0
    for i in range(len(deck_ordi)):
        carte = deck_ordi[i]
        check_carte = verification_carte(carte,carte_jeu,nb_carte_pose)
        i +=1
        if check_carte:
            carte_a_place = carte

            if carte == "carte_p4":
                type_carte = "+4"
            elif carte =="carte_chcouleur":
                type_carte = "changement_couleur"
            elif carte[6:8]=="p2":
                type_carte = "+2"
            elif carte[6:8]=="in":
                type_carte = "in"
            else:
                type_carte = None
            del deck_ordi[i-1]


            return carte_a_place,deck_ordi,type_carte
    return "", deck_ordi,None



