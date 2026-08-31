# -*- coding: utf-8 -*-
"""Roadmap technique Eoleaf — septembre 2026.

Sources des constats : les 5 extractions du Drive (crawl du 20/05/2026),
le fichier H1 du 24/08/2026, l'onglet sémantique de la roadmap client.
Ordre des tickets = ordre d'impact business, jamais la sévérité du crawler.
"""

DRIVE = "https://docs.google.com/spreadsheets/d"
ANNEXES = {
    "indexation": f"{DRIVE}/1KL4Cn_JpDwckWyS3j9cj1HPCcNIvh23OTcCrdifr6RA/edit",
    "balisage":   f"{DRIVE}/1VlQeLHkm_5ajbGMLOKo9f3Xw6vh7y0s6VU-Uyu33qBQ/edit",
    "images":     f"{DRIVE}/1AuHyCxJ8b52Goa6K0nUx1V3Rzwxu24_TxS49s8xH_NY/edit",
    "liens_int":  f"{DRIVE}/1c7_Bu5rdkz9TmV9wHW_I_RJsEEtkrmIMETtDe1oxpRM/edit",
    "err404":     f"{DRIVE}/1fvvO2A_IEKlnqJSQITqIW5ab6-PCf_Cf70mv4mZHzzc/edit",
    "liens_ext":  f"{DRIVE}/1bYcZfpAVMao0PlW-mrWlyl0Pvpe5NfAQgkAJms_OnTs/edit",
    "h1":         f"{DRIVE}/1N0WSvUwQpSEkti1DHOrvsdAfCrKdTPgjOLw7nIl_4HQ/edit",
}

# MOIS, DATE, TICKET, DETAILS, REPARTITION, HEURES, STATUT, ANNEXE(libellé|url), INTERVENANT
SEPTEMBRE = [
 ("SEPTEMBRE", "01/09/2026",
  "Re-crawl de contrôle et réconciliation de l'indexation",
  "Relancer le crawl du site en 1 thread et 1 URL par seconde, user-agent Googlebot Smartphone, "
  "puis confronter chaque statut à l'outil d'inspection d'URL de la Search Console sur 10 URL témoin. "
  "Motif : l'extraction du 20/05/2026 classe environ 250 URL en erreur client, dont des pages qui se "
  "positionnent de la 4e à la 8e place dans l'onglet sémantique (qualité médicale en position 7, "
  "ioniseurs en position 8). Les deux ne peuvent pas être vrais en même temps : la cause probable est un "
  "rejet Shopify sous la charge du crawl, pas une page morte. Tant que ce point n'est pas tranché, aucun "
  "chiffre d'indexation du dossier n'est exploitable. "
  "Critère d'acceptation : nouvel export d'indexation daté, écart entre statut de crawl et statut Search "
  "Console expliqué ligne à ligne, ancien onglet renommé « z · Indexation 05-2026 (ancien) ».",
  "SEO MONKEY", 3.0, "A FAIRE", f"Extraction Indexation|{ANNEXES['indexation']}", "Nicolas"),

 ("SEPTEMBRE", "01/09/2026",
  "Trancher l'URL canonique des fiches produit",
  "Choisir la forme d'URL indexable unique par produit entre /fr/products/<produit> et "
  "/fr/collections/<collection>/products/<produit>, poser la canonique autoréférente sur la forme retenue, "
  "puis aligner les liens internes dessus. "
  "Motif bloquant : les pages relevées comme indexées au crawl sont en /fr/products/, alors que l'onglet "
  "« Tableau de balisage » prépare les nouveaux titles et descriptions sur les URL en "
  "/fr/collections/purificateurs-air/products/. En intégrant en l'état, le balisage se pose sur des URL "
  "qui ne sont pas celles qui rankent, et le travail est perdu. "
  "Critère d'acceptation : une seule URL par produit répond 200 sans redirection, la canonique pointe vers "
  "elle-même, et l'onglet « Tableau de balisage » est corrigé avant toute intégration.",
  "SEO MONKEY", 2.0, "A FAIRE", f"Extraction Balisage|{ANNEXES['balisage']}", "Nicolas"),

 ("SEPTEMBRE", "08/09/2026",
  "Réparer la page contact et le formulaire SAV",
  "Diagnostiquer puis rendre accessibles /fr/pages/contact (erreur client au crawl) et "
  "/fr/pages/formulaire-apres-vente (404, appelé depuis /fr/pages/faqs), et vérifier les 12 versions "
  "linguistiques du même gabarit. Une page contact injoignable sur un site qui vend en B2B coûte "
  "directement des demandes entrantes : ce ticket passe avant tout travail d'optimisation. "
  "Critère d'acceptation : les 12 URL contact et les 12 URL SAV répondent 200, et le lien depuis la FAQ "
  "pointe vers l'URL vivante, sans redirection intermédiaire.",
  "SEO MONKEY + EOLEAF", 2.0, "A FAIRE", f"Extraction Indexation|{ANNEXES['indexation']}",
  "Nicolas / Eoleaf"),

 ("SEPTEMBRE", "15/09/2026",
  "Solder les 33 liens internes rompus encore ouverts",
  "Corriger les 33 lignes encore marquées « Réglé ? = FALSE » dans le fichier des liens internes rompus, "
  "alors que le ticket est déclaré intégré au 14/08/2026 dans la roadmap. Deux cibles mortes reviennent "
  "sur les 12 langues : /collections/air-purifiers/products/altapur-700-air-purifier-en et "
  "/collections/air-purifiers/products/aeropro-150-airpurifier. La colonne « Newlink » du fichier porte "
  "déjà la cible de remplacement pour chaque ligne, il n'y a pas de mapping à refaire. "
  "Critère d'acceptation : zéro ligne FALSE dans le fichier, et les 38 liens répondent 200 en un seul saut.",
  "EOLEAF", 2.0, "A FAIRE", f"Liens internes rompus|{ANNEXES['liens_int']}", "Eoleaf"),

 ("SEPTEMBRE", "22/09/2026",
  "Poser les H1 manquants sur 5 gabarits",
  "Rédiger et intégrer un H1 unique sur les gabarits qui en sont dépourvus : collection "
  "(/fr/collections/filtres-et-accessoires, /fr/collections/all), page institutionnelle "
  "(/fr/pages/a-propos-de-nous, /fr/pages/certifications-eoleaf, /fr/pages/devenez-distributeur), page "
  "métier (/fr/pages/professionnels), comparatif (/fr/pages/comparatif-produit) et FAQ "
  "(/fr/pages/faqs). L'extraction balisage compte 18 H1 manquants et 12 H1 trop longs ; la correction se "
  "fait dans le gabarit Shopify, ce qui traite les 12 langues d'un seul geste. "
  "Page protégée : aucune page qui ressortirait en top 3 au contrôle Search Console du premier ticket "
  "n'est modifiée. "
  "Critère d'acceptation : un H1 et un seul par page, de 20 à 70 caractères, contenant l'expression cible "
  "de la page, et zéro statut « Manquant » au re-crawl.",
  "SEO MONKEY + EOLEAF", 4.0, "A FAIRE", f"Extraction Balisage|{ANNEXES['balisage']}",
  "Jordan / Eoleaf"),

 ("SEPTEMBRE", "29/09/2026",
  "Alléger et décrire les images des gabarits d'achat",
  "Convertir en webp et recompresser les images servies par l'accueil, la collection et la fiche produit, "
  "puis renseigner les balises ALT manquantes. Chiffres du crawl : 334 images pour 91,3 Mo, 64 images "
  "au-delà de 200 Ko, 36 au-delà de 500 Ko, 99 PNG là où le webp s'impose, et 192 ALT vides sur 334 "
  "(57 %). Les plus lourdes sont des visuels de fiche produit : PurCar_1 à PurCar_6 entre 3,0 et 3,6 Mo, "
  "TeraPur_home_3 et _5 à 2,8 et 3,0 Mo, NeoPur_pro_2 et _4 à 2,7 et 3,5 Mo. "
  "Critère d'acceptation : aucune image servie au-delà de 200 Ko sur ces trois gabarits, largeur servie "
  "inférieure ou égale à 1500 px, zéro ALT vide, et LCP mobile de la fiche produit sous 2,5 s.",
  "SEO MONKEY + EOLEAF", 6.0, "A FAIRE", f"Extraction Images|{ANNEXES['images']}", "Jordan / Eoleaf"),
]

BACKLOG = [
 ("OCTOBRE", "06/10/2026",
  "Auditer le hreflang sur les 12 langues",
  "Contrôler le jeu hreflang de chaque URL sur les 12 versions (fr, en à la racine, da, de, es, fi, it, "
  "nl, no, pl, ro, sv) : réciprocité, autoréférence, présence de x-default. Le volet n'a jamais été traité "
  "depuis le début de l'accompagnement, alors que le multilingue produit déjà du trafic (« rökare » en "
  "suédois, position 16). Symptôme déjà visible au crawl : des pages en anglais servies sous le préfixe "
  "/fr (/fr/pages/how-do-hepa-filters-work, /fr/pages/mould). "
  "Critère d'acceptation : chaque URL porte le jeu complet et réciproque, plus x-default, et zéro page en "
  "langue étrangère sous /fr.",
  "SEO MONKEY", 4.0, "A FAIRE", f"Extraction Indexation|{ANNEXES['indexation']}", "Nicolas"),

 ("OCTOBRE", "13/10/2026",
  "Mesurer la vitesse gabarit par gabarit",
  "Passer un relevé Lighthouse mobile sur un exemplaire de chacun des 4 gabarits : accueil, collection, "
  "fiche produit, page métier « acheter-un-purificateur-dair-pour-* ». Aucune mesure de vitesse n'existe à "
  "ce jour dans le dossier, alors que le poids des images laisse attendre un LCP dégradé. "
  "Critère d'acceptation : LCP, INP et CLS relevés et datés pour les 4 gabarits, et un ticket ouvert par "
  "gabarit hors seuil.",
  "SEO MONKEY", 2.0, "A FAIRE", "", "Nicolas"),

 ("OCTOBRE", "20/10/2026",
  "Livrer le JSON-LD par gabarit",
  "Écrire le balisage de données structurées prêt à coller pour chaque gabarit : Product et Offer sur la "
  "fiche produit, Organization sur l'accueil, BreadcrumbList sur tous les gabarits, FAQPage sur "
  "/fr/pages/faqs. Rien n'a été posé à ce jour. "
  "Critère d'acceptation : le code est fourni gabarit par gabarit, intégré, et le test des résultats "
  "enrichis ne remonte aucune erreur.",
  "SEO MONKEY + EOLEAF", 4.0, "A FAIRE", "", "Nicolas / Eoleaf"),

 ("OCTOBRE", "27/10/2026",
  "Reprendre les liens sortants rompus",
  "Remplacer les sources citées qui ne répondent plus, en commençant par les pages FR qui portent des "
  "impressions. Le relevé compte environ 200 liens sortants en échec : 404 majoritaires, 22 en 410, 12 en "
  "503, et une cinquantaine d'URL invalides saisies dans le contenu (http://., http://ozone, "
  "https://jmjaircon.com,). Chaque erreur est répliquée sur les 12 langues, donc une correction en "
  "français se propage. "
  "Critère d'acceptation : zéro lien sortant en erreur sur les pages FR à impressions, chaque source morte "
  "remplacée par une source vivante équivalente.",
  "SEO MONKEY + EOLEAF", 3.0, "A FAIRE", f"Liens externes rompus|{ANNEXES['liens_ext']}",
  "Jordan / Eoleaf"),

 ("OCTOBRE", "27/10/2026",
  "Cadrer le crawl : robots.txt et URL à paramètres",
  "Fermer au crawl ce qui ne doit pas y entrer : /fr/search, /fr/cart, /apps/vf-product-reco/, et les URL "
  "en ?q=, ?page=, ?srsltid=. Le crawl remonte /fr/collections/vendors?q=Eoleaf, "
  "/fr/collections/vendors?page=2&q=Eoleaf et des URL en srsltid, qui consomment du budget de crawl sans "
  "rien rapporter. "
  "Critère d'acceptation : robots.txt à jour, sitemap déclaré dedans, et ces URL absentes du crawl suivant.",
  "SEO MONKEY + EOLEAF", 1.0, "A FAIRE", f"Extraction Indexation|{ANNEXES['indexation']}",
  "Nicolas / Eoleaf"),

 ("NOVEMBRE", "03/11/2026",
  "Produire le plan de maillage interne",
  "Construire la carte des silos et le plan de liens ligne à ligne, en partant du cocon sémantique XMind "
  "existant. Le volet n'a jamais été produit : l'onglet « Pages orphelines » de l'extraction indexation est "
  "resté vide, et la quarantaine de pages métier « acheter-un-purificateur-dair-pour-* » n'est pas câblée "
  "vers les fiches produit qui encaissent. Vérifier les liens déjà posés avant de proposer quoi que ce "
  "soit : sans ce contrôle, une part du plan est du travail fantôme. "
  "Critère d'acceptation : carte XMind livrée, plus un plan portant pour chaque lien la source, la "
  "destination, l'ancre en exact match, et la mention « déjà posé » oui ou non.",
  "SEO MONKEY", 6.0, "A FAIRE", "", "Nicolas"),

 ("NOVEMBRE", "10/11/2026",
  "Relever la profondeur de page et les pages orphelines",
  "Sortir la distribution des pages par niveau de clic depuis l'accueil, la liste des pages d'achat au-delà "
  "du niveau 3, et la liste des orphelines croisée avec les impressions Search Console. "
  "Critère d'acceptation : aucune page d'achat au-delà du niveau 3, et chaque orpheline soit reçoit un lien "
  "interne, soit est fusionnée.",
  "SEO MONKEY", 3.0, "A FAIRE", f"Extraction Indexation|{ANNEXES['indexation']}", "Nicolas"),

 ("NOVEMBRE", "17/11/2026",
  "Dessiner les maquettes SXO par étage de l'arbre",
  "Produire une maquette par étage de l'arbre : hub de silo, collection, fiche produit, page question. À la "
  "charte Eoleaf, avec les sections de preuve et les liens du plan de maillage posés au bon endroit dans la "
  "page. "
  "Critère d'acceptation : une maquette HTML par étage, reprenant le contenu réel de la page capturée, et "
  "respectant le plan de maillage du ticket précédent.",
  "SEO MONKEY", 8.0, "A FAIRE", "", "Nicolas"),
]

CONSTATS = [
 ("Indexation", "Pages relevées comme indexées au crawl du 20/05/2026", "39",
  "À confronter à la Search Console : le chiffre est incohérent avec les positions de l'onglet sémantique."),
 ("Indexation", "URL classées en erreur client au crawl du 20/05/2026", "environ 250",
  "Dont des pages positionnées de la 4e à la 8e place. Rejet Shopify sous charge suspecté, à trancher."),
 ("Indexation", "Versions linguistiques du site", "12",
  "fr, en à la racine, da, de, es, fi, it, nl, no, pl, ro, sv. Chaque correction de gabarit se propage."),
 ("Balisage", "Meta titles trop longs / trop courts / manquants", "11 / 13 / 8",
  "Une partie a été intégrée en juin et juillet, à recontrôler au re-crawl."),
 ("Balisage", "Meta descriptions trop longues / manquantes", "15 / 12",
  "Aucune description trop courte relevée."),
 ("Balisage", "H1 trop longs / trop courts / manquants", "12 / 3 / 18",
  "Les 18 manquants se concentrent sur 5 gabarits : 5 corrections, pas 18."),
 ("Balisage", "Pages à deux H1 corrigées le 24/08/2026", "23 sur 23",
  "Vérifié : la colonne « H1 count now » est à 1 sur les 23 lignes."),
 ("Images", "Images relevées et poids total", "334 pour 91,3 Mo",
  "Moyenne de 273 Ko par image, très au-delà d'un gabarit e-commerce sain."),
 ("Images", "Images au-delà de 200 Ko / de 500 Ko", "64 / 36",
  "La plus lourde atteint 3,58 Mo (PurCar_6.png)."),
 ("Images", "Formats servis", "232 jpeg, 99 png, 3 svg",
  "Aucun webp. Les PNG de fiche produit portent l'essentiel du surpoids."),
 ("Images", "Balises ALT vides", "192 sur 334, soit 57 %",
  "Perte sèche sur Google Images et sur l'accessibilité."),
 ("Maillage", "Liens internes rompus encore marqués FALSE", "33 sur 38",
  "Le ticket est pourtant déclaré intégré au 14/08/2026 dans la roadmap."),
 ("Maillage", "Liens sortants en échec", "environ 200",
  "404 majoritaires, 22 en 410, 12 en 503, une cinquantaine d'URL invalides saisies dans le contenu."),
 ("Maillage", "Plan de maillage interne existant", "aucun",
  "L'onglet « Pages orphelines » de l'extraction indexation est vide."),
 ("Vitesse", "Relevé Lighthouse par gabarit", "aucun",
  "Volet jamais ouvert depuis le début de l'accompagnement."),
 ("JSON-LD", "Données structurées relevées", "aucune",
  "Product, Offer, Organization, BreadcrumbList et FAQPage attendus sur un site marchand."),
 ("Hreflang", "Audit hreflang réalisé", "aucun",
  "12 langues en production, et des pages en anglais servies sous le préfixe /fr."),
]
