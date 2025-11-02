# Système de Gestion Bibliothèque Numérique
from datetime import datetime

class Livre:

    _id = 1 # id de base

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
        super().__init__(identifiant, nom, email)
        self.usertype = "lecteur"
    pass

class Bibliothecaire(Utilisateur):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email)
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

    def ajouter_livres(self, livre, utilisateur):
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

    def rechercher_livres(self, condition):
        attibut, valeur= condition
        compteur = 0
        for i in self.livres:
            if not hasattr(i, attibut):
                print("/!\ Impossible de chercher un livre par",attibut)
                return
            if getattr(i, attibut) == valeur:
                print(i)
                compteur += 1
        print(f"Recherche finie: {compteur} livre(s) trouver")
        pass

    def ajouter_utilisateur(self, utilisateur):
        if utilisateur.identifiant in self.utilisateurs:
            print(f"/!\ Un utilisateur avec l'ID {utilisateur.identifiant} existe déjà.")
            return
        self.utilisateurs[utilisateur.identifiant] = utilisateur
        print(f"Utilisateur ajouté : {utilisateur.nom} ({utilisateur.usertype})")

    def supprimer_utilisateur(self, utilisateur):
        if utilisateur.identifiant not in self.utilisateurs:
            print("/!\ Utilisateur introuvable.")
            return
        del self.utilisateurs[utilisateur.identifiant]
        print("Utilisateur supprimé !")

    def emprunter_livre(self, livre, utilisateur):
        if not isinstance(utilisateur, Lecteur):
            print("/!\ Seuls les lecteurs peuvent emprunter des livres.")
            return
        
        if livre not in self.livres:
            print("/!\ Livre introuvable dans la bibliothèque.")
            return

        if livre.nbexemplaires <= 0:
            print(f"/!\ Le livre '{livre.titre}' n'est pas disponible.")
            return
        
        livre.nbexemplaires -= 1
        livre.status = "disponible" if livre.nbexemplaires > 0 else "emprunté"

        if utilisateur.identifiant not in self.emprunts:
            self.emprunts[utilisateur.identifiant] = []
        self.emprunts[utilisateur.identifiant].append({
            "livre": livre,
            "date_emprunt": datetime.now()
        })

        print(f"{utilisateur.nom} a emprunté '{livre.titre}' le {datetime.now().strftime('%d/%m/%Y')}")
        return

    def rendre_livres(self, livre, utilisateur):
        if not isinstance(utilisateur, Lecteur):
            print("/!\ Seuls les lecteurs peuvent rendre des livres.")
            return
        
        if utilisateur.identifiant not in self.emprunts:
            print("/!\ Le lecteur ne pas de livre emprunté.")
            return

        for i in self.emprunts[utilisateur.identifiant]:
            if livre == i["livre"]:
                livre.nbexemplaires += 1
                livre.status = "disponible" if livre.nbexemplaires > 0 else "emprunté"
                self.emprunts[utilisateur.identifiant].remove(i)
                print(f"{utilisateur.nom} a rendu '{livre.titre}' le {datetime.now().strftime('%d/%m/%Y')}")
                return

        print("/!\ Livre introuvable dans les emprunts du lecteur.")
        return
                
    def statistiques_livres(self):
        total_livres = len(self.livres)
        total_lecteurs=0
        total_emprunts=0
        for u in self.utilisateurs.values():
            if isinstance(u, Lecteur):
                total_lecteurs+=1
        for e in self.emprunts:
            total_emprunts+=1
        print("=== Statistiques de la bibliothèque ===")
        print(f"Nombre total de livres : {total_livres}")
        print(f"Nombre total de lecteurs : {total_lecteurs}")
        print(f"Nombre total de livres empruntés : {total_emprunts}")

biblio = Bibliotheque()
admin = Bibliothecaire(1, "admin", "admin@test.com")
exempleLecteur = Lecteur(2, "Jean Dupont", "jean.dupont@test.com")
exempleLivre = Livre("Les Contemplations", "Victor Hugo", "Poèmes", 10)


while True:
    print("\n--- Menu Principal ---")
    print("1. Gérer les livres")
    print("2. Gérer les utilisateurs")
    print("3. Gérer les emprunts")
    print("4. Quitter")
    choix = int(input(""))
    match choix:
        case 1:
            print("\n--- Gérer les livres ---")
            print("1. Ajouter livre")
            print("2. Modifier livre")
            print("3. Supprimer livre")
            print("4. Afficher liste complète des livres")
            print("5. Rechercher un livre")
            print("6. Revenir au menu principal")
            sousChoix = int(input(""))
            match sousChoix:
                case 1:
                    titre = input("Entrer le titre du livre :")
                    auteur = input("Entrer l'auteur du livre :")
                    categorie = input("Entrer la catégorie principale du livre :")
                    nombre = int(input("Entrer le nombre d'exemplaire du livre :"))
                    nouveauLivre = Livre(titre, auteur, categorie, nombre)
                    biblio.ajouter_livres(nouveauLivre, admin)
                    pass
                case 2:
                    attribut = input("Que voulez vous modifiez :")
                    valeur = input("Entrer la modification :")
                    biblio.modifier_livres(exempleLivre, (attribut, valeur), admin)
                    pass
                case 3:
                    biblio.supprimer_livres(exempleLivre, exempleLecteur)
                    pass
                case 4:
                    print("\nVoici la liste complète des livres :")
                    biblio.afficher_livres()
                    pass
                case 5:
                    attribut = input("Entrer selon quel critère vous voulez chercher le livre :")
                    valeur = input(f"Entrez {attribut} du livre que vous chercher :")
                    biblio.rechercher_livres((attribut, valeur))
                    pass
                case 6:
                    pass
                case _:
                    print("Choix invalide !")
                    pass
        case 2:
            print("\n--- Gérer les utilisateurs ---")
            print("1. Ajouter un utilisateur")
            print("2. Supprimer un utilisateur")
            print("3. Revenir au menu principal")
            sousChoix = int(input(""))
            match sousChoix:
                case 1:
                    id = int(input("Entrer l'id de l'utilisateur :"))
                    nom = input("Entrer le nom de l'utilisateur :")
                    mail = input("Entrer le mail de l'utilisateur :")
                    typeUtilisateur = int(input("L'utilisateur est un lecteur (si oui 1) :"))
                    if typeUtilisateur == 1:
                        nouvelUtilisateur = Lecteur(id, nom, mail)
                    else:
                        nouvelUtilisateur = Bibliothecaire(id, nom, mail)
                    biblio.ajouter_utilisateur(nouvelUtilisateur)
                    pass
                case 2:
                    mail = input("Mail de l'utilisateur à supprimer :")
                    for u in biblio.utilisateurs:
                        if u.email == mail:
                            biblio.supprimer_utilisateur(u)
                            pass
                    print("/!\ Utilisateur introuvable !")
                    pass
                case 3:
                    pass
                case _:
                    print("Choix invalide !")
                    pass
        case 3:
            print("\n--- Gérer les emprunts ---")
            print("1. Emprunt")
            print("2. Retour")
            print("3. Revenir au menu principal")
            sousChoix = int(input(""))
            match sousChoix:
                case 1:
                    mail = input("Entrer le mail du lecteur qui veut emprunter :")
                    utilisateur = None
                    livre = None
                    for u in biblio.utilisateurs:
                        if u.email == mail:
                            utilisateur = u
                    titre = input("Entrer le titre du livre à emprunter :")
                    for l in biblio.livres:
                        if l.titre == titre:
                            livre = l
                    biblio.emprunter_livre(livre, utilisateur)
                    pass
                case 2:
                    mail = input("Entrer le mail du lecteur qui rend le livre :")
                    utilisateur = None
                    livre = None
                    for u in biblio.utilisateurs:
                        if u.email == mail:
                            utilisateur = u
                    titre = input("Entrer le titre du livre rendu :")
                    for l in biblio.livres:
                        if l.titre == titre:
                            livre = l
                    biblio.rendre_livres(livre, utilisateur)
                    pass
                case 3:
                    pass
                case _:
                    print("Choix invalide !")
                    pass
        case 4:
            break
        case _:
            print("Choix invalide !")
            pass
