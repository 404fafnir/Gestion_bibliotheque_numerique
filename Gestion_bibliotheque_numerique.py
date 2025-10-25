# Système de Gestion Bibliothèque Numérique

class Livre:
    def __init__(self, identifiant, titre, auteur, categorie, nbexemplaires):
        self.identifiant = identifiant
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.nbexemplaires = nbexemplaires
        self.status = "disponible" if nbexemplaires > 0 else "emprunté"

    def __str__(self):
        return f"[{self.identifiant}] {self.titre} - {self.auteur} ({self.categorie}) | {self.nbexemplaires} exemplaires | {self.status}"


class Utilisateur:
    def __init__(self, identifiant, nom, email):
        self.identifiant = identifiant
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.nom} ({self.email})"

class Lecteur(Utilisateur):
    def __init__(self, identifiant, nom, email, usertype):
        Utilisateur.__init__(self, identifiant, nom, email)
        self.usertype = "lecteur"
    pass

class Bibliothecaire(Utilisateur):
    def __init__(self, identifiant, nom, email, usertype):
        Utilisateur.__init__(self, identifiant, nom, email)
        self.usertype = "bibliothecaire"
    pass

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = {}
        self.emprunts = {}

    def ajouter_livres(self, livre):
        for i in self.livres:
            if (i.identifiant == livre.identifiant) or (i.titre.lower() == livre.titre.lower()):
                print("/!\ Ce livre existe déjà")
                return
            self.livres.append(livre)
            print(f"Livre ajouté : {livre.titre} - {livre.auteur} ({livre.categorie} - {livre.nbexemplaires})")

    def supprimer_livres(self, id_livre):
        pass

    def afficher_livres(self):
        pass

    def rechercher_livres(self):
        pass

    def ajouter_utilisateur(self, utilisateur):
        pass

    def supprimer_utilisateur(self, utilisateur):
        pass

    def emprunter_livre(self):
        pass

    def rendre_livres(self):
        pass

    def statistiques_livres(self):
        pass
