import random

# --- Paramètres généraux -----------------------------------------------------
TAILLE_CODE   = 4
ESSAIS_MAX    = 10
PALETTE       = ["Vert", "Noir", "Rouge", "Jaune", "Orange", "Marron"]

# --- Génération du code secret ----------------------------------------------
def generer_code_secret():
    """Crée aléatoirement la combinaison que le joueur doit deviner."""
    return [random.choice(PALETTE) for _ in range(TAILLE_CODE)]

# --- Saisie et validation de la proposition ---------------------------------
def saisir_proposition():
    """Invite le joueur à entrer sa combinaison et vérifie la saisie."""
    while True:
        saisie = input(
            f"Entrez {TAILLE_CODE} couleurs (séparées par un espace) parmi "
            f"{', '.join(PALETTE)} : "
        ).strip()
        tentative = saisie.split()

        if len(tentative) != TAILLE_CODE:
            print(f"⚠️  Il faut fournir exactement {TAILLE_CODE} couleurs.")
            continue
        if any(c not in PALETTE for c in tentative):
            print("⚠️  Utilisez uniquement les couleurs proposées.")
            continue

        return tentative

# --- Évaluation de la tentative ---------------------------------------------
def evaluer_tentative(secret, tentative):
    """Retourne le nombre de pions bien placés et mal placés."""
    bien_places = sum(s == t for s, t in zip(secret, tentative))

    # On ne garde que les positions qui ne sont pas déjà correctes
    reste_secret    = [s for s, t in zip(secret, tentative) if s != t]
    reste_tentative = [t for s, t in zip(secret, tentative) if s != t]

    mal_places = 0
    for couleur in reste_tentative:
        if couleur in reste_secret:
            mal_places += 1
            reste_secret.remove(couleur)  # évite de compter deux fois la même couleur

    return bien_places, mal_places

# --- Boucle principale du jeu -----------------------------------------------
def lancer_mastermind():
    print("🎯 Bienvenue dans cette version revisitée du Mastermind !")
    code_secret      = generer_code_secret()
    essais_restants  = ESSAIS_MAX

    while essais_restants:
        print(f"\nIl vous reste {essais_restants} essai(s).")
        tentative = saisir_proposition()
        bien, mal = evaluer_tentative(code_secret, tentative)

        print(f"Résultat → {bien} bien placé(s), {mal} mal placé(s).")

        if bien == TAILLE_CODE:
            print("🏆 Bravo ! Vous avez découvert la combinaison secrète !")
            break

        essais_restants -= 1
    else:
        print("\n💥 Tous les essais sont épuisés.")
        print("La combinaison secrète était :", " ".join(code_secret))

# --- Exécution directe du script --------------------------------------------
if __name__ == "__main__":
    lancer_mastermind()
