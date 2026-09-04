# Roadmap technique Eoleaf — septembre à novembre 2026

Établie le 04/09/2026 par SEO Monkey. 21 tickets, 71 heures estimées.

## Où c'est écrit

Les 21 tickets sont dans le Sheet de pilotage, onglet `Technique` : septembre
en L24-31, octobre en L32-37, novembre en L38-44. La colonne Mois, fusionnée
par bloc, n'a pas été touchée ; seules les colonnes B à F ont été écrites,
après insertion de 4, 1 et 2 lignes pour faire la place.

L'onglet `Annexes` porte en L15 un lien vers le dossier des 19 livrables.

Deux pièges rencontrés sur ce document, à ne pas refaire :

1. **L'API Sheets ne traduit pas les noms de fonctions.** Ce document est en
   locale française : une formule doit être envoyée en
   `LIEN_HYPERTEXTE(...;...)`. Envoyée en `HYPERLINK(...,...)`, elle rend
   `#ERROR!`.
2. **Ne jamais écrire sur un numéro de ligne mémorisé.** Le 04/09, une ligne
   insérée dans le Sheet entre deux de mes écritures a décalé tout le bloc, et
   trois titres ont été écrasés sur les mauvaises lignes. Correction : localiser
   la ligne par le libellé de sa colonne Livrable, qui est stable, puis écrire.
   C'est ce que fait la réparation, et c'est la méthode à garder.

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
| `a-coller-onglet-technique.tsv` | Les 21 lignes au format exact de l'onglet technique. Devenu un filet de sécurité : les 21 lignes ont été écrites directement dans le Sheet de pilotage le 04/09/2026 (onglet `Technique`, L24 à L44). La colonne Livrable porte `LIEN_HYPERTEXTE` avec un point-virgule, syntaxe confirmée pour ce document — il est en locale française. |
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

## Le contrôle Search Console du 04/09/2026

Fait via l'API sur la propriété `sc-domain:eoleaf.com`. Le détail est dans le
Sheet `Controle indexation Eoleaf`, onglet `CONTROLE INDEXATION`.

Le crawl du 20/05 était faux. Il déclarait 39 pages indexées et environ 250 URL
en erreur client ; la Search Console compte 2 994 pages portant au moins une
impression sur 90 jours, 28 889 clics et 3 765 160 impressions, position moyenne
12,5. Les 10 URL témoin sont toutes « Envoyée et indexée », robots autorisé,
page récupérée, dernier passage de Google entre le 22/08 et le 04/09.

Trois tickets en sortent modifiés :

- **Page contact** : les pages contact FR, EN et DE sont saines, la FR est en
  position 2,2 avec 477 impressions. Seule `/fr/pages/formulaire-apres-vente`
  est morte. Ticket ramené de 2 h à 30 min et confié à Eoleaf.
- **JSON-LD** : la fiche produit porte déjà Product, Offer et AggregateRating,
  verdict PASS. Ticket ramené de 4 h à 3 h, périmètre réduit à l'accueil, la
  catégorie, les pages métier et la FAQ.
- **Sitemap** : 6 des 10 URL témoin ne sont pas déclarées au sitemap, dont
  l'accueil FR et la fiche AltaPur 700. Le ticket gagne en importance.

Deux constats nouveaux, à trancher avec Eoleaf :

- Le français ne porte que 21 % des clics. Les onze autres langues en font 79 %,
  et la page la plus cliquée du site est allemande
  (`/de/pages/kauf-eines-luftreinigers-fur-cannabis`, 928 clics).
- Les positions de l'onglet sémantique sont à re-sourcer : « purificateur d'air
  professionnel » y figure en position 4, la Search Console la donne en 37.

### Ticket 01 : intégré le 04/09/2026

L'écart est expliqué ligne à ligne, ce qui était le critère d'acceptation :

- 206 des 305 URL déclarées non indexées portent en réalité des impressions,
  soit 5 748 clics et 562 617 impressions cumulés. Faux positifs.
- Les 99 restantes ont été inspectées une à une : 68 inconnues de Google (des
  formes d'URL parasites), 21 explorées non indexées, 6 déjà redirigées,
  2 indexées sans impression, 2 canoniques ou noindex volontaires.
- Chaque ligne est rattachée au ticket qui la traite. 8 URL ne relèvent d'aucun
  ticket et attendent un arbitrage, dont 3 unités d'achat FR explorées et non
  indexées.

Livrable produit : `Extraction Indexation 09-2026 Eoleaf`, trois onglets
(PAGES INDEXEES 2 994 lignes, ECART CRAWL 05-2026 305 lignes, A ARBITRER 8
lignes). L'ancienne extraction est renommée
`z - Extraction Indexation Eoleaf 05-2026 (ancien, statuts errones)`.

Deux tickets sont revus par ce contrôle :

- **36 pages EN sous /fr** : 28 des 33 URL sans impression sont inconnues de
  Google. Elles ne cannibalisent rien. Le ticket passe de bloquant à budget de
  crawl, de 4 h à 2 h, et repasse à Eoleaf.
- **Robots.txt** : `/fr/search` ressort « Envoyée et indexée ». Confirmé.

Ce qui ne relève pas de ce ticket : profondeur de page, pages orphelines et
liens internes. La Search Console ne les fournit pas, il faut un crawl, et ces
trois volets appartiennent au ticket « Profondeur et pages orphelines » daté en
novembre. Le crawl ne peut pas être lancé depuis l'environnement de travail,
eoleaf.com y étant bloqué par la politique réseau.

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
