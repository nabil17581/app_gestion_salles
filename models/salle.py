class Salle:
    def __init__(self, code,description,categorie,capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite
    def afficher_infos(self):
        print(f"La salle({self.code}): {self.description}.´\nCategories: {self.categorie}\nCapacite: {self.capacite}")




