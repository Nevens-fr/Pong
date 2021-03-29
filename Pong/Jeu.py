import pygame as pg
from Joueur import *
from Balle import *
from IA import *

#permet de jouer contre l'ia
def jeu(screen, WIN_WIDTH, WIN_HEIGHT, myfont, nbPlayer):

    
    vitesse = 1
    temps = pg.time.get_ticks()

    ## Création des joueurs et balle
    j1 = Joueur(0, WIN_HEIGHT / 2 - (WIN_HEIGHT * 0.3)/2, WIN_HEIGHT, WIN_WIDTH)
    if nbPlayer == 1:
        j2 = IA(WIN_WIDTH - WIN_WIDTH * 0.02, WIN_HEIGHT / 2 - (WIN_HEIGHT * 0.3)/2, WIN_HEIGHT, WIN_WIDTH)
    else:
        j2 = Joueur(WIN_WIDTH - WIN_WIDTH * 0.02, WIN_HEIGHT / 2 - (WIN_HEIGHT * 0.3)/2, WIN_HEIGHT, WIN_WIDTH)

    balle = Balle(WIN_HEIGHT, WIN_WIDTH)

    continuer = True

    ## Boucle de jeu
    while continuer:

        if j1.getPoint() == 10 or j2.getPoint() == 10:
            continuer = False
            pg.time.wait(4000)
            return True

        event = pg.key.get_pressed()
        
        if(nbPlayer == 1):
        # IA
            j2.updateY(WIN_WIDTH, balle)
        else:
            # Déplacement J1
            if event[pg.K_UP]:
                j2.updateY('-', 5)
            if event[pg.K_DOWN]:
                j2.updateY('+', 5)

        # Déplacement J1
        if event[pg.K_z]:
            j1.updateY('-', 5)
        if event[pg.K_s]:
            j1.updateY('+', 5)

        # Pour quitter la fenetre
        if event[pg.K_ESCAPE]:
            continuer = False
        for events in pg.event.get():
            if events.type == pg.QUIT:
                exit()

        balle.deplace(vitesse)



        ##Vérification des positions
        j1.checkPos(WIN_HEIGHT)
        j2.checkPos(WIN_HEIGHT)
        
        pointMarque, touche = balle.checkPos(WIN_WIDTH, WIN_HEIGHT, j1,j2)

        if pointMarque:
            balle = Balle(WIN_HEIGHT, WIN_WIDTH)
            vitesse = 1
            temps = pg.time.get_ticks()
        elif touche: # on augmente la vitesse de la balle si elle a touchée une raquette
            if(temps + 1000 <= pg.time.get_ticks()):
                temps = pg.time.get_ticks()
                vitesse += 1

        ## Nettoyage de l'écran et affichage des nouvelles positions
        textJ1 = myfont.render(str(j1.getPoint()), False, (255, 255, 255))
        textJ2 = myfont.render(str(j2.getPoint()), False, (255, 255, 255))

        screen.fill(0)
        screen.blit(textJ1,(75, 5))
        screen.blit(textJ2,(600, 5))
        pg.draw.rect(screen, pg.Color(25,25,255), j2.getBarre())
        pg.draw.rect(screen, pg.Color(255,120,255), j1.getBarre())
        pg.draw.rect(screen, pg.Color(255,255,255), balle.getBarre())
        pg.display.flip()