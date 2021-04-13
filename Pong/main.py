from menu import *
from Jeu import *

##
# Création et set up de la fenetre

pg.init()
pg.font.init()

WIN_WIDTH = 700
WIN_HEIGHT = 400

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pg.display.set_caption("Pong")

logo = pg.image.load("icone.png")

pg.display.set_icon(logo)

myfont = pg.font.SysFont("Comic Sans MS", 30)

##
# Affichage du logo

logo = pg.image.load("logo_NS.png")

screen.blit(logo,(WIN_WIDTH / 2 - 480 / 2, WIN_HEIGHT / 2 - 290 / 2))

pg.display.flip()

pg.time.wait(2500)

##
# Boucle principale du programme
continuer = True

while continuer:
    if menu(screen, WIN_WIDTH, WIN_HEIGHT, myfont):
        jeu(screen, WIN_WIDTH, WIN_HEIGHT, myfont, 1)
    else:
        jeu(screen, WIN_WIDTH, WIN_HEIGHT, myfont, 2)