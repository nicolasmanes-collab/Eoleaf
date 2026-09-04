# Roadmap technique Eoleaf — septembre à novembre 2026

Établie le 04/09/2026 par SEO Monkey. 21 tickets, 71 heures estimées.

## Où vivent les livrables

Les 19 Sheets de travail sont sur le Drive client, dans
`2 - Technique / 5 - Mois 5 (septembre)`. Un par ticket, à la structure des
extractions existantes : libellés de colonnes en ligne 1, bandeau
« Important ⚠️ » en ligne 2, données ensuite.

| Ticket | Sheet de travail |
|---|---|
| Re-crawl de contrôle indexation | Controle indexation Eoleaf |
| Canonique des fiches produit | Canonique fiches produit Eoleaf |
| Page contact et formulaire SAV | Contact et SAV 12 langues Eoleaf |
| 36 pages EN sous le préfixe /fr | Pages EN sous prefixe fr Eoleaf |
| Cannibalisation : 14 clusters FR | Cannibalisation clusters FR Eoleaf |
| 33 liens internes rompus | *liens internes rompus* (fichier existant, on écrit dedans) |
| H1 manquants sur 5 gabarits | H1 manquants Eoleaf |
| Images des gabarits d'achat | Images a corriger Eoleaf |
| Hreflang sur 12 langues | Hreflang 12 langues Eoleaf |
| Redirections des anciennes URL AEROPRO | Redirections AEROPRO Eoleaf |
| Doublons de pages de service | Doublons pages service Eoleaf |
| Vitesse par gabarit | Vitesse par gabarit Eoleaf |
| JSON-LD par gabarit | JSON-LD par gabarit Eoleaf |
| Sitemap contre pages réelles | Sitemap contre pages Eoleaf |
| Robots.txt et URL à paramètres | Robots et parametres Eoleaf |
| Liens sortants rompus | Liens sortants a remplacer Eoleaf |
| Plan de maillage interne | Plan de maillage Eoleaf |
| Profondeur et pages orphelines | Profondeur et orphelines Eoleaf |
| Couche géo : 4 pages villes | Pages geo villes Eoleaf |
| 13 comparatifs concurrents | Comparatifs concurrents Eoleaf |
| Maquettes SXO par étage | pages HTML, pas de Sheet |

## Ce que contient ce dossier

| Fichier | À quoi il sert |
|---|---|
| `2026-09-04-roadmap-technique-septembre-eoleaf.xlsx` | Le classeur. ROADMAP TECHNIQUE (septembre), BACKLOG OCT-NOV, CONSTATS CHIFFRES. |
| `a-coller-onglet-technique.tsv` | Les 21 lignes au format exact de l'onglet technique du Sheet de pilotage. La colonne Livrable porte une formule `LIEN_HYPERTEXTE` : si le Sheet est en locale anglaise, remplacer par `HYPERLINK` et le point-virgule par une virgule. |
| `roadmap-technique-eoleaf-complet.tsv` | Les 21 tickets au format du modèle, colonnes DETAILS, REPARTITION, HEURE DE TRAVAIL, LIVRABLE et SEVERITE comprises. |
| `roadmap-septembre.html` | La roadmap en page lisible, publiée en artifact. |
| `donnees_roadmap.py` | Source de vérité des tickets et des constats. On modifie ici, puis on régénère. |
| `contenu_sheets_1..4.py` | Contenu des 19 Sheets de travail. |
| `construire_roadmap.py` | Régénère le classeur et les deux TSV. |
| `construire_page.py` | Régénère la page HTML depuis les mêmes données. |
| `vers_csv.py` | Sort les 19 CSV depuis `contenu_sheets_*.py`, pour reverser sur le Drive. |
| `sheets/*.csv` | Les 19 livrables en local, tels qu'ils ont été téléversés. |

Tout se régénère par :

```bash
python3 construire_roadmap.py && python3 construire_page.py && python3 vers_csv.py
```

## Le point qui change la lecture du dossier

L'extraction d'indexation du 20/05 classe environ 250 URL en « erreur client »,
dont des pages que l'onglet sémantique donne en position 4 à 8. Une page morte
ne se classe pas. La cause probable est un rejet Shopify sous la charge du
crawl. Tant que ce n'est pas tranché, les 39 « pages indexées », la liste des
orphelines et le décompte des erreurs sont à refaire : c'est le premier ticket
de septembre, et il conditionne les sept autres.

## Trois réserves à lever

1. **Le volume d'heures du contrat** n'est pas dans le dossier. Septembre est
   calé sur 8 lignes (28 h estimées). Si le volume contractuel est inférieur,
   les tickets 07 (H1) et 08 (images) basculent en octobre : ce sont les deux
   dont le report coûte le moins.
2. **eoleaf.com est injoignable** depuis l'environnement de travail (politique
   réseau de la session). Aucun constat n'a pu être revérifié en direct ; le
   plus récent date du 24/08.
3. **Pas d'accès Search Console.** Le premier ticket en dépend, ainsi que la
   priorisation par clics 90 jours et le relevé des pages orphelines.
