from Data.dao_salle import DataSalle
from models.salle import Salle


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

    def modifier_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or not salle.description :
            return False, "Toutes les informations doivent être saisies."

        if salle.capacite is  None or salle.capacite < 1:

            return False, "Valeur invalide : une salle doit accueillir au moins 1 personne."
        else:
            self.dao_salle.update_data(salle)
            return True, "Salle modifier avec succès."






    def supprimer_salle(self,code):

        if not code  :
            return False, "Code obligatoire !"

        suppression = self.dao_salle.delete_data(code)

        if suppression:
             return True, "Salle Supprimée "
        else:
             return False, "Aucune salle trouvée avec ce code"

    def rechercher_salle(self,code):
        code_exists = self.dao_salle.get_data(code)
        if code_exists is False:
            return None
        else :
            return code_exists


    def recuperer_salles(self):
        table = self.dao_salle.get_salles()
        if table is False:
            print("Table vide! Aucune insformations existante ")
        else :
            for salle in table:
                Salle.afficher_infos(salle)







