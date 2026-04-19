from models.salle import Salle
from services.services_salle import ServiceSalle
import customtkinter as ctk



class ViewSalle:
    def __init__(self):
        self.service_salle = ServiceSalle()

        #Fenetre principal
        self.app = ctk.CTk()
        self.app.title("Gestion des salles")
        self.app.geometry("800x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        #Cadre Information salle

        self.frame_info = ctk.CTkFrame(self.app)
        self.frame_info.pack(padx=10, pady=10)

        self.label_code = ctk.CTkLabel(self.frame_info, text="Code salle :")
        self.label_code.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_code = ctk.CTkEntry(self.frame_info)
        self.entry_code.grid(row=1, column=1, padx=10, pady=5)

        self.label_desc = ctk.CTkLabel(self.frame_info, text="Description :")
        self.label_desc.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_desc = ctk.CTkEntry(self.frame_info)
        self.entry_desc.grid(row=2, column=1, padx=10, pady=5)

        self.label_cat = ctk.CTkLabel(self.frame_info, text="Catégorie :")
        self.label_cat.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.entry_cat = ctk.CTkEntry(self.frame_info)
        self.entry_cat.grid(row=3, column=1, padx=10, pady=5)

        self.label_cap = ctk.CTkLabel(self.frame_info, text="Capacité :")
        self.label_cap.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.entry_cap = ctk.CTkEntry(self.frame_info)
        self.entry_cap.grid(row=4, column=1, padx=10, pady=5)

        #Cadre actions

        self.frame_action = ctk.CTkFrame(self.app)
        self.frame_action.pack(padx=10, pady=10)

        self.btn_ajouter = ctk.CTkButton(self.frame_action, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.frame_action, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer= ctk.CTkButton(self.frame_action, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.frame_action, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def get_info(self):
        code = self.entry_code.get()
        description = self.entry_desc.get()
        categorie = self.entry_cat.get()
        capacite = self.entry_cap.get()

        salle = Salle(code, description, categorie, capacite)
        return salle






    #Ajouter une salle
    def ajout_salle(self):

        salle_add = self.get_info()

        msg = self.service_salle.ajouter_salle(salle_add)
        print(msg)

    #Modifier salle
    def update_salle(self):
        salle_update = self.get_info()
        msg = self.service_salle.modifier_salle(salle_update)
        print(msg)



    def run(self):
        self.app.mainloop()







