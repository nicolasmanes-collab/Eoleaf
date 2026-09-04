# -*- coding: utf-8 -*-
"""Sort un CSV par ticket : ligne 1 = libelles de colonnes, ligne 2 = bandeau
pedagogique, donnees ensuite. Meme structure que les extractions existantes."""
import os, sys, csv
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
SORTIE = os.path.join(ICI, "sheets")

def charger():
    f = {}
    for m in ("contenu_sheets_1", "contenu_sheets_2", "contenu_sheets_3", "contenu_sheets_4"):
        f.update(__import__(m).FICHIERS)
    return f

if __name__ == "__main__":
    os.makedirs(SORTIE, exist_ok=True)
    for nom, (bandeau, entetes, lignes) in charger().items():
        chemin = os.path.join(SORTIE, nom + ".csv")
        with open(chemin, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
            w.writerow(entetes)
            w.writerow([bandeau] + [""] * (len(entetes) - 1))
            for l in lignes:
                w.writerow(list(l) + [""] * (len(entetes) - len(l)))
        print(f"{os.path.getsize(chemin):>6} o  {nom}.csv")
