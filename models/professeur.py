class Professeur :
    def __init__(self, nom ,matiere):
        self.nom = nom
        self.matiere = matiere
    def enseigner(self):
        print(f"Mr {self.nom} enseigne la matiere {self.matiere}")