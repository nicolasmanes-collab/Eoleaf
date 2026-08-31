# Roadmap technique Eoleaf — septembre 2026

Établie le 28/08/2026 par SEO Monkey.

## Ce que contient ce dossier

| Fichier | À quoi il sert |
|---|---|
| `2026-08-28-roadmap-technique-septembre-eoleaf.xlsx` | Le livrable. Trois feuilles : ROADMAP TECHNIQUE (septembre), BACKLOG OCTOBRE-NOVEMBRE, CONSTATS CHIFFRES. |
| `a-coller-onglet-technique-septembre.tsv` | Les six lignes de septembre au format exact de l'onglet technique du Sheet de pilotage (Mois, Semaine, Brief technique, Livrable, Intervenant, Statut). À coller dans les lignes septembre déjà en place. |
| `roadmap-technique-eoleaf-complet.tsv` | Septembre + backlog au format du modèle de roadmap technique, colonnes DETAILS, REPARTITION, HEURE DE TRAVAIL et ANNEXE comprises. |
| `roadmap-septembre.html` | La même roadmap en page lisible, publiée en artifact. |
| `donnees_roadmap.py` | La source de vérité des tickets et des constats. On modifie ici, puis on régénère. |
| `construire_roadmap.py` | Régénère le classeur et les deux TSV : `python3 construire_roadmap.py`. |

## Sources des constats

Aucun chiffre n'est estimé, tous viennent du Drive du client :

- Extraction Indexation Eoleaf — crawl du 20/05/2026
- Extraction Balisage Eoleaf — modifiée le 17/07/2026
- Extraction Images Eoleaf — modifiée le 20/05/2026
- liens internes rompus — modifiée le 30/06/2026
- liens sortants rompus (feuille sans titre, Mois 2) — 22/07/2026
- 23 pages ont plus d'un titre h1 — 24/08/2026
- Onglet sémantique de la roadmap client, pour les positions

## Trois réserves à lever

1. **Le volume d'heures du contrat** n'est pas dans le dossier. Septembre est calé sur six lignes (19 h estimées), à l'image de la cadence de juin à août. Les heures sont des estimations d'effort, pas des engagements.
2. **eoleaf.com est injoignable** depuis l'environnement de travail (politique réseau de la session). Aucun constat n'a pu être revérifié en direct sur le site ; le plus récent date du 24/08.
3. **Pas d'accès Search Console.** Le premier ticket en dépend, ainsi que la priorisation par clics 90 jours et le relevé des pages orphelines.

## Le point qui change la lecture du dossier

L'extraction d'indexation du 20/05 classe environ 250 URL en « erreur client », dont des pages que
l'onglet sémantique donne en position 4 à 8 sur leur requête cible. Une page morte ne se classe pas.
La cause probable est un rejet Shopify sous la charge du crawl. Tant que ce n'est pas tranché, les
39 « pages indexées » relevées, la liste des orphelines et le décompte des erreurs sont à refaire :
c'est le premier ticket de septembre.
