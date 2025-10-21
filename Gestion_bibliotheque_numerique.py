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
    pass

class Lecteur(Utilisateur):
    pass

class Bibliothecaire(Utilisateur):
    pass

class Bibliotheque:
    pass

# Système de Gestion Bibliothèque Numérique
