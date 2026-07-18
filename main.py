from models import Eleve , Professeur , Note , Matiere

def main():
    while True:
        print("Bienvenue a tous !")
        print("1. Afficher les eleves ")
        print("2 .Afficher les professeurs")
        print("3. Afficher les matieres")
        print("4. Afficher les notes")

        n = (input("Faites votre choix : "))
        try :
            n = int(n)
        except ValueError  :
            print("Vous avez entrer un caraterer non autaurise !")
            continue

        if n == 1:
            nom = str(input("Entrer le nom pour le creer :"))
            age = int(input("Entrer l'age pour le creer :"))
            classe = str(input("Entrer la classe pour le creer :"))
            e = Eleve(nom, age , classe)
            e.afficher_eleve()

        elif n == 2:
            nom = str(input("Entrer le nom pour le creer :"))
            matiere = str(input("Entrer la matiere pour le creer :"))
            p = Professeur(nom, matiere)
            p.enseigner()
        elif n ==3:
            nom = str(input("Entrer le nom pour le creer :"))
            coef = int(input("Entrer le coef pour le creer :"))
            m = Matiere(nom, coef)
            m.afficher()
        elif n == 4:
            nom = str(input("Entrer le nom pour le creer :"))
            matiere = str(input("Entrer la matiere pour le creer :"))
            valeur = int(input("Entrer la valeur pour le creer :"))
            n = Note(nom, matiere, valeur)
            n.afficher_note()





main()