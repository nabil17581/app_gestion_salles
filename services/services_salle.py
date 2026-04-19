from Data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Toutes les informations doivent être saisies."


        if salle.capacite < 1:
            return False, "Valeur invalide : une salle doit accueillir au moins 1 personne."


        self.dao_salle.add_data(salle)

        return True, "Salle ajoutée avec succès."
