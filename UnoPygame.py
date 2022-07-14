import sys

import AlgoUno
import pygame
pygame.init()
from pygame.locals import *
import ressourcePygame as rp
import time
import AlgoJetons
import ressourcePygame

def clique_bouton():
    global affichage,deckJoueursUno,pioche,derniere_carte_pose,nb_joueur,running
    x, y = pygame.mouse.get_pos()
    over_retour_menuJeu = bouton_rect_retour_menuJeu.collidepoint(x,y)
    over_regle = bouton_rect_regle.collidepoint(x,y)
    over_retour_regle = bouton_rect_retour_regle.collidepoint(x,y)
    over_jouer = bouton_rect_jouer.collidepoint(x,y)
    over_2joueur = bouton_rect_2j.collidepoint(x,y)
    over_3joueur = bouton_rect_3j.collidepoint(x,y)
    over_4joueur = bouton_rect_4j.collidepoint(x,y)
    over_retour_fdp = bouton_rect_retour_fin_de_parti.collidepoint(x,y)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if affichage == menu_uno:
                if over_regle:
                    affichage = regle_uno
                elif over_jouer:
                    affichage = select_joueur_uno
                elif over_retour_menuJeu:
                    running = False
                    pygame.quit()
                    sys.exit()

            elif affichage == regle_uno:
                if over_retour_regle:
                        affichage = menu_uno
            elif affichage == select_joueur_uno:
                time.sleep(0.5)
                if over_2joueur:
                    nb_joueur = 2
                    affichage = jeu_uno
                    deckJoueursUno,pioche,derniere_carte_pose = AlgoUno.distribution(2)

                elif over_3joueur:
                    nb_joueur = 3
                    affichage = jeu_uno
                    deckJoueursUno,pioche,derniere_carte_pose = AlgoUno.distribution(3)

                elif over_4joueur:
                    nb_joueur = 4
                    affichage = jeu_uno
                    deckJoueursUno,pioche,derniere_carte_pose = AlgoUno.distribution(4)

            if affichage == menu_fin_de_partie:
                if over_retour_fdp:
                    running = False
                    pygame.quit()
                    sys.exit()




        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()



def menu_uno():
    screen.blit(rp.texte.titre_menu_uno,((580),50))
    screen.blit(bouton_jouer,(498,300))
    screen.blit(bouton_regle,(240,500))
    screen.blit(bouton_retour_menuJeu,(760,500))
    screen.blit(texte_nb_jetons,(1100,655))
    screen.blit(jeton,(1200,640))
    clique_bouton()

def regle_uno():
    screen.blit(rp.texte.titre_regle_uno,((largeur//2.8),50))
    screen.blit(txt_regle_uno,(125,150))
    screen.blit(bouton_retour_regle,(500,517))
    clique_bouton()

def select_joueur_uno():
    screen.blit(rp.texte.choix_nombre_ordi,(100,50))
    screen.blit(bouton_2j,(largeur//2.7,150))
    screen.blit(bouton_3j,(largeur//2.7,350))
    screen.blit(bouton_4j,(largeur//2.7,550))
    clique_bouton()

def jeu_uno():
    global pioche, coo_rect_carte,derniere_carte_pose,fin_de_tour,nb_carte_pose, prochain_joueur, joueur_actuel, affichage, running, resultat_fin_de_partie


    screen.blit(bouton_finTour_uno,(1100,430))

    if nb_joueur >= 2:
        screen.blit(icone_ordi1,(20,230))
        texte_nbCarte_ordi1 = rp.font_info.render(str(len(deckJoueursUno["joueur2"]))+" carte(s)",1,(0,0,0))
        screen.blit(texte_nbCarte_ordi1,((10),345))
    if nb_joueur >=3:
        screen.blit(icone_ordi2,(585,10))
        texte_nbCarte_ordi2 = rp.font_info.render(str(len(deckJoueursUno["joueur3"]))+" carte(s)",1,(0,0,0))
        screen.blit(texte_nbCarte_ordi2,((575),125))

    if nb_joueur >=4:
        screen.blit(icone_ordi3,(1160,230))
        texte_nbCarte_ordi3 = rp.font_info.render(str(len(deckJoueursUno["joueur4"]))+" carte(s)",1,(0,0,0))
        screen.blit(texte_nbCarte_ordi3,((1150),345))

    x, y = pygame.mouse.get_pos()
    over_pioche = carte_pioche_uno_rect.collidepoint(x,y)
    over_fin_de_tour = bouton_rect_finTour_uno.collidepoint(x,y)

    i=0
    carte_a_pose = []
    type_carte = ""
    liste_carte_fdt = ["+4","changement_couleur"]




    nb_rect = len(deckJoueursUno["joueur1"])
    placement_cartes_uno(deckJoueursUno["joueur1"],pioche,derniere_carte_pose)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:

            if over_fin_de_tour:
                if nb_carte_pose == 0:
                    AlgoUno.ajouter_carte(1, deckJoueursUno['joueur1'],pioche)
                    print("Tu pioche 1 cartes")
                fin_de_tour = AlgoUno.test_fdt()
                placement_cartes_uno(deckJoueursUno["joueur1"],pioche,derniere_carte_pose)
                joueur_actuel = "joueur1"
                prochain_joueur = ""
                nb_carte_pose = 0
                while prochain_joueur != "joueur1":
                    type_carte = ""
                    nb_carte_pose = 0
                    i = 0

                    if AlgoUno.sens(False) == "normal":
                        if nb_joueur == 2:
                            if joueur_actuel == "joueur1":
                                joueur_actuel = "joueur2"
                                prochain_joueur ="joueur1"
                        if nb_joueur == 3:
                            if joueur_actuel == "joueur1":
                                joueur_actuel ="joueur2"
                                prochain_joueur = "joueur3"
                            elif joueur_actuel == "joueur2":
                                joueur_actuel ="joueur3"
                                prochain_joueur = "joueur1"
                        if nb_joueur == 4:
                            if joueur_actuel == "joueur1":
                                joueur_actuel = "joueur2"
                                prochain_joueur = "joueur3"
                            elif joueur_actuel == "joueur2":
                                joueur_actuel = "joueur3"
                                prochain_joueur = "joueur4"
                            elif joueur_actuel == "joueur3":
                                joueur_actuel = "joueur4"
                                prochain_joueur = "joueur1"
                    if AlgoUno.sens(False) == "inverse":
                        if nb_joueur == 2:
                            if joueur_actuel == "joueur1":
                                joueur_actuel = "joueur2"
                                prochain_joueur = "joueur1"
                        if nb_joueur == 3:
                            if joueur_actuel == "joueur1":
                                joueur_actuel ="joueur3"
                                prochain_joueur ="joueur2"
                            elif joueur_actuel == "joueur3":
                                joueur_actuel = "joueur2"
                                prochain_joueur ="joueur1"
                        if nb_joueur == 4:
                            if joueur_actuel == "joueur1":
                                joueur_actuel = "joueur4"
                                prochain_joueur= "joueur3"
                            elif joueur_actuel == "joueur4":
                                joueur_actuel = "joueur3"
                                prochain_joueur = "joueur2"
                            elif joueur_actuel == "joueur3":
                                joueur_actuel = "joueur2"
                                prochain_joueur = "joueur1"

                    print("Au tour du " + joueur_actuel + "\n")

                    while i < len(deckJoueursUno[joueur_actuel]):
                        i += 1
                        if len(deckJoueursUno[joueur_actuel]) != 0:
                            if type_carte not in liste_carte_fdt:
                                liste_carte_ordi, deckJoueursUno[joueur_actuel],type_carte = AlgoUno.IA_ORDI(deckJoueursUno[joueur_actuel],derniere_carte_pose,nb_carte_pose)
                                if len(liste_carte_ordi) > 0:
                                    print(joueur_actuel + " pose : " + liste_carte_ordi)
                                    nb_carte_pose +=1
                                    derniere_carte_pose = liste_carte_ordi
                                    placement_cartes_uno(deckJoueursUno["joueur1"],pioche,derniere_carte_pose)
                                    if type_carte == "+4":
                                         AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                         derniere_carte_pose = AlgoUno.couleur_aleatoire()
                                         print(joueur_actuel +" choisis du " + derniere_carte_pose[9:].upper())
                                         print(prochain_joueur + " pioches 4 cartes !")
                                    if type_carte == "changement_couleur":
                                         derniere_carte_pose = AlgoUno.couleur_aleatoire()
                                         print(joueur_actuel +" choisis du " + derniere_carte_pose[9:].upper())
                                    if type_carte == "+2":
                                         AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)
                                         print(prochain_joueur + " pioche 2 cartes !")
                                    if type_carte == "in":
                                         AlgoUno.sens(True)
                                         print(joueur_actuel +" change de sens !")
                                    time.sleep(0.5)
                    if nb_carte_pose == 0:
                        AlgoUno.ajouter_carte(1,deckJoueursUno[joueur_actuel],pioche)
                        print(joueur_actuel +" pioche 1 carte")
                for i in range(nb_joueur):
                    if len(deckJoueursUno["joueur"+str(i+1)]) == 0:
                        print("joueur"+str(i+1)+" gagne la partie !")
                        resultat_fin_de_partie = False
                        affichage = menu_fin_de_partie

                print("A ton tour !")
                fin_de_tour = True
                nb_carte_pose = 0



            if AlgoUno.sens(False) == "normal":
                prochain_joueur = "joueur2"
            else:
                prochain_joueur = "joueur"+ str(nb_joueur-1)

            if fin_de_tour == True:
                if over_pioche:
                    if fin_de_tour != False:
                        deckJoueursUno["joueur1"],pioche = AlgoUno.ajouter_carte(1,deckJoueursUno["joueur1"],pioche)
                        nb_carte_pose +=1
                        print("Tu pioche une carte et ton tour se termine")
                        fin_de_tour = False
                if nb_rect >= 1:
                    if nb_rect > 7:
                        carte_rect_uno_1 = pygame.Rect(coo_rect_carte[0][0],642,coo_rect_carte[0][2],coo_rect_carte[0][3])
                    else:
                        carte_rect_uno_1 = pygame.Rect(coo_rect_carte[0])
                    over_carte_uno_1 = carte_rect_uno_1.collidepoint(x,y)
                    if over_carte_uno_1:
                        verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][0],derniere_carte_pose,nb_carte_pose)
                        if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][0]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][0]
                        if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)



                if nb_rect >= 2:
                     if nb_rect > 8:
                        carte_rect_uno_2 = pygame.Rect(coo_rect_carte[1][0],642,coo_rect_carte[1][2],coo_rect_carte[1][3])
                     else:
                        carte_rect_uno_2 = pygame.Rect(coo_rect_carte[1])
                     over_carte_uno_2 = carte_rect_uno_2.collidepoint(x,y)
                     if over_carte_uno_2:
                        verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][1],derniere_carte_pose,nb_carte_pose)
                        if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][1]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][1]
                        if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)


                if nb_rect >= 3:
                    if nb_rect > 9:
                        carte_rect_uno_3 = pygame.Rect(coo_rect_carte[2][0],642,coo_rect_carte[2][2],coo_rect_carte[2][3])
                    else:
                        carte_rect_uno_3 = pygame.Rect(coo_rect_carte[2])
                    over_carte_uno_3 = carte_rect_uno_3.collidepoint(x,y)
                    if over_carte_uno_3:
                        verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][2],derniere_carte_pose,nb_carte_pose)
                        if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][2]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][2]
                        if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 4:
                    if nb_rect > 10:
                        carte_rect_uno_4 = pygame.Rect(coo_rect_carte[3][0],642,coo_rect_carte[3][2],coo_rect_carte[3][3])
                    else:
                        carte_rect_uno_4 = pygame.Rect(coo_rect_carte[3])
                    over_carte_uno_4 = carte_rect_uno_4.collidepoint(x,y)
                    if over_carte_uno_4:
                        verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][3],derniere_carte_pose,nb_carte_pose)
                        if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][3]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][3]
                        if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 5:
                    if nb_rect > 11:
                        carte_rect_uno_5 = pygame.Rect(coo_rect_carte[4][0],642,coo_rect_carte[4][2],coo_rect_carte[4][3])
                    else:
                        carte_rect_uno_5 = pygame.Rect(coo_rect_carte[4])
                    over_carte_uno_5 = carte_rect_uno_5.collidepoint(x,y)
                    if over_carte_uno_5:
                       verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][4],derniere_carte_pose,nb_carte_pose)
                       if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][4]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][4]
                       if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                       if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                       if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 6:
                    if nb_rect > 12:
                        carte_rect_uno_6 = pygame.Rect(coo_rect_carte[5][0],642,coo_rect_carte[5][2],coo_rect_carte[5][3])
                    else:
                        carte_rect_uno_6 = pygame.Rect(coo_rect_carte[5])
                    over_carte_uno_6 = carte_rect_uno_6.collidepoint(x,y)
                    if over_carte_uno_6:
                       verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][5],derniere_carte_pose,nb_carte_pose)
                       if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][5]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][5]
                       if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                       if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                       if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 7:
                    if nb_rect > 13:
                        carte_rect_uno_7 = pygame.Rect(coo_rect_carte[6][0],642,coo_rect_carte[6][2],coo_rect_carte[6][3])
                    else:
                        carte_rect_uno_7 = pygame.Rect(coo_rect_carte[6])
                    over_carte_uno_7 = carte_rect_uno_7.collidepoint(x,y)
                    if over_carte_uno_7:
                        verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][6],derniere_carte_pose,nb_carte_pose)
                        if verification_carte:
                            derniere_carte_pose = deckJoueursUno["joueur1"][6]
                            nb_carte_pose += 1
                            del deckJoueursUno["joueur1"][6]
                        if verification_carte == "+4":
                            AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "changement_couleur":
                            derniere_carte_pose = couleur_choisi()
                            fin_de_tour = False
                        if verification_carte == "+2":
                            AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)


                if nb_rect >= 8:
                    carte_rect_uno_8 = pygame.Rect(coo_rect_carte[7])
                    over_carte_uno_8 = carte_rect_uno_8.collidepoint(x,y)
                    if over_carte_uno_8:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][7],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][7]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][7]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)


                if nb_rect >= 9:
                    carte_rect_uno_9 = pygame.Rect(coo_rect_carte[8])
                    over_carte_uno_9 = carte_rect_uno_9.collidepoint(x,y)
                    if over_carte_uno_9:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][8],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][8]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][8]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 10:
                    carte_rect_uno_10 = pygame.Rect(coo_rect_carte[9])
                    over_carte_uno_10 = carte_rect_uno_10.collidepoint(x,y)
                    if over_carte_uno_10:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][9],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][9]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][9]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 11:
                    carte_rect_uno_11 = pygame.Rect(coo_rect_carte[10])
                    over_carte_uno_11 = carte_rect_uno_11.collidepoint(x,y)
                    if over_carte_uno_11:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][10],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][10]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][10]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 12:
                    carte_rect_uno_12 = pygame.Rect(coo_rect_carte[11])
                    over_carte_uno_12 = carte_rect_uno_12.collidepoint(x,y)
                    if over_carte_uno_12:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][11],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][11]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][11]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 13:
                    carte_rect_uno_13 = pygame.Rect(coo_rect_carte[12])
                    over_carte_uno_13 = carte_rect_uno_13.collidepoint(x,y)
                    if over_carte_uno_13:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][12],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][12]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][12]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

                if nb_rect >= 14:
                    carte_rect_uno_14 = pygame.Rect(coo_rect_carte[13])
                    over_carte_uno_14 = carte_rect_uno_14.collidepoint(x,y)
                    if over_carte_uno_14:
                            verification_carte = AlgoUno.verification_carte(deckJoueursUno["joueur1"][13],derniere_carte_pose,nb_carte_pose)
                            if verification_carte:
                                derniere_carte_pose = deckJoueursUno["joueur1"][13]
                                nb_carte_pose += 1
                                del deckJoueursUno["joueur1"][13]
                            if verification_carte == "+4":
                                AlgoUno.ajouter_carte(4,deckJoueursUno[prochain_joueur],pioche)
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "changement_couleur":
                                derniere_carte_pose = couleur_choisi()
                                fin_de_tour = False
                            if verification_carte == "+2":
                                AlgoUno.ajouter_carte(2,deckJoueursUno[prochain_joueur],pioche)

        if len(deckJoueursUno["joueur1"]) == 0:
            resultat_fin_de_partie = True
            affichage = menu_fin_de_partie


        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()






def placement_cartes_uno(deck,pioche,carte_jeu):
    global coo_rect_carte,derniere_carte_pose
    coo_rect_carte = []
    etage = 585
    index_carte = 0

    for carte in deck:

        screen.blit(eval(carte),(25+(145*index_carte),etage))
        coo_rect_carte.append((25+(145*index_carte),etage,130,182))
        index_carte +=1
        if index_carte >=7:
            etage = 460
            index_carte = 0
    for carte_pioche in range(1,13):
        screen.blit(carte_back,(1105+(3*carte_pioche),530))
    screen.blit(eval(derniere_carte_pose),(570,230))


def couleur_choisi():
    couleur_choisi = ""
    couleur =["bleu","rouge","vert","jaune"]
    print("Veuillez choisir votre couleur (dans le input)")
    while couleur_choisi not in couleur:
        couleur_choisi =str(input("Quelle couleur demandez-vous ? (\"bleu\",\"rouge\",\"vert\",\"jaune\")"))
    if couleur_choisi == "bleu":
        return "carte_sc_bleu"
    elif couleur_choisi == "rouge":
        return "carte_sc_rouge"
    elif couleur_choisi == "vert":
        return "carte_sc_vert"
    elif couleur_choisi == "jaune":
        return "carte_sc_jaune"


def menu_fin_de_partie():
    global resultat_fin_de_partie, running
    screen.blit(bouton_retour_menuJeu,(490,580))

    if resultat_fin_de_partie == True:
        screen.blit(rp.texte.felicitation,((largeur//2.8),100))
        screen.blit(rp.texte.vous_gagnez,((largeur//2.7),200))
        screen.blit(rp.texte.vingt_jeton,((largeur//2.7),325))
        screen.blit(jeton,((largeur//2.15),460))
    else:
        screen.blit(rp.texte.dommage,((largeur//2.55),100))
        screen.blit(rp.texte.vous_perdez,((largeur//2.7),200))
        screen.blit(rp.texte.dix_jeton,((largeur//2.7),325))
        screen.blit(jeton,((largeur//2.15),460))
    x, y = pygame.mouse.get_pos()
    over_retour = bouton_rect_retour_fin_de_parti.collidepoint(x,y)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
           if over_retour:
                running = False
                pygame.quit()
                if resultat_fin_de_partie == True:
                    AlgoJetons.set_jeton(20)
                else:
                    AlgoJetons.set_jeton(-10)



        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()





#generation de la fenetre
pygame.init()
largeur,hauteur = 1280,720
background = (255,255,255)

pygame.display.set_caption("Uno - Projet Fin D'Année")        #Titre de la fenetre
screen = pygame.display.set_mode((largeur,hauteur)) #Taille fenetre

bouton_jouer = pygame.image.load("asset/bouton_jouer.png").convert_alpha()
bouton_rect_jouer = bouton_jouer.get_rect()
bouton_rect_jouer.move_ip(498,300)
bouton_regle = pygame.image.load("asset/bouton_regle.png").convert_alpha()
bouton_rect_regle = bouton_regle.get_rect()
bouton_rect_regle.move_ip(240,500)
bouton_retour_menuJeu = pygame.image.load("asset/bouton_retour.png").convert_alpha()
bouton_rect_retour_menuJeu = bouton_retour_menuJeu.get_rect()
bouton_rect_retour_menuJeu.move_ip(760,500)
bouton_rect_retour_fin_de_parti = bouton_retour_menuJeu.get_rect()
bouton_rect_retour_fin_de_parti.move_ip(495,580)
bouton_retour_regle = pygame.image.load("asset/bouton_retour.png").convert_alpha()
bouton_rect_retour_regle = bouton_retour_regle.get_rect()
bouton_rect_retour_regle.move_ip(500,517)
txt_regle_uno = pygame.image.load("asset/regle_uno.png").convert_alpha()
txt_relge_uno_rect = txt_regle_uno.get_rect()
bouton_2j = pygame.image.load("asset/bouton_2joueurs.png").convert_alpha()
bouton_rect_2j = bouton_2j.get_rect()
bouton_rect_2j.move_ip(largeur//2.7,150)
bouton_3j = pygame.image.load("asset/bouton_3joueurs.png").convert_alpha()
bouton_rect_3j = bouton_3j.get_rect()
bouton_rect_3j.move_ip(largeur//2.7,350)
bouton_4j = pygame.image.load("asset/bouton_4joueurs.png").convert_alpha()
bouton_rect_4j = bouton_4j.get_rect()
bouton_rect_4j.move_ip(largeur//2.7,550)



icone_ordi1 = pygame.image.load("asset/ordi_1.png")
icone_ordi2 = pygame.image.load("asset/ordi_2.png")
icone_ordi3 = pygame.image.load("asset/ordi_3.png")
#--------CARTE UNO---------
carte_0_bleu = pygame.image.load("carte_uno/blue_0.png").convert_alpha()
carte_1_bleu = pygame.image.load("carte_uno/blue_1.png").convert_alpha()
carte_2_bleu = pygame.image.load("carte_uno/blue_2.png").convert_alpha()
carte_3_bleu = pygame.image.load("carte_uno/blue_3.png").convert_alpha()
carte_4_bleu = pygame.image.load("carte_uno/blue_4.png").convert_alpha()
carte_5_bleu = pygame.image.load("carte_uno/blue_5.png").convert_alpha()
carte_6_bleu = pygame.image.load("carte_uno/blue_6.png").convert_alpha()
carte_7_bleu = pygame.image.load("carte_uno/blue_7.png").convert_alpha()
carte_8_bleu = pygame.image.load("carte_uno/blue_8.png").convert_alpha()
carte_9_bleu = pygame.image.load("carte_uno/blue_9.png").convert_alpha()
carte_p2_bleu = pygame.image.load("carte_uno/blue_picker.png").convert_alpha()
carte_in_bleu = pygame.image.load("carte_uno/blue_reverse.png").convert_alpha()


carte_0_vert = pygame.image.load("carte_uno/green_0.png").convert_alpha()
carte_1_vert = pygame.image.load("carte_uno/green_1.png").convert_alpha()
carte_2_vert = pygame.image.load("carte_uno/green_2.png").convert_alpha()
carte_3_vert = pygame.image.load("carte_uno/green_3.png").convert_alpha()
carte_4_vert = pygame.image.load("carte_uno/green_4.png").convert_alpha()
carte_5_vert = pygame.image.load("carte_uno/green_5.png").convert_alpha()
carte_6_vert = pygame.image.load("carte_uno/green_6.png").convert_alpha()
carte_7_vert = pygame.image.load("carte_uno/green_7.png").convert_alpha()
carte_8_vert = pygame.image.load("carte_uno/green_8.png").convert_alpha()
carte_9_vert = pygame.image.load("carte_uno/green_9.png").convert_alpha()
carte_p2_vert = pygame.image.load("carte_uno/green_picker.png").convert_alpha()
carte_in_vert = pygame.image.load("carte_uno/green_reverse.png").convert_alpha()

carte_0_rouge = pygame.image.load("carte_uno/red_0.png").convert_alpha()
carte_1_rouge = pygame.image.load("carte_uno/red_1.png").convert_alpha()
carte_2_rouge = pygame.image.load("carte_uno/red_2.png").convert_alpha()
carte_3_rouge = pygame.image.load("carte_uno/red_3.png").convert_alpha()
carte_4_rouge = pygame.image.load("carte_uno/red_4.png").convert_alpha()
carte_5_rouge = pygame.image.load("carte_uno/red_5.png").convert_alpha()
carte_6_rouge = pygame.image.load("carte_uno/red_6.png").convert_alpha()
carte_7_rouge = pygame.image.load("carte_uno/red_7.png").convert_alpha()
carte_8_rouge = pygame.image.load("carte_uno/red_8.png").convert_alpha()
carte_9_rouge = pygame.image.load("carte_uno/red_9.png").convert_alpha()
carte_p2_rouge = pygame.image.load("carte_uno/red_picker.png").convert_alpha()
carte_in_rouge = pygame.image.load("carte_uno/red_reverse.png").convert_alpha()


carte_0_jaune = pygame.image.load("carte_uno/yellow_0.png").convert_alpha()
carte_1_jaune = pygame.image.load("carte_uno/yellow_1.png").convert_alpha()
carte_2_jaune = pygame.image.load("carte_uno/yellow_2.png").convert_alpha()
carte_3_jaune = pygame.image.load("carte_uno/yellow_3.png").convert_alpha()
carte_4_jaune = pygame.image.load("carte_uno/yellow_4.png").convert_alpha()
carte_5_jaune = pygame.image.load("carte_uno/yellow_5.png").convert_alpha()
carte_6_jaune = pygame.image.load("carte_uno/yellow_6.png").convert_alpha()
carte_7_jaune = pygame.image.load("carte_uno/yellow_7.png").convert_alpha()
carte_8_jaune = pygame.image.load("carte_uno/yellow_8.png").convert_alpha()
carte_9_jaune = pygame.image.load("carte_uno/yellow_9.png").convert_alpha()
carte_p2_jaune = pygame.image.load("carte_uno/yellow_picker.png").convert_alpha()
carte_in_jaune = pygame.image.load("carte_uno/yellow_reverse.png").convert_alpha()


carte_chcouleur = pygame.image.load("carte_uno/wild_color_changer.png").convert_alpha()
carte_p4 = pygame.image.load("carte_uno/wild_pick_four.png").convert_alpha()
carte_back = pygame.image.load("carte_uno/card_back.png").convert_alpha()
carte_sc_bleu = pygame.image.load("carte_uno/blue_.png").convert_alpha()
carte_sc_vert = pygame.image.load("carte_uno/green_.png").convert_alpha()
carte_sc_rouge = pygame.image.load("carte_uno/red_.png").convert_alpha()
carte_sc_jaune = pygame.image.load("carte_uno/yellow_.png").convert_alpha()



carte_pioche_uno_rect = carte_back.get_rect()
carte_pioche_uno_rect.move_ip(1141,530)

#--------BOUTON UNO---------


bouton_pioche_uno = pygame.image.load("asset/bouton.jpg").convert_alpha()

bouton_rect_pioche_uno = bouton_pioche_uno.get_rect()
bouton_rect_pioche_uno.move_ip(150,475)
bouton_finTour_uno = pygame.image.load("asset/bouton_findetour.png").convert_alpha()
bouton_rect_finTour_uno = bouton_finTour_uno.get_rect()
bouton_rect_finTour_uno.move_ip(1100,430)

#-------------------------------------------------------------------------------

texte_nb_jetons = ressourcePygame.font.render(str(AlgoJetons.get_jeton()), 1, (0, 0, 0))
jeton = pygame.image.load("asset/jetons.png").convert_alpha()
jeton = pygame.transform.scale(jeton,(75,75))

fin_de_tour = True
derniere_carte_pose, prochain_joueur , joueur_actuel = "", "",""
resultat_fin_de_partie = True
nb_joueur,nb_carte_pose = 0,0
derniere_carte_pose,coo_rect_carte = [],[]
pioche = []
deckJoueursUno = {}
running = True
affichage = menu_uno
while running:

    screen.fill(background)
    affichage()
    if running:

        pygame.display.flip()
    else:
        pygame.quit()
        sys.exit()







