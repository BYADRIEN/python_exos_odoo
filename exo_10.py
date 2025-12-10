class Voiture:
    def __init__(self, marque, modele, annee )
    self.marque = marque
    self.model = modele
    self.annee =annee

    def klaxonner(self):
        print("tu tut !")

cybertruck = Voiture(marque="tesla", modele="cybertruck", annee="2024")

print(dir(cybertruck))