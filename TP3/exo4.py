import random
from exceptions import LettreDejaSoumise

def choisir_mot(fichier="dic.txt"):
    with open(fichier, "r", encoding="utf-8") as f:
        mots = [ligne.strip() for ligne in f if ligne.strip()]
    return random.choice(mots).upper()

def jouer_pendu():
    mot_a_trouver = choisir_mot()
    vies = 6
    lettres_proposees = set()

    premiere_lettre = mot_a_trouver[0]
    lettres_trouvees = {premiere_lettre}  
    print("=== JEU DU PENDU ===")

    while vies > 0:
        affichage = [lettre if lettre in lettres_trouvees else "_" for lettre in mot_a_trouver]
        print("\nMot à deviner :", " ".join(affichage))
        print(f"Vies restantes : {vies}")

        if "_" not in affichage:
            print("\nBravo, vous avez gagné ! ")
            return

        proposition = input("Proposez une lettre : ").strip().upper()

        if not proposition.isalpha() or len(proposition) != 1:
            print("Veuillez entrer une seule lettre valide.")
            continue

        try:
            if proposition in lettres_proposees:
                raise LettreDejaSoumise(f"La lettre '{proposition}' a déjà été proposée !")
            
            lettres_proposees.add(proposition)

            if proposition in mot_a_trouver:
                lettres_trouvees.add(proposition)
                print(f"Bonne réponse ! La lettre '{proposition}' est dans le mot.")
            else:
                vies -= 1
                print(f"La lettre '{proposition}' n'est pas dans le mot.")

        except LettreDejaSoumise as e:
            print(f"Erreur : {e}")

    print(f"\nVous avez perdu ! Le mot était : {mot_a_trouver}")

if __name__ == "__main__":
    jouer_pendu()