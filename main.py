from Data.dao_salle import DataSalle
from models.salle import Salle
from services.services_salle import ServiceSalle

salle = Salle("S101","Salle équipée d’un projecteur.","Informatique",25)
salle2 = Salle("S104","Salle  table centrale et écran.","Réunion",20)
salle3= Salle("S103","Salle polyvalente adaptée aux formations.","Formation",0)

data= DataSalle()
data.add_data(salle2)




