# coding=utf-8
class Brick(): 

    #attribut de classe un dictionnaire de couleurs

    COLORS = {1: "#FFFF99", 2: "#FC7BD5", 3: "#48E1BD"}

    def __init__(self, x, y, hits):# le constructeur

        self.w = 75 # attribut longueur

        self.h = 20 # attreibut largeur

        self.pos = PVector(x, y) # attribut position

        self.hits = hits #attribut clé pour la couleur

        self.col = Brick.COLORS[hits] # la couleur

        

    # méthode pour afficher la brique

    def display(self):

        fill(self.col)

        stroke("#ffffff") # couleur du bord

        strokeWeight(2)# épaisseur des bords

        rect(self.pos.x, self.pos.y, self.w, self.h)
