class Eleve :
    def __init__(self, nom , age , classe):
        self.nom = nom
        self.age = age
        self.classe = classe
    def afficher_eleve(self):
        print(f"Il s'agi de l'eleve {self.nom} ages de {self.age} et de classe {self.classe}")