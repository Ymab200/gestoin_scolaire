class Note:
    def __init__(self, nom , matiere , valeur):
        self.nom = nom
        self.matiere = matiere
        self.valeur = valeur
    def afficher_note(self):
        print(f"L'eleve {self.nom} a obtenu une note de {self.valeur} en {self.matiere}")