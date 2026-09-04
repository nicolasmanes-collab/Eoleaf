# -*- coding: utf-8 -*-
"""Contenu des Sheets de travail Eoleaf - tickets 01 a 05."""

# Chaque entree : (nom de fichier, bandeau "Important", en-tetes, lignes)
FICHIERS = {}

FICHIERS["Controle indexation Eoleaf"] = (
 "Important ⚠️ : le crawl du 20/05/2026 classe environ 250 URL en erreur client, dont des pages "
 "positionnées de la 4e à la 8e place sur leur requête cible. Une page morte ne se classe pas. "
 "On tranche ici avec la Search Console avant de bâtir la roadmap dessus. Re-crawl à passer en "
 "1 thread / 1 URL par seconde / user-agent Googlebot Smartphone.",
 ["URL TEMOIN","GABARIT","REQUETE CIBLE","POSITION CONNUE","STATUT CRAWL 20/05",
  "STATUT GSC A RELEVER","STATUT RE-CRAWL","VERDICT","ACTION","STATUT"],
 [
  ["https://eoleaf.com/fr","Accueil","purificateur d air hepa","19","Indexée","","","","",'A FAIRE'],
  ["https://eoleaf.com/fr/collections/purificateurs-air","Catégorie","purificateur d'air professionnel","4","Indexée","","","","",'A FAIRE'],
  ["https://eoleaf.com/fr/products/purificateur-air-altapur-700","Fiche produit","Eoleaf Altapur 700","non relevée","Indexée","","","","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/comment-fonctionnent-les-filtres-hepa","Question","filtre hepa","6","Indexée","","","","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/ioniseurs-a-quoi-servent-ils","Question","ioniseur d'air","8","Erreur client","","","Contradiction à lever","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/acheter-un-purificateur-dair-de-qualite-medicale","Unité d'achat","purificateur d'air avis medical","7","Erreur client","","","Contradiction à lever","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/acheter-un-purificateur-dair-hepa","Unité d'achat","purificateur d'air hepa","5","Erreur client","","","Contradiction à lever","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/acheter-un-purificateur-dair-pour-la-poussiere","Unité d'achat","purificateur d'air poussière","10","Erreur client","","","Contradiction à lever","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/qualite-de-lair-a-lyon","Géo","qualité de l air lyon","6","Erreur client","","","Contradiction à lever","",'A FAIRE'],
  ["https://eoleaf.com/fr/pages/contact","Contact","non applicable","non applicable","Erreur client","","","À confirmer : panne réelle probable","Voir ticket Page contact et formulaire SAV",'A FAIRE'],
  ["","","","","","","","","",""],
  ["PARAMETRES DU RE-CRAWL","VALEUR A UTILISER","MOTIF","","","","","","",""],
  ["Threads simultanés","1","Au-delà, Shopify rejette les requêtes et le crawl invente des 4xx","","","","","","",""],
  ["Limite de vitesse","1 URL par seconde","Idem","","","","","","",""],
  ["User-agent","Googlebot Smartphone","Voir le site comme Google le voit, mobile d'abord","","","","","","",""],
  ["Rendu JavaScript","Activé","Thème Shopify : une partie du contenu est injectée","","","","","","",""],
  ["Périmètre","eoleaf.com, toutes langues","12 versions en production","","","","","","",""],
  ["Contrôle croisé","Inspection d'URL GSC sur les 10 URL témoin","Seule source qui dit ce que Google a réellement indexé","","","","","","",""],
 ])

FICHIERS["Canonique fiches produit Eoleaf"] = (
 "Important ⚠️ : chaque produit Shopify est atteignable en /fr/products/<produit> ET en "
 "/fr/collections/<collection>/products/<produit>. Les pages relevées comme indexées sont les URL "
 "courtes, alors que l'onglet Tableau de balisage prépare les titles sur les URL longues. Intégré en "
 "l'état, ce balisage se pose à côté des pages qui rankent.",
 ["PRODUIT","URL COURTE","URL LONGUE","STATUT CRAWL URL COURTE","STATUT CRAWL URL LONGUE",
  "URL RETENUE","CANONIQUE A POSER","LIENS INTERNES A REPOINTER","STATUT"],
 [
  ["NeoPur 400","/fr/products/purificateur-air-neopur-400","/fr/collections/purificateurs-air/products/purificateur-air-neopur-400","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["TeraPur 600","/fr/products/purificateur-air-terapur-600","/fr/collections/purificateurs-air/products/purificateur-air-terapur-600","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["AltaPur 700","/fr/products/purificateur-air-altapur-700","/fr/collections/purificateurs-air/products/purificateur-air-altapur-700","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["PurCar","/fr/products/purificateur-air-purcar","/fr/collections/purificateurs-air/products/purificateur-air-purcar","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Capteur CO2 Smart CO2","/fr/products/capteur-co2-eoleaf-smart-co2","/fr/collections/all/products/capteur-co2-eoleaf-smart-co2","Erreur client","Erreur client","URL courte","Autoréférente vers URL courte","Unité d'achat morte au crawl : à vérifier en priorité",'A FAIRE'],
  ["Filtre NeoPur 400","/fr/products/filtre-de-rechange-neopur-400","/fr/collections/filtres-et-accessoires/products/filtre-de-rechange-neopur-400","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Filtre TeraPur 600","/fr/products/filtre-de-rechange-terapur-600","/fr/collections/filtres-et-accessoires/products/filtre-de-rechange-terapur-600","Erreur client","Erreur client","URL courte","Autoréférente vers URL courte","Les deux formes en échec : à vérifier",'A FAIRE'],
  ["Filtre AltaPur 700","/fr/products/filtre-de-rechange-altapur-700","/fr/collections/filtres-et-accessoires/products/filtre-de-rechange-altapur-700","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Préfiltre AltaPur 700","/fr/products/prefiltre-de-rechange-altapur-700","/fr/collections/filtres-et-accessoires/products/prefiltre-de-rechange-altapur-700","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Filtre PurCar","/fr/products/filtre-de-rechange-purcar","/fr/collections/filtres-et-accessoires/products/filtre-de-rechange-purcar","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Lampe UVC de rechange","/fr/products/lampe-uvc-rechange","/fr/collections/filtres-et-accessoires/products/lampe-uvc-rechange","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Terminal de contrôle","/fr/products/terminal-de-controle-rechange","/fr/collections/filtres-et-accessoires/products/terminal-de-controle-rechange","Non relevée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Terminal de contrôle 2.0","/fr/products/terminal-de-controle-rechange-2-0","/fr/collections/filtres-et-accessoires/products/terminal-de-controle-rechange-2-0","Non relevée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["Kit de communication","/fr/products/kit-communication-gratuit","/fr/collections/all/products/kit-communication-gratuit","Indexée","Erreur client","URL courte","Autoréférente vers URL courte","",'A FAIRE'],
  ["","","","","","","","",""],
  ["A CORRIGER DANS LE TABLEAU DE BALISAGE","","","","","","","",""],
  ["Les 6 lignes PRODUITS de l'onglet Tableau de balisage visent les URL longues","Remplacer par la forme courte retenue avant toute intégration","","","","","","",'A FAIRE'],
 ])

FICHIERS["Contact et SAV 12 langues Eoleaf"] = (
 "Important ⚠️ : /fr/pages/contact ressort en erreur client au crawl et /fr/pages/formulaire-apres-vente "
 "répond 404 alors que la FAQ y renvoie. Une page contact injoignable sur un site qui vend en B2B coûte "
 "des demandes entrantes chaque jour. Les slugs varient selon la langue : relever ceux des 10 autres "
 "versions avant correction.",
 ["LANGUE","URL CONTACT","CODE HTTP CONTACT","URL SAV","CODE HTTP SAV","LIEN ENTRANT DEPUIS","ACTION","STATUT"],
 [
  ["FR","/fr/pages/contact","Erreur client au crawl","/fr/pages/formulaire-sav","Indexée","/fr/pages/faqs","Vérifier le contact ; le lien FAQ pointe vers formulaire-apres-vente en 404, le repointer vers formulaire-sav",'A FAIRE'],
  ["FR (doublon)","","","/fr/pages/formulaire-apres-vente","404","/fr/pages/faqs","301 vers /fr/pages/formulaire-sav",'A FAIRE'],
  ["EN (racine)","/pages/contact","Erreur client au crawl","/pages/after-sales-form","Erreur client au crawl","À relever","Vérifier les deux",'A FAIRE'],
  ["DA","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["DE","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["ES","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["FI","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["IT","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["NL","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["NO","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["PL","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["RO","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["SV","À relever","","À relever","","À relever","Relever le slug puis vérifier",'A FAIRE'],
  ["","","","","","","",""],
  ["CRITERE D'ACCEPTATION","Les 12 URL contact et les 12 URL SAV répondent 200","","","","","",""],
  ["","Le lien depuis la FAQ pointe vers l'URL vivante sans redirection intermédiaire","","","","","",""],
 ])

FICHIERS["Pages EN sous prefixe fr Eoleaf"] = (
 "Important ⚠️ : 36 URL en anglais sont servies sous le préfixe /fr. C'est un défaut de l'application de "
 "traduction : la page existe en double et Google reçoit du contenu anglais sur une URL déclarée "
 "française. Règle de décision : si la page FR équivalente existe, 301 de l'URL anglaise vers elle ; "
 "sinon 301 vers l'URL anglaise à la racine.",
 ["URL EN SOUS /fr","SUJET","EQUIVALENT FR EXISTANT","URL EN CORRECTE A LA RACINE","ACTION","STATUT"],
 [
  ["/fr/pages/how-do-hepa-filters-work","Filtres HEPA","/fr/pages/comment-fonctionnent-les-filtres-hepa","/pages/how-do-hepa-filters-work","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/what-is-activated-carbon-filtration","Filtration charbon actif","/fr/pages/quest-ce-que-la-filtration-au-charbon-actif","/pages/what-is-activated-carbon-filtration","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/activated-carbon-and-its-role-in-air-filtration","Rôle du charbon actif","/fr/pages/le-charbon-actif-et-son-role-dans-la-filtration-de-lair","/pages/activated-carbon-and-its-role-in-air-filtration","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/all-about-ionisation","Ionisation","/fr/pages/tout-savoir-sur-lionisation","/pages/all-about-ionisation","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/ionisers-what-do-they-do","Ioniseurs","/fr/pages/ioniseurs-a-quoi-servent-ils","/pages/ionisers-what-do-they-do","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/negative-ions-and-their-benefits-on-our-health","Ions négatifs","/fr/pages/les-ions-negatifs-et-leurs-bienfaits-pour-notre-sante","/pages/negative-ions-and-their-benefits-on-our-health","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/all-about-uv-sterilisation","Stérilisation UVC","/fr/pages/tout-savoir-sur-la-sterilisation-uvc","/pages/all-about-uv-sterilisation","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/how-does-photocatalysis-work","Photocatalyse","/fr/pages/tout-savoir-sur-la-photocatalyse","/pages/how-does-photocatalysis-work","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/all-about-particulate-matter-pm","Particules fines","/fr/pages/tout-savoir-sur-les-particules-fines-pm","/pages/all-about-particulate-matter-pm","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/all-you-need-to-know-about-volatile-organic-compounds-vocs","COV","/fr/pages/tout-ce-que-vous-devez-savoir-sur-les-composes-organiques-volatils-cov","/pages/all-you-need-to-know-about-volatile-organic-compounds-vocs","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/what-is-ground-level-ozone","Ozone troposphérique","/fr/pages/quest-ce-que-lozone-tropospherique","/pages/what-is-ground-level-ozone","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/what-is-chemical-pollution","Pollution chimique","/fr/pages/quest-ce-que-la-pollution-chimique","/pages/what-is-chemical-pollution","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/all-about-biological-pollution","Pollution biologique","/fr/pages/quest-ce-que-la-pollution-biologique","/pages/all-about-biological-pollution","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/air-quality-and-the-different-forms-of-air-pollution","Formes de pollution","/fr/pages/la-qualite-de-lair-et-les-differentes-formes-de-pollution-de-lair","/pages/air-quality-and-the-different-forms-of-air-pollution","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/the-new-who-air-quality-guidelines","Directives OMS","/fr/pages/les-nouvelles-directives-de-loms-sur-la-qualite-de-lair","/pages/the-new-who-air-quality-guidelines","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/respiratory-diseases-and-air-pollution","Maladies respiratoires","/fr/pages/maladies-respiratoires-et-pollution-de-lair","/pages/respiratory-diseases-and-air-pollution","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/can-air-purifiers-alleviate-asthma-symptoms","Asthme","/fr/pages/un-purificateur-dair-peut-il-soulager-les-symptomes-de-lasthme","/pages/can-air-purifiers-alleviate-asthma-symptoms","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/fight-against-respiratory-allergies-with-an-air-purifier","Allergies respiratoires","/fr/pages/luttez-contre-les-allergies-respiratoires-avec-un-purificateur-dair","/pages/fight-against-respiratory-allergies-with-an-air-purifier","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/using-an-air-purifier-to-fight-pollen-allergy","Allergie pollen","/fr/pages/utiliser-un-purificateur-dair-pour-lutter-contre-lallergie-au-pollen","/pages/using-an-air-purifier-to-fight-pollen-allergy","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/using-an-air-purifier-to-combat-airborne-germs","Germes en suspension","/fr/pages/utiliser-un-purificateur-dair-pour-lutter-contre-les-germes-en-suspension-dans-lair","/pages/using-an-air-purifier-to-combat-airborne-germs","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/how-to-use-air-purifiers-to-fight-allergies-to-dust-and-dustmites","Acariens et poussière","/fr/pages/comment-utiliser-les-purificateurs-dair-pour-lutter-contre-les-allergies-a-la-poussiere-e-aux-acariens","/pages/how-to-use-air-purifiers-to-fight-allergies-to-dust-and-dustmites","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/how-an-air-purifier-can-help-with-pet-allergies","Allergies animaux","/fr/pages/comment-un-purificateur-dair-peut-aider-avec-les-allergies-aux-animaux","/pages/how-an-air-purifier-can-help-with-pet-allergies","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/how-air-purifiers-can-protect-you-from-fine-particle-pollution","Particules fines","/fr/pages/comment-les-purificateurs-dair-peuvent-vous-proteger-de-la-pollution-par-les-particules-fines","/pages/how-air-purifiers-can-protect-you-from-fine-particle-pollution","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/using-an-air-purifier-to-protect-your-lungs-from-cigarette-smoke","Fumée de cigarette","/fr/pages/utiliser-un-purificateur-dair-pour-proteger-vos-poumons-de-la-fumee-de-cigarette","/pages/using-an-air-purifier-to-protect-your-lungs-from-cigarette-smoke","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/combatting-bad-odours-with-an-air-purifier","Mauvaises odeurs","/fr/pages/combattre-les-mauvaises-odeurs-avec-un-purificateur-dair","/pages/combatting-bad-odours-with-an-air-purifier","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/where-to-install-an-air-purifier","Où installer","/fr/pages/ou-installer-un-purificateur-dair","/pages/where-to-install-an-air-purifier","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/sleep-better-with-eoleaf","Mieux dormir","/fr/pages/dormez-mieux-en-installant-un-purificateur-dair-dans-votre-chambre","/pages/sleep-better-with-eoleaf","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/eoleafs-multi-layer-filtration-technology","Technologie multicouche","/fr/pages/la-technologie-de-filtration-multicouche-utilisee-par-eoleaf","/pages/eoleafs-multi-layer-filtration-technology","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/warranty-terms","Conditions de garantie","/fr/pages/conditions-garantie","/pages/warranty-terms","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/mould","Moisissures","/fr/pages/utiliser-un-purificateur-dair-pour-lutter-contre-les-moisissures","/pages/mould","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/wildfires-and-indoor-air-quality","Incendies de forêt","/fr/pages/acheter-un-purificateur-dair-pour-la-fumee-des-incendies-de-foret","/pages/wildfires-and-indoor-air-quality","301 vers la page FR",'A FAIRE'],
  ["/fr/pages/buying-an-air-purifier-in-belgium","Belgique","/fr/pages/acheter-un-purificateur-dair-en-belgique","/pages/buying-an-air-purifier-in-belgium","301 vers la page FR",'A FAIRE'],
  ["/fr/products/aeropro-40-airpurifier","Ancien modèle AEROPRO 40","/fr/products/purificateur-air-neopur-400","/products/neopur-400-air-purifier","301 vers la fiche NeoPur 400 : voir ticket Redirections AEROPRO",'A FAIRE'],
  ["/fr/products/aeropro-100-airpurifier","Ancien modèle AEROPRO 100","/fr/products/purificateur-air-terapur-600","/products/terapur-600-air-purifier","301 vers la fiche TeraPur 600 : voir ticket Redirections AEROPRO",'A FAIRE'],
  ["/fr/products/aeropro-150-airpurifier","Ancien modèle AEROPRO 150","/fr/products/purificateur-air-altapur-700","/products/altapur-700-air-purifier","301 vers la fiche AltaPur 700 : voir ticket Redirections AEROPRO",'A FAIRE'],
  ["/fr/products/replacement-uvc-lamp","Lampe UVC","/fr/products/lampe-uvc-rechange","/products/replacement-uvc-lamp","301 vers la page FR",'A FAIRE'],
 ])
