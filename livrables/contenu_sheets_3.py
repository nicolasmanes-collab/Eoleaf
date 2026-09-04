# -*- coding: utf-8 -*-
"""Contenu des Sheets de travail Eoleaf - octobre et novembre."""
FICHIERS = {}

FICHIERS["Hreflang 12 langues Eoleaf"] = (
 "Important ⚠️ : le hreflang dit à Google quelle version servir à quel pays. Sur 12 langues en "
 "production, un jeu incomplet ou non réciproque fait servir la mauvaise langue et met les versions en "
 "concurrence. Volet jamais audité. Symptôme déjà visible : 36 URL anglaises servies sous /fr.",
 ["LANGUE","CODE HREFLANG ATTENDU","PREFIXE URL","JEU COMPLET","AUTOREFERENCE","RECIPROCITE","X-DEFAULT","ANOMALIE RELEVEE","STATUT"],
 [
  ["Anglais","en","/ (racine)","","","","Devrait porter x-default","36 URL anglaises dupliquées sous /fr",'A FAIRE'],
  ["Français","fr","/fr/","","","","non","Contenu anglais servi sous ce préfixe",'A FAIRE'],
  ["Danois","da","/da/","","","","non","",'A FAIRE'],
  ["Allemand","de","/de/","","","","non","",'A FAIRE'],
  ["Espagnol","es","/es/","","","","non","",'A FAIRE'],
  ["Finnois","fi","/fi/","","","","non","",'A FAIRE'],
  ["Italien","it","/it/","","","","non","",'A FAIRE'],
  ["Néerlandais","nl","/nl/","","","","non","",'A FAIRE'],
  ["Norvégien","no","/no/","","","","non","",'A FAIRE'],
  ["Polonais","pl","/pl/","","","","non","",'A FAIRE'],
  ["Roumain","ro","/ro/","","","","non","",'A FAIRE'],
  ["Suédois","sv","/sv/","","","","non","Porte du trafic : « rökare » en position 16",'A FAIRE'],
  ["","","","","","","","",""],
  ["POINT DE CONTROLE","CE QU'ON VERIFIE","","","","","","",""],
  ["Réciprocité","Si /fr/X déclare /de/X, alors /de/X doit déclarer /fr/X","","","","","","",""],
  ["Autoréférence","Chaque page se déclare elle-même dans son propre jeu","","","","","","",""],
  ["x-default","Une seule version porte x-default, en principe l'anglais","","","","","","",""],
  ["Cohérence canonique","La canonique d'une page pointe vers elle-même, jamais vers une autre langue","","","","","","",""],
  ["Codes de langue","Format ISO 639-1 en minuscules, sans code pays sauf ciblage pays réel","","","","","","",""],
 ])

FICHIERS["Vitesse par gabarit Eoleaf"] = (
 "Important ⚠️ : la vitesse se mesure par gabarit, pas URL par URL : un gabarit corrigé corrige toutes "
 "ses pages. Aucune mesure n'existe à ce jour dans le dossier, alors que 91,3 Mo d'images laissent "
 "attendre un LCP dégradé. Mobile d'abord. Seuils : LCP sous 2,5 s, INP sous 200 ms, CLS sous 0,1.",
 ["GABARIT","URL TEMOIN","LCP MOBILE","INP","CLS","SCORE PERF","POIDS PAGE","VERDICT","PREMIER LEVIER","STATUT"],
 [
  ["Accueil","/fr","","","","","","","Image fr_qualite_d_air à 2,9 Mo",'A FAIRE'],
  ["Catégorie","/fr/collections/purificateurs-air","","","","","","","Vignettes produit en PNG",'A FAIRE'],
  ["Fiche produit","/fr/products/purificateur-air-purcar","","","","","","","6 visuels PNG entre 3,0 et 3,6 Mo",'A FAIRE'],
  ["Page métier","/fr/pages/acheter-un-purificateur-dair-hepa","","","","","","","À relever",'A FAIRE'],
  ["Question","/fr/pages/comment-fonctionnent-les-filtres-hepa","","","","","","","À relever",'A FAIRE'],
  ["Géo","/fr/pages/qualite-de-lair-a-lyon","","","","","","","À relever",'A FAIRE'],
  ["","","","","","","","","",""],
  ["SEUIL","LCP","INP","CLS","","","","","",""],
  ["Bon","moins de 2,5 s","moins de 200 ms","moins de 0,1","","","","","",""],
  ["A améliorer","2,5 à 4 s","200 à 500 ms","0,1 à 0,25","","","","","",""],
  ["Mauvais","plus de 4 s","plus de 500 ms","plus de 0,25","","","","","",""],
  ["","","","","","","","","",""],
  ["ORDRE DE PRIORITE","Le gabarit fiche produit passe avant le score global du site : c'est lui qui encaisse","","","","","","","",""],
 ])

FICHIERS["JSON-LD par gabarit Eoleaf"] = (
 "Important ⚠️ : les données structurées permettent les résultats enrichis (prix, note, disponibilité, "
 "fil d'Ariane) et donnent du contexte à Google sur l'entité Eoleaf. Aucune donnée structurée relevée à "
 "ce jour. Le livrable attendu est le code prêt à coller, gabarit par gabarit, pas une recommandation.",
 ["GABARIT","URL TEMOIN","TYPE ATTENDU","PRESENT","PROPRIETES OBLIGATOIRES","GAIN ATTENDU","STATUT"],
 [
  ["Accueil","/fr","Organization + WebSite","Non relevé","name, url, logo, sameAs, contactPoint","Entité reconnue, panneau de marque",'A FAIRE'],
  ["Fiche produit","/fr/products/purificateur-air-altapur-700","Product + Offer","Non relevé","name, image, description, sku, brand, offers (price, priceCurrency, availability)","Prix et disponibilité dans la SERP",'A FAIRE'],
  ["Fiche produit","idem","AggregateRating","Non relevé","ratingValue, reviewCount","Étoiles dans la SERP : nécessite des avis réels sur la fiche",'A FAIRE'],
  ["Catégorie","/fr/collections/purificateurs-air","CollectionPage + ItemList","Non relevé","name, itemListElement","Contexte de la liste",'A FAIRE'],
  ["Tous les gabarits","toutes","BreadcrumbList","Non relevé","itemListElement (position, name, item)","Fil d'Ariane dans la SERP à la place de l'URL",'A FAIRE'],
  ["FAQ","/fr/pages/faqs","FAQPage","Non relevé","mainEntity (Question, acceptedAnswer)","Questions dépliables dans la SERP",'A FAIRE'],
  ["Page métier","/fr/pages/acheter-un-purificateur-dair-hepa","Article + Person (auteur)","Non relevé","headline, author, datePublished, dateModified","Signal E-E-A-T : un auteur identifié",'A FAIRE'],
  ["Comparatif","/fr/pages/comparatif-produit","ItemList","Non relevé","itemListElement","Contexte du comparatif",'A FAIRE'],
  ["Avis clients","/fr/pages/avis-clients","Review","Non relevé","itemReviewed, author, reviewRating","Preuve sociale structurée",'A FAIRE'],
  ["","","","","","",""],
  ["POINT DE VIGILANCE","Ne déclarer AggregateRating que si les avis sont réellement affichés sur la page : sinon Google sanctionne","","","","",""],
  ["CRITERE D'ACCEPTATION","Test des résultats enrichis sans erreur ni avertissement bloquant sur chacun des gabarits","","","","",""],
 ])

FICHIERS["Redirections AEROPRO Eoleaf"] = (
 "Important ⚠️ : la gamme a changé de nom (AEROPRO devenu NeoPur, TeraPur, AltaPur) mais les anciennes "
 "URL circulent encore et répondent en erreur. Elles reçoivent des liens internes et probablement des "
 "liens externes : sans 301, cette autorité est perdue et le visiteur tombe sur une page morte.",
 ["ANCIENNE URL","ANCIEN MODELE","NOUVEAU MODELE","REDIRECTION 301 VERS","LIENS INTERNES POINTANT DESSUS","STATUT"],
 [
  ["/fr/products/aeropro-40-airpurifier","AEROPRO 40","NeoPur 400","/fr/products/purificateur-air-neopur-400","À relever",'A FAIRE'],
  ["/fr/products/aeropro-100-airpurifier","AEROPRO 100","TeraPur 600","/fr/products/purificateur-air-terapur-600","À relever",'A FAIRE'],
  ["/fr/products/aeropro-150-airpurifier","AEROPRO 150","AltaPur 700","/fr/products/purificateur-air-altapur-700","À relever",'A FAIRE'],
  ["/collections/air-purifiers/products/aeropro-150-airpurifier-en","AEROPRO 150 (EN)","AltaPur 700","/products/altapur-700-air-purifier","Cible morte répétée sur 12 langues",'A FAIRE'],
  ["/collections/air-purifiers/products/altapur-700-air-purifier-en","suffixe -en parasite","AltaPur 700","/products/altapur-700-air-purifier","24 liens internes, toutes langues",'A FAIRE'],
  ["/fr/collections/air-purifiers/products/aeropro-150-airpurifier","AEROPRO 150 sous /fr","AltaPur 700","/fr/products/purificateur-air-altapur-700","Appelée depuis 3 pages FR",'A FAIRE'],
  ["/products/altapur-700-air-purifier-en","suffixe -en parasite","AltaPur 700","/products/altapur-700-air-purifier","Déjà en redirection : vérifier la cible finale",'A FAIRE'],
  ["","","","","",""],
  ["A VERIFIER AUSSI","Les visuels de fiche produit portent encore les noms AEROPRO40, AEROPRO100, AEROPRO150 dans leurs fichiers : sans impact SEO direct, mais les ALT doivent nommer le modèle actuel","","","",""],
 ])

FICHIERS["Doublons pages service Eoleaf"] = (
 "Important ⚠️ : plusieurs pages de service existent en deux exemplaires, l'un en français, l'autre avec "
 "le slug anglais sous le même préfixe. Deux URL pour un même service, c'est un choix imposé à Google et "
 "un lien interne sur deux qui part au mauvais endroit.",
 ["SUJET","URL A CONSERVER","URL DOUBLON","CODE HTTP DOUBLON","ACTION","STATUT"],
 [
  ["Conditions de garantie","/fr/pages/conditions-garantie","/fr/pages/warranty-terms","Erreur client","301 vers la page conservée",'A FAIRE'],
  ["Formulaire SAV","/fr/pages/formulaire-sav","/fr/pages/formulaire-apres-vente","404","301 vers la page conservée",'A FAIRE'],
  ["Photos clients","/fr/pages/photos-clients","/fr/pages/client-photos","Erreur client","301 vers la page conservée",'A FAIRE'],
  ["Générateurs d'ozone","/fr/pages/purificateurs-dair-a-lozone-et-generateurs-dozone-ce-quil-faut-savoir","/fr/pages/purificateurs-et-generateurs-a-lozone-ce-quil-faut-savoir","Erreur client","Fusionner puis 301 : voir le fichier Cannibalisation",'A FAIRE'],
  ["Belgique","/fr/pages/acheter-un-purificateur-dair-en-belgique","/fr/pages/buying-an-air-purifier-in-belgium","Erreur client","301 vers la page conservée",'A FAIRE'],
  ["Recherche interne","non applicable","/fr/search","Erreur client","Interdire au crawl : voir le fichier Robots et paramètres",'A FAIRE'],
  ["Panier","non applicable","/fr/cart","Indexée","Interdire au crawl : une page panier n'a rien à faire dans l'index",'A FAIRE'],
  ["Recommandation produit","non applicable","/apps/vf-product-reco/2t6d2b2b","noindex","Interdire au crawl : application tierce",'A FAIRE'],
  ["","","","","",""],
  ["METHODE","Avant chaque 301, vérifier que la page conservée reçoit bien les liens internes qui pointaient vers le doublon","","","",""],
 ])

FICHIERS["Sitemap contre pages Eoleaf"] = (
 "Important ⚠️ : le sitemap est la liste que le site déclare à Google. Deux écarts coûtent cher : une page "
 "indexable absente du sitemap, que Google découvre mal ; une URL déclarée au sitemap qui répond autre "
 "chose que 200, qui abîme la confiance dans le fichier. Grille à remplir au re-crawl du ticket 01.",
 ["TYPE D'ECART","URL","PRESENTE AU SITEMAP","CODE HTTP","INDEXABLE","ACTION","STATUT"],
 [
  ["Sitemap à localiser","https://eoleaf.com/sitemap.xml","","","","Relever les sitemaps enfants générés par Shopify (produits, collections, pages, blogs) et par l'application de traduction",'A FAIRE'],
  ["Déclaration robots.txt","","","","","Vérifier que le sitemap est déclaré dans robots.txt",'A FAIRE'],
  ["Sitemap par langue","","","","","Vérifier qu'il existe un sitemap par langue, ou un sitemap global portant les 12 versions",'A FAIRE'],
  ["Indexable hors sitemap","","","","","Lister puis corriger",'A FAIRE'],
  ["Au sitemap mais non 200","","","","","Lister puis retirer ou corriger",'A FAIRE'],
  ["Au sitemap mais noindex","","","","","Lister puis trancher",'A FAIRE'],
  ["Au sitemap mais redirigée","","","","","Remplacer par l'URL de destination",'A FAIRE'],
  ["Au sitemap mais non canonique","","","","","Remplacer par l'URL canonique",'A FAIRE'],
  ["","","","","","",""],
  ["A CONTROLER EN PRIORITE","Les 3 anciennes URL AEROPRO et les 36 URL anglaises sous /fr ne doivent pas figurer au sitemap","","","","",""],
 ])

FICHIERS["Robots et parametres Eoleaf"] = (
 "Important ⚠️ : chaque URL inutile crawlée est du budget que Google ne passe pas sur les pages qui "
 "vendent. Le crawl remonte des URL de recherche interne, de panier, d'application tierce et des URL à "
 "paramètres. Une directive dans robots.txt suffit à les fermer.",
 ["MOTIF","CHEMIN OU PARAMETRE","EXEMPLE RELEVE","DIRECTIVE A POSER","STATUT"],
 [
  ["Recherche interne","/search","/fr/search","Disallow: /*/search",'A FAIRE'],
  ["Panier","/cart","/fr/cart","Disallow: /*/cart",'A FAIRE'],
  ["Compte client","/account","à confirmer","Disallow: /*/account",'A FAIRE'],
  ["Application tierce","/apps/","/apps/vf-product-reco/2t6d2b2b","Disallow: /apps/",'A FAIRE'],
  ["Liste par fournisseur","/collections/vendors","/fr/collections/vendors?q=Eoleaf","Disallow: /*/collections/vendors",'A FAIRE'],
  ["Paramètre de recherche","?q=","/fr/collections/vendors?page=2&q=Eoleaf","Disallow: /*?*q=",'A FAIRE'],
  ["Paramètre Google Shopping","?srsltid=","/pages/learning-centre?srsltid=AfmBOoq...","Disallow: /*?*srsltid=",'A FAIRE'],
  ["Paramètre de redirection","?redirected=true","/fr/pages/quest-ce-que-la-filtration-au-charbon-actif?redirected=true","Disallow: /*?*redirected=",'A FAIRE'],
  ["Paramètre inconnu","?ose=","/pages/why-is-it-important-to-change-the-filter...?ose=false","Disallow: /*?*ose=",'A FAIRE'],
  ["Pagination de collection","?page=","/fr/collections/all?page=2","À NE PAS interdire : laisser crawler, canonique autoréférente sur chaque page",'A FAIRE'],
  ["Déclaration du sitemap","","","Sitemap: https://eoleaf.com/sitemap.xml",'A FAIRE'],
  ["","","","",""],
  ["POINT DE VIGILANCE","Shopify gère un robots.txt éditable par le thème (robots.txt.liquid) : les directives se posent là, pas à la main sur le serveur","","",""],
  ["A NE JAMAIS INTERDIRE","Les chemins /products/, /collections/ et /pages/ : ce sont les pages qui vendent","","",""],
 ])
