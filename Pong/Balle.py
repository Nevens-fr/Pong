import pygame as pg

#Classe représentant une balle
class Balle:

    # Constructeur
    def __init__(self, WIN_HEIGHT, WIN_WIDTH):

        self.hauteur = 20
        self.largeur = 20
        self.directionX = 1
        self.directionY = 0
        self.time = pg.time.get_ticks()
        self.barre = pg.Rect(WIN_WIDTH / 2, WIN_HEIGHT/2, self.largeur, self.hauteur)

    # retourne le rectangle de la balle
    def getBarre(self):
        return self.barre

    #deplace la balle sur l'écran
    def deplace(self, vitesse):
        if self.time +10 <= pg.time.get_ticks():
            self.time = pg.time.get_ticks()
            if self.directionX == 0:
                self.barre.x += vitesse
            else:
                self.barre.x -= vitesse
            
            if self.directionY == 0:
                self.barre.y += vitesse
            else:
                self.barre.y -= vitesse
        
    #Vérifie que la balle ne sort pas de l'écran
    def checkPos(self, WIN_WIDTH, WIN_HEIGHT, j1, j2):

        touche = False # vrai si une raquette est touchée par la balle

        if self.barre.colliderect(j1.getBarre()):
            self.directionX = 0
            touche = True
            if self.directionY == 0:
                self.directionY = 1
            else :
                self.directionY = 0
        if self.barre.colliderect(j2.getBarre()):
            self.directionX = 1
            touche = True
            if self.directionY == 0:
                self.directionY = 1
            else :
                self.directionY = 0

        if self.barre.y <= 0:
            self.directionY = 0
        if self.barre.y + self.hauteur >= WIN_HEIGHT:
            self.directionY = 1
        
        if self.barre.x <= 0:
            self.directionX = 0
            j2.addPt(1)
            return True, touche
        if self.barre.x + self.largeur >= WIN_WIDTH:
            self.directionX = 1
            j1.addPt(1)
            return True, touche

        return False, touche