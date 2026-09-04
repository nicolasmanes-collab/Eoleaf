# -*- coding: utf-8 -*-
"""Roadmap technique Eoleaf — septembre à novembre 2026.

Le ticket dit quoi faire et à quoi on sait qu'il est fini. Le détail vit dans
le Sheet de travail porté par la colonne LIVRABLE, un par ticket, rangé dans
« 2 - Technique / 5 - Mois 5 (septembre) » du Drive client.

Sources des constats : les 5 extractions du Drive (crawl du 20/05/2026), le
relevé H1 du 24/08/2026, l'onglet sémantique de la roadmap client.
Ordre des tickets = ordre d'impact business, jamais la sévérité du crawler.
"""

D = "https://docs.google.com/spreadsheets/d"
LIV = {
    "indexation":     f"{D}/1b_tVRfcWzqweKpb5L30yiDJtstaU5D82CE6gUWNYrEo/edit",
    "canonique":      f"{D}/1-n0jKORE6XE_sI7gnLOe5n5orXDtGtnIVFIc24ttoHs/edit",
    "contact":        f"{D}/1Xbtiqi8qqxckCMM9tamEXibKGKJnycpl10XoOnbg_0Q/edit",
    "pages_en":       f"{D}/1dzRHnQFaMkPXW3hvyO_A8-x0JwlwhUAi7MEY7giwvao/edit",
    "cannibalisation":f"{D}/1KzD2Mf-ugn3jPmKIFoYTrXalEtu1VyeoZof5pAkUwyc/edit",
    "h1":             f"{D}/1Q6k2HwvNLGqNTloPdjTfgDheWMCL3vIJxo4OL5BJNTE/edit",
    "images":         f"{D}/154aIMHSG_lqUWNOCfNlvgo9ZNHlvUESCsTherEkdcFE/edit",
    "hreflang":       f"{D}/1MBkbFcXU3orsOy2sg8G5fAnB_hZEP6B-8hDDubPj__8/edit",
    "vitesse":        f"{D}/1QFxHJEqA3_U7PFg_Uk8LAHcUIhfHMoybX7s1n66SvAs/edit",
    "jsonld":         f"{D}/1sRODCSAIrNeRLF8Hq6r5Vmflq2jNSXjzzoMZYX2WRo8/edit",
    "aeropro":        f"{D}/1WntNwaXwSKQvZTx6WlzFb1HHujttU6rBjMG_choz6sA/edit",
    "doublons":       f"{D}/1tpgQ9FPnXUAZMuWnQZB57l_3WAbOUC9ISUbq_IfFVxY/edit",
    "sitemap":        f"{D}/1RMWs2FaTOHIcXs-frPj4xF-mshvxdZOUMCwOwZFjIM4/edit",
    "robots":         f"{D}/1oggu_W80Xm-SyQFoyOxGFYEndqvmYiSMBZCJs3GVmqQ/edit",
    "liens_sortants": f"{D}/13rEU2zMOXDBtBzwUjTdmn7_Q6JqiLZnW1IZKj82nd5w/edit",
    "maillage":       f"{D}/1mXYafC-aJlmM8Mph3TIvJIHo2SM8Vfsd4b0v5jJSY0g/edit",
    "profondeur":     f"{D}/1CYMTMD5UYeEz0X0_5aqIadVJUYGchMSwcTaf0NoV7_E/edit",
    "geo":            f"{D}/1XGesA1Kf8IRRNWSMuvSs4JHyIjSipNuv0MOpWM-y0sk/edit",
    "comparatifs":    f"{D}/1-gqb1QzLV9mQQ1b6eVQEhVUUQTf1goEwmq-ulGvcB_Y/edit",
    # fichier deja existant chez le client, on ecrit dedans plutot que d'en creer un second
    "liens_internes": f"{D}/1c7_Bu5rdkz9TmV9wHW_I_RJsEEtkrmIMETtDe1oxpRM/edit",
}

# MOIS, DATE, TICKET, DETAILS, REPARTITION, HEURES, STATUT, LIVRABLE(libellé|url), INTERVENANT, SEVERITE
SEPTEMBRE = [
 ("SEPTEMBRE", "04/09/2026", "Redirections des anciennes URL AEROPRO",
  "Poser les 301 des anciennes URL produit AEROPRO 40, 100 et 150 vers les fiches NeoPur 400, "
  "TeraPur 600 et AltaPur 700. Traité par Nicolas le 04/09/2026, avant l'échéance d'octobre. Le contrôle "
  "Search Console confirmait le besoin : /fr/products/aeropro-150-airpurifier ressortait en « Explorée, "
  "actuellement non indexée ». "
  "Fini quand : chaque ancienne URL répond 301 en un saut vers la fiche du modèle actuel.",
  "EOLEAF", 1.0, "TERMINE", f"Redirections AEROPRO Eoleaf|{LIV['aeropro']}", "Nicolas", "freine"),

  ("SEPTEMBRE", "01/09/2026", "Re-crawl de contrôle indexation",
  "Relancer le crawl en 1 thread et 1 URL par seconde, user-agent Googlebot Smartphone, puis confronter "
  "chaque statut à l'inspection d'URL de la Search Console sur 10 URL témoin. L'extraction du 20/05 classe "
  "environ 250 URL en erreur client alors que certaines se positionnent de la 4e à la 8e place : les deux "
  "ne peuvent pas être vrais. Ce ticket conditionne la lecture des sept autres. "
  "Fini quand : nouvel export d'indexation daté, écart crawl / Search Console expliqué ligne à ligne, "
  "ancien onglet renommé « z · Indexation 05-2026 (ancien) ».",
  "SEO MONKEY", 3.0, "TERMINE", f"Controle indexation Eoleaf|{LIV['indexation']}", "Nicolas", "bloque"),

 ("SEPTEMBRE", "01/09/2026", "Canonique des fiches produit",
  "Retenir une seule forme d'URL indexable par produit, poser la canonique autoréférente dessus et aligner "
  "les liens internes. Les pages indexées sont en /fr/products/ alors que l'onglet « Tableau de balisage » "
  "prépare les titles sur les URL en /fr/collections/.../products/ : intégré en l'état, ce balisage se pose "
  "à côté des pages qui rankent. "
  "Fini quand : une seule URL par produit répond 200 sans redirection, canonique autoréférente, et l'onglet "
  "« Tableau de balisage » corrigé avant intégration.",
  "SEO MONKEY", 2.0, "A FAIRE", f"Canonique fiches produit Eoleaf|{LIV['canonique']}", "Nicolas", "bloque"),

 ("SEPTEMBRE", "08/09/2026", "Lien FAQ vers un formulaire SAV mort",
  "Poser une 301 de /fr/pages/formulaire-apres-vente vers /fr/pages/formulaire-sav et corriger le lien "
  "depuis /fr/pages/faqs. Périmètre réduit par le contrôle Search Console du 04/09 : les pages contact FR, "
  "EN et DE sont indexées et saines, la FR est même en position 2,2 avec 477 impressions. Le crawl du 20/05 "
  "les déclarait en erreur à tort. Seule l'URL formulaire-apres-vente est réellement morte. "
  "Fini quand : /fr/pages/formulaire-apres-vente répond 301 vers formulaire-sav, et la FAQ pointe "
  "directement vers l'URL vivante.",
  "EOLEAF", 0.5, "A FAIRE", f"Contact et SAV 12 langues Eoleaf|{LIV['contact']}",
  "Eoleaf", "bloque"),

 ("SEPTEMBRE", "08/09/2026", "36 pages EN sous /fr : budget de crawl",
  "Rediriger en 301 les 36 URL anglaises servies sous /fr : vers la page FR équivalente quand elle "
  "existe, sinon vers l'URL anglaise à la racine. "
  "Périmètre revu par le contrôle Search Console du 04/09 : sur les 33 de ces URL sans impression, 28 "
  "ressortent en « Google ne reconnaît pas cette URL ». Elles ne sont donc pas indexées et ne "
  "cannibalisent rien. Ce qu'elles coûtent : du budget de crawl, et des liens internes qui partent dans "
  "le vide. Le ticket reste utile mais n'est plus bloquant, et son volume baisse. "
  "Fini quand : les 36 URL répondent 301 en un saut vers la bonne cible, et aucune ne figure plus au "
  "sitemap ni dans un lien interne.",
  "EOLEAF", 2.0, "A FAIRE", f"Pages EN sous prefixe fr Eoleaf|{LIV['pages_en']}",
  "Eoleaf", "crawl"),

 ("SEPTEMBRE", "15/09/2026", "Cannibalisation : 14 clusters FR",
  "Désigner un pilier par cluster, fusionner les doublons d'intention dans ce pilier puis poser les 301. "
  "L'onglet sémantique en porte la preuve : « purificateur d'air voiture » est planifié sur 3 URL, "
  "« purificateur d'air chambre » sur 2, « allergie chat » sur 2, « fumée de cigarette » sur 2. Le cluster "
  "dentaire compte 3 pages sur la même intention, le cluster tabac 5. "
  "Fini quand : un seul pilier par cluster, contenu utile remonté avant la 301, aucune page en top 3 "
  "touchée.",
  "SEO MONKEY", 5.0, "A FAIRE", f"Cannibalisation clusters FR Eoleaf|{LIV['cannibalisation']}",
  "Jordan / Nicolas", "bloque"),

 ("SEPTEMBRE", "22/09/2026", "33 liens internes rompus",
  "Corriger les 33 lignes encore marquées « Réglé ? = FALSE » dans le fichier existant, alors que le ticket "
  "est déclaré intégré au 14/08. Deux cibles mortes reviennent sur les 12 langues. La colonne « Newlink » "
  "porte déjà la cible de remplacement : il n'y a pas de mapping à refaire. "
  "Fini quand : zéro ligne FALSE, et les 38 liens répondent 200 en un seul saut.",
  "EOLEAF", 2.0, "A FAIRE", f"liens internes rompus|{LIV['liens_internes']}", "Eoleaf", "freine"),

 ("SEPTEMBRE", "22/09/2026", "H1 manquants sur 5 gabarits",
  "Poser un H1 unique sur les gabarits qui en sont dépourvus : collection, institutionnel, page métier, "
  "comparatif et FAQ. 18 H1 manquants et 12 trop longs relevés, mais 5 corrections de gabarit Shopify "
  "suffisent et traitent les 12 langues d'un seul geste. Les H1 sont déjà rédigés dans le livrable. "
  "Fini quand : un H1 et un seul par page, de 20 à 70 caractères, contenant l'expression cible, et zéro "
  "statut « Manquant » au re-crawl.",
  "SEO MONKEY + EOLEAF", 4.0, "A FAIRE", f"H1 manquants Eoleaf|{LIV['h1']}", "Jordan / Eoleaf", "freine"),

 ("SEPTEMBRE", "29/09/2026", "Images des gabarits d'achat",
  "Convertir en webp et recompresser les images de l'accueil, de la collection et de la fiche produit, puis "
  "renseigner les ALT. 334 images pour 91,3 Mo, 64 au-delà de 200 Ko, 36 au-delà de 500 Ko, 99 PNG, aucun "
  "webp, et 192 ALT vides sur 334. Les plus lourdes sont des visuels de fiche produit, entre 2,7 et 3,6 Mo. "
  "Les ALT sont déjà rédigés dans le livrable. "
  "Fini quand : aucune image servie au-delà de 200 Ko sur ces trois gabarits, largeur servie ≤ 1500 px, "
  "zéro ALT vide, LCP mobile de la fiche produit sous 2,5 s.",
  "SEO MONKEY + EOLEAF", 6.0, "A FAIRE", f"Images a corriger Eoleaf|{LIV['images']}",
  "Jordan / Eoleaf", "freine"),
]

OCTOBRE = [
 ("OCTOBRE", "06/10/2026", "Hreflang sur 12 langues",
  "Contrôler le jeu hreflang de chaque URL sur les 12 versions : réciprocité, autoréférence, x-default. "
  "Volet jamais audité, alors que le multilingue produit déjà du trafic (« rökare » en suédois, position "
  "16). "
  "Fini quand : chaque URL porte le jeu complet et réciproque plus x-default, et zéro page en langue "
  "étrangère sous /fr.",
  "SEO MONKEY", 4.0, "A FAIRE", f"Hreflang 12 langues Eoleaf|{LIV['hreflang']}", "Nicolas", "freine"),

 ("OCTOBRE", "13/10/2026", "Doublons de pages de service",
  "Fusionner les pages de service existant en deux exemplaires, l'une au slug français, l'autre au slug "
  "anglais sous le même préfixe : garantie, SAV, photos clients, Belgique, ozone. "
  "Fini quand : une seule URL par service répond 200, le doublon répond 301, et les liens internes pointent "
  "vers la page conservée.",
  "EOLEAF", 2.0, "A FAIRE", f"Doublons pages service Eoleaf|{LIV['doublons']}", "Eoleaf", "crawl"),

 ("OCTOBRE", "20/10/2026", "Vitesse par gabarit",
  "Relever Lighthouse mobile sur un exemplaire de chacun des 6 gabarits : accueil, collection, fiche "
  "produit, page métier, question, géo. Aucune mesure de vitesse n'existe à ce jour dans le dossier. "
  "Fini quand : LCP, INP et CLS relevés et datés pour les 6 gabarits, et un ticket ouvert par gabarit hors "
  "seuil.",
  "SEO MONKEY", 2.0, "A FAIRE", f"Vitesse par gabarit Eoleaf|{LIV['vitesse']}", "Nicolas", "freine"),

 ("OCTOBRE", "27/10/2026", "JSON-LD hors fiche produit",
  "Écrire et intégrer le balisage de données structurées pour l'accueil (Organization, WebSite), la "
  "catégorie (CollectionPage, ItemList), les pages métier (Article, Person) et la FAQ (FAQPage). "
  "Périmètre réduit par le contrôle Search Console du 04/09 : la fiche produit porte déjà Product, Offer et "
  "AggregateRating, verdict PASS, avec extraits de produit, fiche de marchand et extraits d'avis détectés. "
  "Réserve : l'inspection d'URL ne remonte que les types éligibles aux résultats enrichis, l'absence de "
  "BreadcrumbList reste à confirmer dans le code des gabarits. "
  "Fini quand : le test des résultats enrichis ne remonte aucune erreur sur les quatre gabarits restants.",
  "SEO MONKEY + EOLEAF", 3.0, "A FAIRE", f"JSON-LD par gabarit Eoleaf|{LIV['jsonld']}",
  "Nicolas / Eoleaf", "freine"),

 ("OCTOBRE", "27/10/2026", "Sitemap contre pages réelles",
  "Confronter le sitemap aux pages du re-crawl : indexables absentes du sitemap, et URL déclarées qui ne "
  "répondent pas 200. Vérifier aussi la couverture des 12 langues et la déclaration dans robots.txt. "
  "Fini quand : chaque URL du sitemap répond 200 et est canonique, et chaque page indexable y figure.",
  "SEO MONKEY", 2.0, "A FAIRE", f"Sitemap contre pages Eoleaf|{LIV['sitemap']}", "Nicolas", "crawl"),
]

NOVEMBRE = [
 ("NOVEMBRE", "03/11/2026", "Robots.txt et URL à paramètres",
  "Fermer au crawl la recherche interne, le panier, /apps/ et les URL en ?q=, ?srsltid=, ?redirected=. Ces "
  "URL consomment du budget de crawl sans rien rapporter. La pagination de collection, elle, reste ouverte. "
  "Fini quand : robots.txt.liquid à jour, sitemap déclaré dedans, et ces URL absentes du crawl suivant.",
  "SEO MONKEY + EOLEAF", 1.0, "A FAIRE", f"Robots et parametres Eoleaf|{LIV['robots']}",
  "Nicolas / Eoleaf", "crawl"),

 ("NOVEMBRE", "03/11/2026", "Liens sortants rompus",
  "Remplacer les sources citées qui ne répondent plus, pages FR à impressions d'abord. Environ 200 liens "
  "sortants en échec : 404 en majorité, 22 en 410, 12 en 503, et une cinquantaine d'URL invalides saisies "
  "dans le contenu. Chaque erreur étant répliquée sur 12 langues, une correction en français se propage. "
  "Fini quand : zéro lien sortant en erreur sur les pages FR à impressions, chaque source morte remplacée "
  "par une source vivante équivalente.",
  "SEO MONKEY + EOLEAF", 3.0, "A FAIRE", f"Liens sortants a remplacer Eoleaf|{LIV['liens_sortants']}",
  "Jordan / Eoleaf", "freine"),

 ("NOVEMBRE", "10/11/2026", "Plan de maillage interne",
  "Construire la carte des silos et le plan de liens ligne à ligne, à partir du cocon sémantique XMind. "
  "Volet jamais produit : la quarantaine de pages métier n'est pas câblée vers les fiches produit. Vérifier "
  "les liens déjà posés avant de proposer quoi que ce soit. "
  "Fini quand : carte XMind livrée, et plan portant pour chaque lien la source, la destination, l'ancre en "
  "exact match et la mention « déjà posé ».",
  "SEO MONKEY", 6.0, "A FAIRE", f"Plan de maillage Eoleaf|{LIV['maillage']}", "Nicolas", "freine"),

 ("NOVEMBRE", "10/11/2026", "Profondeur et pages orphelines",
  "Sortir la distribution des pages par niveau de clic, la liste des pages d'achat au-delà du niveau 3, et "
  "les orphelines croisées avec les impressions. L'onglet « Pages orphelines » est resté vide depuis le "
  "début. "
  "Fini quand : aucune page d'achat au-delà du niveau 3, et chaque orpheline reçoit un lien interne ou est "
  "fusionnée.",
  "SEO MONKEY", 3.0, "A FAIRE", f"Profondeur et orphelines Eoleaf|{LIV['profondeur']}", "Nicolas", "freine"),

 ("NOVEMBRE", "17/11/2026", "Couche géo : 4 pages villes",
  "Trancher le statut de la couche géo, puis aligner les 4 pages ville sur un gabarit commun et les câbler "
  "au pilier professionnel. Lyon est en position 6 et Paris en 18 : la couche produit déjà du trafic sans "
  "être structurée. Deux slugs portent une phrase entière, dont une faute de frappe. "
  "Fini quand : les 4 pages partagent le même gabarit, portent un lien vers l'unité d'achat, et les slugs "
  "fautifs sont corrigés avec 301.",
  "SEO MONKEY", 3.0, "A FAIRE", f"Pages geo villes Eoleaf|{LIV['geo']}", "Jordan", "freine"),

 ("NOVEMBRE", "24/11/2026", "13 comparatifs concurrents",
  "Aligner les pages comparatives sur un gabarit commun : tableau chiffré, preuve vérifiable, mention "
  "honnête d'un point où le concurrent est meilleur, et lien vers la fiche produit. Ce sont des pages à "
  "forte intention d'achat. Levoit est en position 20 sur 390 de volume, « dyson chauffant » en 9 sur 1900. "
  "Fini quand : chaque comparatif porte les 4 modules et un lien vers la fiche du modèle Eoleaf comparé.",
  "SEO MONKEY", 4.0, "A FAIRE", f"Comparatifs concurrents Eoleaf|{LIV['comparatifs']}", "Jordan", "freine"),

 ("NOVEMBRE", "24/11/2026", "Maquettes SXO par étage",
  "Produire une maquette par étage de l'arbre : hub de silo, collection, fiche produit, page question. À la "
  "charte Eoleaf, avec les sections de preuve et les liens du plan de maillage posés au bon endroit. "
  "Fini quand : une maquette HTML par étage, reprenant le contenu réel de la page capturée, et respectant "
  "le plan de maillage.",
  "SEO MONKEY", 8.0, "A FAIRE", "", "Nicolas", "freine"),
]

BACKLOG = OCTOBRE + NOVEMBRE

CONSTATS = [
 ("Indexation", "Pages portant au moins une impression sur 90 jours", "2 994",
  "Relevé Search Console du 04/09/2026 (03/06 au 01/09). Le crawl du 20/05 en déclarait 39 : il était faux."),
 ("Indexation", "URL déclarées non indexées au crawl qui portent en réalité des impressions", "206 sur 305",
  "Soit 68 %, cumulant 5 748 clics et 562 617 impressions sur 90 jours. Écart expliqué ligne à ligne "
  "dans l'onglet ECART CRAWL 05-2026 du nouvel export."),
 ("Indexation", "URL sans impression inspectées une à une", "99",
  "68 inconnues de Google (formes d'URL parasites), 21 explorées non indexées, 6 déjà redirigées, "
  "2 indexées sans impression, 2 canoniques ou noindex volontaires."),
 ("Indexation", "URL non couvertes par un ticket existant", "8",
  "Dont 3 unités d'achat FR explorées et non indexées. Listées dans l'onglet A ARBITRER."),
 ("Indexation", "Slugs anglais sous /fr que Google ne connaît pas", "28 sur 33",
  "Ces URL ne cannibalisent rien : le ticket passe de bloquant à budget de crawl, de 4 h à 2 h."),
 ("Indexation", "Recherche interne /fr/search", "indexée",
  "Confirmée « Envoyée et indexée ». Le ticket robots.txt est justifié."),
 ("Indexation", "URL témoin déclarées indexées par Google", "10 sur 10",
  "Inspection d'URL du 04/09. Les 6 classées « erreur client » au crawl sont saines : robots autorisé, "
  "page récupérée, dernier passage de Google entre le 22/08 et le 04/09."),
 ("Indexation", "Clics et impressions sur 90 jours", "28 889 · 3 765 160",
  "Position moyenne 12,5. Le site est massivement indexé et visible."),
 ("Indexation", "Part du français dans les clics", "21 %",
  "284 pages FR pour 6 106 clics. Les onze autres langues portent 79 % des clics : la priorisation par "
  "langue est à revoir avec Eoleaf."),
 ("Indexation", "Page la plus cliquée du site", "/de/pages/kauf-eines-luftreinigers-fur-cannabis",
  "928 clics et 10 216 impressions sur 90 jours. Elle est en allemand."),
 ("Indexation", "URL témoin absentes du sitemap", "6 sur 10",
  "Dont l'accueil FR, la fiche AltaPur 700 et deux unités d'achat. Elles rankent sans être déclarées."),
 ("Indexation", "URL déclarées au sitemap", "3 001",
  "Dernier téléchargement par Google le 03/09/2026, zéro erreur, zéro avertissement."),
 ("Sémantique", "Écart de position relevé sur l'onglet sémantique", "position 4 contre 37",
  "« purificateur d'air professionnel » : l'onglet donne 4, la Search Console 37 avec 894 impressions et "
  "3 clics. Les positions de l'onglet sémantique sont à re-sourcer."),
 ("JSON-LD", "Fiche produit", "Product, Offer et AggregateRating présents",
  "Verdict PASS au 04/09. Le gabarit qui encaisse est déjà équipé, contrairement au constat initial."),
 ("Indexation", "Versions linguistiques du site", "12",
  "fr, en à la racine, da, de, es, fi, it, nl, no, pl, ro, sv. Une correction de gabarit se propage."),
 ("Indexation", "URL anglaises servies sous le préfixe /fr", "36",
  "Duplication et mauvaise langue déclarée. Défaut de l'application de traduction."),
 ("Indexation", "Anciennes URL produit AEROPRO encore en circulation", "7",
  "La gamme a été renommée NeoPur, TeraPur, AltaPur sans que les 301 soient posées."),
 ("Sémantique", "Clusters FR où deux pages ou plus visent la même intention", "14",
  "Le cluster tabac compte 5 pages, le dentaire 3, la voiture 4. Un pilier par cluster à désigner."),
 ("Sémantique", "Requêtes de l'onglet sémantique planifiées sur plusieurs URL", "4 au moins",
  "Voiture sur 3 URL, chambre sur 2, allergie chat sur 2, fumée de cigarette sur 2."),
 ("Balisage", "Meta titles trop longs / trop courts / manquants", "11 / 13 / 8",
  "Une partie intégrée en juin et juillet, à recontrôler au re-crawl."),
 ("Balisage", "Meta descriptions trop longues / manquantes", "15 / 12",
  "Aucune description trop courte relevée."),
 ("Balisage", "H1 trop longs / trop courts / manquants", "12 / 3 / 18",
  "Les 18 manquants tiennent à 5 gabarits : 5 corrections, pas 18."),
 ("Balisage", "Pages à deux H1 corrigées le 24/08/2026", "23 sur 23",
  "Vérifié : la colonne « H1 count now » est à 1 sur les 23 lignes."),
 ("Balisage", "Lignes PRODUITS du Tableau de balisage visant la mauvaise URL", "6 sur 6",
  "Elles ciblent les URL longues alors que les pages indexées sont les URL courtes."),
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
  "404 en majorité, 22 en 410, 12 en 503, une cinquantaine d'URL invalides saisies dans le contenu."),
 ("Maillage", "Plan de maillage interne existant", "aucun",
  "L'onglet « Pages orphelines » de l'extraction indexation est vide."),
 ("Vitesse", "Relevé Lighthouse par gabarit", "aucun",
  "Volet jamais ouvert depuis le début de l'accompagnement."),
 ("JSON-LD", "Accueil, catégorie, page métier et FAQ", "aucun type enrichi détecté",
  "Organization, CollectionPage, Article et FAQPage restent à poser."),
 ("Hreflang", "Audit hreflang réalisé", "aucun",
  "12 langues en production, et des pages en anglais servies sous /fr."),
 ("Géo", "Pages ville en production", "5 dont 1 en anglais",
  "Lyon en position 6, Paris en 18, Londres en 16, Paris EN en 7. Couche non structurée."),
 ("Comparatifs", "Pages comparant Eoleaf à un concurrent", "13",
  "Fort potentiel d'achat : Levoit en position 20 sur 390, « dyson chauffant » en 9 sur 1900."),
]
