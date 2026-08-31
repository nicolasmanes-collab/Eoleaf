# -*- coding: utf-8 -*-
"""Construit le classeur de roadmap technique + les TSV prêts à coller.

Charte appliquée (décrite dans le skill audit-technique, faute d'accès au
standard.json partagé) : Comfortaa 10, centrage horizontal et vertical,
bandeau pédagogique fusionné en ligne 1 sur fond #1A73E8 texte blanc,
libellés de colonnes en ligne 2, les deux figés, feuilles en MAJUSCULES,
aucune ligne ni colonne vide.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from donnees_roadmap import SEPTEMBRE, BACKLOG, CONSTATS

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BLEU = "1A73E8"
POLICE = "Comfortaa"
BORD = Border(*[Side(style="thin", color="D9D9D9")] * 4)


def _bandeau(ws, ncol, quoi, pourquoi, comment):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncol)
    c = ws.cell(row=1, column=1)
    c.value = f"QUOI · {quoi}    POURQUOI · {pourquoi}    COMMENT · {comment}"
    c.font = Font(name=POLICE, size=10, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor=BLEU)
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 46


def _entetes(ws, cols):
    for i, nom in enumerate(cols, start=1):
        c = ws.cell(row=2, column=i, value=nom)
        c.font = Font(name=POLICE, size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=BLEU)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORD
    ws.row_dimensions[2].height = 30
    ws.freeze_panes = "A3"


def _corps(ws, lignes, largeurs, col_annexe=None):
    for r, ligne in enumerate(lignes, start=3):
        for i, val in enumerate(ligne, start=1):
            c = ws.cell(row=r, column=i)
            if col_annexe and i == col_annexe and val:
                libelle, _, url = str(val).partition("|")
                c.value = libelle
                if url:
                    c.hyperlink = url
                    c.font = Font(name=POLICE, size=10, color="1155CC", underline="single")
                else:
                    c.font = Font(name=POLICE, size=10)
            else:
                c.value = val
                c.font = Font(name=POLICE, size=10)
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            c.border = BORD
        ws.row_dimensions[r].height = 96
    for i, l in enumerate(largeurs, start=1):
        ws.column_dimensions[get_column_letter(i)].width = l


COLS_ROADMAP = ["MOIS", "DATE DE LIVRAISON", "TICKET", "DETAILS",
                "REPARTITION", "HEURE DE TRAVAIL", "STATUT", "ANNEXE", "INTERVENANT"]
LARG_ROADMAP = [13, 16, 34, 96, 20, 12, 12, 22, 16]


def feuille_roadmap(wb, titre, lignes, quoi, pourquoi, comment):
    ws = wb.create_sheet(titre)
    _bandeau(ws, len(COLS_ROADMAP), quoi, pourquoi, comment)
    _entetes(ws, COLS_ROADMAP)
    _corps(ws, lignes, LARG_ROADMAP, col_annexe=8)
    # ligne de total des heures, hors zone de données
    r = len(lignes) + 3
    ws.cell(row=r, column=5, value="TOTAL HEURES").font = Font(name=POLICE, size=10, bold=True)
    tot = ws.cell(row=r, column=6, value=sum(l[5] for l in lignes))
    tot.font = Font(name=POLICE, size=10, bold=True)
    for col in (5, 6):
        ws.cell(row=r, column=col).alignment = Alignment(horizontal="center", vertical="center")
    return ws


def feuille_constats(wb):
    ws = wb.create_sheet("CONSTATS CHIFFRES")
    cols = ["VOLET", "CE QUI EST MESURE", "VALEUR RELEVEE", "CE QUE CELA IMPLIQUE"]
    _bandeau(ws, len(cols),
             "les chiffres qui fondent chaque ticket de la roadmap",
             "un ticket sans chiffre daté ne se compare pas d'un mois sur l'autre",
             "chaque valeur vient d'une extraction du Drive, la date de relevé est indiquée dans la ligne")
    _entetes(ws, cols)
    for r, ligne in enumerate(CONSTATS, start=3):
        for i, val in enumerate(ligne, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = Font(name=POLICE, size=10)
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            c.border = BORD
        ws.row_dimensions[r].height = 46
    for i, l in enumerate([16, 44, 22, 76], start=1):
        ws.column_dimensions[get_column_letter(i)].width = l
    return ws


def main():
    out = os.path.dirname(os.path.abspath(__file__))
    wb = Workbook()
    wb.remove(wb.active)

    feuille_roadmap(
        wb, "ROADMAP TECHNIQUE", SEPTEMBRE,
        "les six chantiers techniques de septembre 2026, dans leur ordre d'exécution",
        "l'ordre des lignes est l'ordre d'impact sur le chiffre : ce qui empêche une page de vendre passe "
        "avant ce qui la freine, et le budget de crawl vient après",
        "chaque ligne porte son critère d'acceptation dans DETAILS et son annexe cliquable ; on ne clôt "
        "une ligne que lorsque le critère est vérifié")

    feuille_roadmap(
        wb, "BACKLOG OCTOBRE-NOVEMBRE", BACKLOG,
        "les chantiers identifiés mais non tenables dans le volume de septembre",
        "ils sont datés pour ne pas se perdre : hreflang, vitesse, JSON-LD et maillage n'ont jamais été "
        "ouverts depuis le début de l'accompagnement",
        "à confirmer au volume d'heures du contrat avant bascule dans l'onglet du mois")

    feuille_constats(wb)

    chemin = os.path.join(out, "2026-08-28-roadmap-technique-septembre-eoleaf.xlsx")
    wb.save(chemin)
    print("classeur :", chemin)

    # TSV au format de l'onglet technique du Sheet client
    tsv = os.path.join(out, "a-coller-onglet-technique-septembre.tsv")
    with open(tsv, "w", encoding="utf-8") as f:
        f.write("Mois\tSemaine\tBrief technique\tLivrable\tIntervenant\tStatut\n")
        for l in SEPTEMBRE:
            livrable = l[7].partition("|")[0] if l[7] else ""
            f.write(f"{l[0]}\t{l[1]}\t{l[2]}\t{livrable}\t{l[8]}\tA faire\n")
    print("tsv sheet :", tsv)

    # TSV complet au format du modèle de roadmap technique
    tsv2 = os.path.join(out, "roadmap-technique-eoleaf-complet.tsv")
    with open(tsv2, "w", encoding="utf-8") as f:
        f.write("\t".join(COLS_ROADMAP) + "\n")
        for l in SEPTEMBRE + BACKLOG:
            f.write("\t".join(str(x).replace("\t", " ") for x in l) + "\n")
    print("tsv complet :", tsv2)


if __name__ == "__main__":
    main()
