from Joueur import *

class IA(Joueur):

    #constructeur
    def __init__(self, x , y, WIN_HEIGHT, WIN_WIDTH):

        Joueur.__init__(self, x,y, WIN_HEIGHT, WIN_WIDTH)
        self.departY = y + 25
        self.win_height = WIN_HEIGHT

    # modifie la position en hauteur du joueur
    def updateY(self, WIN_WIDTH, balle):

        if self.time +10 <= pg.time.get_ticks():
            self.time = pg.time.get_ticks()

            # La raquette se replace au centre
            if balle.directionX == 1:
                if self.barre.y  < self.departY:
                    self.barre.y += 2
                elif self.barre.y  > self.departY:
                    self.barre.y -= 2

            elif balle.barre.x >= WIN_WIDTH / 2:

                if balle.barre.y < self.win_height * 0.75:

                    if balle.directionY == 0 and balle.barre.y >= self.win_height * 0.80: #la balle va percuter un mur avant d'arriver
                        a = 1
                    elif balle.directionY == 1 and balle.barre.y <= self.win_height * 0.2:#la balle va percuter un mur avant d'arriver
                        a = 1
                    else:
                        if balle.barre.y - 20 < self.barre.y and balle.directionY == 1:
                            self.barre.y -= 3
                        elif balle.barre.y + 20 > self.barre.y and balle.directionY == 0:
                            self.barre.y += 3