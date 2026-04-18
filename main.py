from Data.dao_salle import DataSalle
from models.salle import Salle

salle = Salle("S101","Salle équipée d’un projecteur.","Informatique",25)
salle2 = Salle("S102","Salle  table centrale et écran.","Réunion",12)
salle3= Salle("S103","Salle polyvalente adaptée aux formations.","Atelier",36)

data = DataSalle()
affiche = data.get_data("S101")
print(affiche)



