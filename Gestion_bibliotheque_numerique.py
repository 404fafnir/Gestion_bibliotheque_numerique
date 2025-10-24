# Système de Gestion Bibliothèque Numérique

class Livre:
    def __init__(self, identifiant, titre, auteur, categorie, nbexemplaires, status):
        self.identifiant = identifiant
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.nbexemplaires = nbexemplaires
        self.status = status
    pass

class Utilisateur:
    def __init__(self, identifiant, nom, email):
        self.identifiant = identifiant
        self.nom = nom
        self.email = email
    pass

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
    pass

