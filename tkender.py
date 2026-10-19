import tkinter as tk
from tkinter import messagebox

# ======================
# Classe Projet (POO)
# ======================
class Projet:
    def __init__(self, nom, responsable, budget, duree):
        self.nom = nom
        self.responsable = responsable
        self.budget = budget
        self.duree = duree

    def details(self):
        return (
            f"Nom du projet : {self.nom}\n"
            f"Responsable : {self.responsable}\n"
            f"Budget : {self.budget} DH\n"
            f"Durée : {self.duree} mois"
        )

# ======================
# Classe Application
# ======================
class GestionEntreprise:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Gestion d'entreprise")
        self.fenetre.geometry("400x400")

        # Labels et Entrées
        tk.Label(fenetre, text="Nom du projet").pack()
        self.entry_nom = tk.Entry(fenetre)
        self.entry_nom.pack()

        tk.Label(fenetre, text="Responsable").pack()
        self.entry_responsable = tk.Entry(fenetre)
        self.entry_responsable.pack()

        tk.Label(fenetre, text="Budget (DH)").pack()
        self.entry_budget = tk.Entry(fenetre)
        self.entry_budget.pack()

        tk.Label(fenetre, text="Durée (mois)").pack()
        self.entry_duree = tk.Entry(fenetre)
        self.entry_duree.pack()

        # Bouton
        tk.Button(
            fenetre,
            text="Enregistrer le projet",
            command=self.creer_projet
        ).pack(pady=10)

        # Zone d'affichage
        self.resultat = tk.Text(fenetre, height=8, width=45)
        self.resultat.pack()

    def creer_projet(self):
        try:
            nom = self.entry_nom.get()
            responsable = self.entry_responsable.get()
            budget = float(self.entry_budget.get())
            duree = int(self.entry_duree.get())

            projet = Projet(nom, responsable, budget, duree)

            self.resultat.delete(1.0, tk.END)
            self.resultat.insert(tk.END, projet.details())

        except ValueError:
            messagebox.showerror(
                "Erreur",
                "Veuillez entrer des valeurs valides"
            )

# ======================
# Programme principal
# ======================
fenetre = tk.Tk()
app = GestionEntreprise(fenetre)
fenetre.mainloop()
