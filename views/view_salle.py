from tkinter import messagebox, ttk

from models.salle import Salle
from services.services_salle import ServiceSalle
import customtkinter as ctk



class ViewSalle():
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

        self.btn_rechercher = ctk.CTkButton(self.frame_action, text="Rechercher",command=self.get_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self.app, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "description", "categorie", "capacite"),show="headings")

        # En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        # Largeur des colonnes

        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
        self.lister_salles()




    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))




    def get_info(self):
        code = self.entry_code.get()
        description = self.entry_desc.get()
        categorie = self.entry_cat.get()
        cap = self.entry_cap.get()

        if cap == "":
            messagebox.showerror("Erreur", "La capacité est obligatoire")
            return None

        try:
            capacite = int(cap)
        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre")
            return None



        return Salle(code, description, categorie, capacite)








    #Ajouter une salle
    def add_salle(self):

        salle_add = self.get_info()

        if salle_add is None:
            return
        if len(salle_add.code)>5:
            messagebox.showerror("Erreur", "La taille maximale du code doit etre 5 caracteres ")
            return



        resultat,message = self.service_salle.ajouter_salle(salle_add)
        self.lister_salles()
        if resultat :
            messagebox.showinfo("Bravo", message)

        else:
            messagebox.showerror("Erreur", message)



    #Modifier salle
    def update_salle(self):
        salle_update = self.get_info()

        resultat,message = self.service_salle.modifier_salle(salle_update)
        if resultat:
            messagebox.showinfo("Bravo", message)

        else:
            messagebox.showerror("Erreur", message)


    #Supprimer salle
    def del_salle(self):
        code_del = self.entry_code.get()
        resultat,message=self.service_salle.supprimer_salle(code_del)
        if resultat:
            messagebox.showinfo("Bravo", message)

        else:
            messagebox.showerror("Erreur", message)

    #Rechercher salle


    def get_salle(self):

        code_get = self.entry_code.get()

        if not code_get:
            messagebox.showerror("Erreur", "Veuillez entrer un code")
            return

        resultat= self.service_salle.rechercher_salle(code_get)

        if not resultat:
            messagebox.showerror("Erreur", "Salle introuvable")
            return

        self.entry_desc.delete(0, "end")
        self.entry_desc.insert(0, resultat.description)

        self.entry_cat.delete(0, "end")
        self.entry_cat.insert(0, resultat.categorie)

        self.entry_cap.delete(0, "end")
        self.entry_cap.insert(0, str(resultat.capacite))

        message = (
            f"--------SALLE--------\n"
            f"Code : {resultat.code}\n"
            f"Description : {resultat.description}\n"
            f"Catégorie : {resultat.categorie}\n"
            f"Capacité : {resultat.capacite}"
        )

        messagebox.showinfo("Résultat recherche", message)










    def run(self):
        self.app.mainloop()









