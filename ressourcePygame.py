import pygame
pygame.font.init()
from pygame.locals import *
import AlgoJetons


font = pygame.font.SysFont('helvetic', 70)
font_info = pygame.font.SysFont('helvetic',35)

largeur,hauteur = 1280,720

class texte:
    monnaie = font.render("0", 1, (0,0,0))
    titre_menu = font.render("PROJET JEU DE CARTES", 1, (255,0,0))
    titre_menu_uno = font.render("UNO", 1, (255,0,0))
    titre_regle_uno = font.render("REGLE DU UNO", 1, (0,0,0))
    regle_uno = font.render("REGLE DU UNO", 1, (0,0,0))
    titre_menu_solitaire = font.render("SOLITAIRE",1,(0,0,255))
    regle_solitaire = font.render("REGLE DU SOLIATAIRE",1,(0,0,0))
    choix_nombre_ordi = font.render("CHOISSISEZ LE NOMBRE D'ORDINATEUR",1,(0,0,0))
    felicitation = font.render("FELICITATION !",1,(0,0,0))
    dommage = font.render("Dommage !",1,(0,0,0))
    vous_gagnez = font.render("vous gagnez :",1,(0,0,0))
    vingt_jeton =  font.render("+ 20 jetons !",1,(0,0,0))
    vous_perdez = font.render("vous perdez :",1,(0,0,0))
    dix_jeton =  font.render("- 10 jetons !",1,(0,0,0))
    nb_jeton = font.render(str(AlgoJetons.get_jeton()),1,(0,0,0))

