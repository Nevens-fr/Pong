from Joueur import *

class IA(Joueur):

    #constructeur
    def __init__(self, x , y, WIN_HEIGHT, WIN_WIDTH):

        Joueur.__init__(self, x,y, WIN_HEIGHT, WIN_WIDTH)
        self.departY = y

    # modifie la position en hauteur du joueur
    def updateY(self, ope, balle):

        if self.time +10 <= pg.time.get_ticks():
            self.time = pg.time.get_ticks()

            # La raquette se replace au centre
            if balle.directionX == 1:
                if self.barre.y  < self.departY:
                    self.barre.y += 2
                elif self.barre.y  > self.departY:
                    self.barre.y -= 2

            else:
                #On essaie de prévoir la trajectoire de la balle
                print("come")

          