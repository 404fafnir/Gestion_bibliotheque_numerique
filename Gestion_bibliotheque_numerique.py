# Système de Gestion Bibliothèque Numérique

class Livre:

    _id = 0 # id de base

    def __init__(self, titre, auteur, categorie, nbexemplaires):
        self.identifiant = Livre._id
        Livre._id += 1
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
    def __init__(self, identifiant, nom, email):
        Utilisateur.__init__(self, identifiant, nom, email)
        self.usertype = "lecteur"
    pass

class Bibliothecaire(Utilisateur):
    def __init__(self, identifiant, nom, email):
        Utilisateur.__init__(self, identifiant, nom, email)
        self.usertype = "bibliothecaire"
    pass

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = {}
        self.emprunts = {}

    def autorisation(self, utilisateur):
        if isinstance(utilisateur, Bibliothecaire):
            return True
        else:
            return False

    def ajouter_livres(self,livre, utilisateur):
        if not self.autorisation(utilisateur):
            print('/!\ Accès refusé.')
            return
        for i in self.livres:
            if (i.identifiant == livre.identifiant) or (i.titre.lower() == livre.titre.lower()):
                print("/!\ Ce livre existe déjà")
                return
        self.livres.append(livre)
        print(f"Livre ajouté : {livre.titre} - {livre.auteur} ({livre.categorie} - {livre.nbexemplaires})")

    def modifier_livres(self, livre, modification, utilisateur):
        if not self.autorisation(utilisateur):
            print('/!\ Accès refusé.')
            return
        attribut,valeur= modification
        for i in self.livres:
            if (i.identifiant == livre.identifiant):
                if hasattr(i, attribut):
                    setattr(i, attribut, valeur)
                else:
                    print("/!\ Un livre n'a pas cette attribut :",attribut)
                return
        print("/!\ Le livre n'a pas pu être modifier. (Mauvais identifiant)")


    def supprimer_livres(self, livre, utilisateur):
        if not self.autorisation(utilisateur):
            print("/!\ Accès refusé.")
            return
        for i in self.livres:
            if (i.identifiant == livre.identifiant):
                self.livres.remove(livre)
                print("Livre supprimé correctement.")
                return
        print("/!\ Le livre n'a pas pu être supprimer. (Mauvais identifiant)")

    def afficher_livres(self):
        for i in self.livres:
            print(i)
        return

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
