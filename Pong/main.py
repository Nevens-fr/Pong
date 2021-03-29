from menu import *
from Jeu import *



pg.init()
pg.font.init()

WIN_WIDTH = 700
WIN_HEIGHT = 400

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pg.display.set_caption("Pong")

logo = pg.image.load("icone.png")

pg.display.set_icon(logo)

myfont = pg.font.SysFont("Comic Sans MS", 30)

continuer = True

while continuer:
    if menu(screen, WIN_WIDTH, WIN_HEIGHT, myfont):
        jeu(screen, WIN_WIDTH, WIN_HEIGHT, myfont, 1)
    else:
        jeu(screen, WIN_WIDTH, WIN_HEIGHT, myfont, 2)