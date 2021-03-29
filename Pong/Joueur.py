import pygame as pg

# Représentation du rectangle du joueur
class Joueur:

    #constructeur
    def __init__(self, x , y, WIN_HEIGHT, WIN_WIDTH):

        self.barre = pg.Rect(x,y,WIN_WIDTH *0.02, WIN_HEIGHT * 0.2)
        self.hauteur = WIN_HEIGHT * 0.2
        self.time = pg.time.get_ticks()
        self.point = 0

    # retourne le rectangle du joueur
    def getBarre(self):
        return self.barre

    #incrément le score
    def addPt(self, score):
        self.point += score

    #retourne le score du joueur
    def getPoint(self):
        return self.point

    # modifie la position en hauteur du joueur
    def updateY(self, op, val):
        if self.time +10 <= pg.time.get_ticks():
            self.time = pg.time.get_ticks()
            if (op == '-'):
                self.barre.y -= val
            else :
                self.barre.y += val

    # Vérifie que la barre ne sort pas de l'écran et la replace correctement si besoin
    def checkPos(self, WIN_HEIGHT):
        if(self.barre.y < 0):
            self.barre.y = 0
        if(self.barre.y + self.hauteur > WIN_HEIGHT):
            self.barre.y = WIN_HEIGHT - self.hauteur
    