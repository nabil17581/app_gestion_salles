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

        self.btn_ajouter = ctk.CTkButton(self.frame_action, text="Ajouter",command=self.add_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.frame_action, text="Modifier",command=self.update_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer= ctk.CTkButton(self.frame_action, text="Supprimer",command= self.del_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.frame_action, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def get_info(self):
        code = self.entry_code.get()
        description = self.entry_desc.get()
        categorie = self.entry_cat.get()
        capacite = int(self.entry_cap.get())


        salle = Salle(code, description, categorie, capacite)
        return salle









    #Ajouter une salle
    def add_salle(self):

        salle_add = self.get_info()

        resultat = self.service_salle.ajouter_salle(salle_add)
        print(resultat)

    #Modifier salle
    def update_salle(self):
        salle_update = self.get_info()

        resultat = self.service_salle.modifier_salle(salle_update)
        print(resultat)


    #Supprimer salle
    def del_salle(self):
        code_del = self.entry_code.get()
        msg=self.service_salle.supprimer_salle(code_del)
        print(msg)

    #Rechercher salle
    """def get_salle(self):
        code_get = self.entry_code.get()
        resultat = self.service_salle.rechercher_salle(code_get)
        if resultat:

            self.entry_desc.delete(0, "end")
            self.entry_desc.insert(0, resultat.description)

            self.entry_cat.delete(0, "end")
            self.entry_cat.insert(0, resultat.categorie)

            self.entry_cap.delete(0, "end")
            self.entry_cap.insert(0, str(resultat.capacite))"""






    def run(self):
        self.app.mainloop()







