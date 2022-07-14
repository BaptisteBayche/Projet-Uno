def get_jeton():
    '''
    Spécification
    permet de récupérer le nombre de jetons
    précondition:
        - aucune

    post conditions:
        - renvois un integer des données du fichier jetons.txt qui contient le bombre de jetons

    '''

    with open("jetons.txt","r") as fichier:
        nb_jeton = fichier.read()
        fichier.close()
        return int(nb_jeton)

def set_jeton(nouveau_jetons,nb_jeton = get_jeton()):
    '''
    Spécification
    Permet de changer le nombre de jetons
    permet de récupérer le nombre de jetons
    précondition:
        - nouveau_jetons (int négatif ou positif)  : nombre de jetons à enlever ou ajouter
        - nb_jetons (int positif) : nombre de jetons du joueur

    post conditions:
        - change les données du fichier jetons.txt (somme de 'nouveau_jetons' et de 'nb_jeton'

    '''
    with open("jetons.txt", "w") as fichier:

        jetons = nouveau_jetons + nb_jeton
        fichier.write(str(jetons))
        fichier.close()



