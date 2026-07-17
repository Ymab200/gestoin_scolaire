class Matiere :

    def __init__(self, nom , coef):
        self.nom = nom
        self.coef = coef
    def afficher(self):
        print(f"La matirer de {self.nom} a pour coeficient {self.coef}")