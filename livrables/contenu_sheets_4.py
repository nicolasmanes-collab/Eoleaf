# -*- coding: utf-8 -*-
"""Contenu des Sheets de travail Eoleaf - liens sortants, maillage, geo, comparatifs."""
FICHIERS = {}

FICHIERS["Liens sortants a remplacer Eoleaf"] = (
 "Important ⚠️ : environ 200 liens sortants ne répondent plus sur l'ensemble du site. Sur des pages qui "
 "citent des sources scientifiques, un lien mort abîme le signal de fiabilité. Les pages FR sont "
 "traitées d'abord ; chaque erreur étant répliquée sur les 12 langues, une correction en français se "
 "propage. Cinquante URL sont invalides dès la saisie (http://., http://ozone).",
 ["PAGE FR","LIEN SORTANT ROMPU","CODE","SOURCE DE REMPLACEMENT PROPOSEE","STATUT"],
 [
  ["/fr/pages/comment-fonctionnent-les-filtres-hepa","cdc.gov/niosh/docs/96-101/default.html","404","Fiche NIOSH actuelle sur les respirateurs et filtres, ou norme EN 1822 pour la classification HEPA",'A FAIRE'],
  ["/fr/pages/tout-ce-que-vous-devez-savoir-sur-les-composes-organiques-volatils-cov","apis.ac.uk/overview/pollutants/overview_vocs.htm","404","Page COV de l'Agence européenne pour l'environnement, ou fiche ANSES",'A FAIRE'],
  ["/fr/pages/quest-ce-que-lozone-tropospherique","cdc.gov/niosh/topics/ozone/default.html","404","Fiche ozone de l'OMS ou de l'Agence européenne pour l'environnement",'A FAIRE'],
  ["/fr/pages/les-differences-entre-les-purificateurs-dair-et-les-humidificateurs","sleepopolis.com/education/how-does-a-humidifier-work/","404","Source institutionnelle plutôt qu'un site affilié : fiche humidité intérieure de l'ANSES",'A FAIRE'],
  ["/fr/pages/les-differences-entre-un-purificateur-dair-et-un-climatiseur","homeairguides.com/air-purifier-vs-air-conditioner/","404","Fiche ADEME sur la qualité de l'air intérieur et la climatisation",'A FAIRE'],
  ["/fr/pages/purificateurs-dair-eoleaf-vs-winix","winixamerica.com/2019/08/07/hr900-ultimate-pet-air-purifier/","404","Fiche produit Winix actuelle, ou retirer le lien vers le concurrent",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-en-belgique","prb.org/international/indicator/urban/snapshot","404","Données d'urbanisation de la Banque mondiale ou d'Eurostat",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-au-luxembourg","prb.org/international/indicator/urban/snapshot","404","Idem",'A FAIRE'],
  ["/fr/pages/protegez-vos-enfants-de-la-pollution-de-lair-interieur","airpurifiers.com/6-ways-to-protect-children-from-air-pollution/","404","Rapport OMS sur la pollution de l'air et la santé des enfants",'A FAIRE'],
  ["/fr/pages/oxydes-dazote-dans-la-pollution-de-lair-risques-pour-la-sante...","doi.org/10.1590/1414-431X2015439","404","Vérifier le DOI : s'il est valide, corriger la saisie ; sinon, citer une étude équivalente",'A FAIRE'],
  ["/fr/pages/dormez-mieux-en-installant-un-purificateur-dair-dans-votre-chambre","stallergenesgreer.com/uk/what-respiratory-allergy","404","Fiche allergies respiratoires de l'Assurance maladie ou de l'INSERM",'A FAIRE'],
  ["/fr/pages/installer-un-capteur-de-co2-dans-votre-maison...","workinmind.org/2018/12/05/une-etude-reveals-c02-levels...","404","URL manifestement corrompue : retrouver l'étude d'origine sur le CO2 en bureau ou la retirer",'A FAIRE'],
  ["/fr/pages/purificateurs-dair-a-lozone-et-generateurs-dozone-ce-quil-faut-savoir","eea.europa.eu/help/glossary/eea-glossary/ozone-depleting-substance","410","Glossaire actuel de l'Agence européenne pour l'environnement",'A FAIRE'],
  ["/fr/pages/tout-savoir-sur-les-particules-fines-pm","eea.europa.eu/themes/air/urban-air-quality","410","Page qualité de l'air urbain actuelle de l'AEE",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-pour-un-restaurant","nateosante.com/en/business-solutions/...","503","Lien vers un concurrent direct : à retirer, pas à remplacer",'A FAIRE'],
  ["/fr/pages/tout-savoir-sur-la-sterilisation-uvc","http://ozone","URL invalide","Saisie tronquée : retrouver la source visée ou retirer le lien",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-pour-la-toux","http://.","URL invalide","Saisie vide : retirer le lien",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-pour-les-odeurs","ehp.niehs.nih.gov/doi/10.1289/ehp.1510037","Inaccessible","Vérifier l'accès : la revue peut bloquer les robots. Si l'article existe, conserver le lien",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-contre-le-vapotage","factor.niehs.nih.gov/2022/2/feature/3-feature-e-cigarettes-and-toxic-metals","Inaccessible","Idem : vérifier avant de remplacer",'A FAIRE'],
  ["/fr/pages/la-qualite-de-lair-et-les-differentes-formes-de-pollution-de-lair","particuliers.promotelec.com/fiche-habitat/qualite-de-lair-interieur...","Inaccessible","Fiche qualité de l'air intérieur de l'ADEME",'A FAIRE'],
  ["","","","",""],
  ["METHODE","Corriger la source dans la page FR, puis répliquer la correction sur les 11 autres langues : le même lien mort y figure","","",""],
  ["REGLE","Un lien vers un concurrent direct (Nateosante, Winix) se retire, il ne se remplace pas","","",""],
  ["PRIORITE","Les pages portant des impressions d'abord : voir les positions de l'onglet sémantique","","",""],
 ])

FICHIERS["Plan de maillage Eoleaf"] = (
 "Important ⚠️ : le maillage interne distribue l'autorité et guide le visiteur vers la page qui vend. "
 "Le volet n'a jamais été produit : la quarantaine de pages métier « acheter-un-purificateur-dair-pour-* » "
 "n'est pas câblée vers les fiches produit. Règle : chaque page reçoit un lien de sa mère, lie ses filles "
 "et 2 à 3 sœurs du même silo. Ancre en exact match, contiguë, jamais « voir la sélection ».",
 ["SOURCE","DESTINATION","ANCRE PROPOSEE","TYPE DE LIEN","DEJA POSE","STATUT"],
 [
  ["/fr/pages/acheter-un-purificateur-dair-hepa","/fr/products/purificateur-air-altapur-700","purificateur d'air AltaPur 700","Pilier vers unité d'achat","À vérifier",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-professionnel","/fr/collections/purificateurs-air","purificateurs d'air professionnels","Pilier vers catégorie","À vérifier",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-pour-la-voiture","/fr/products/purificateur-air-purcar","purificateur d'air PurCar","Pilier vers unité d'achat","À vérifier",'A FAIRE'],
  ["/fr/pages/acheter-un-purificateur-dair-de-qualite-medicale","/fr/products/purificateur-air-terapur-600","purificateur d'air TeraPur 600","Pilier vers unité d'achat","À vérifier",'A FAIRE'],
  ["/fr/pages/comment-fonctionnent-les-filtres-hepa","/fr/pages/acheter-un-purificateur-dair-hepa","acheter un purificateur d'air HEPA","Question vers pilier","À vérifier",'A FAIRE'],
  ["/fr/pages/tout-savoir-sur-lionisation","/fr/collections/purificateurs-air","purificateurs d'air professionnels","Question vers catégorie","À vérifier",'A FAIRE'],
  ["/fr/pages/guide-dachat-comment-choisir-un-purificateur-dair","/fr/pages/comparatif-produit","comparatif des purificateurs d'air Eoleaf","Guide vers comparatif","À vérifier",'A FAIRE'],
  ["/fr/collections/purificateurs-air","/fr/pages/guide-dachat-comment-choisir-un-purificateur-dair","comment choisir un purificateur d'air","Catégorie vers guide","À vérifier",'A FAIRE'],
  ["/fr/pages/qualite-de-lair-a-lyon","/fr/pages/acheter-un-purificateur-dair-professionnel","purificateur d'air professionnel","Géo vers pilier","À vérifier",'A FAIRE'],
  ["/fr/pages/purificateurs-dair-levoit-vs-eoleaf","/fr/products/purificateur-air-neopur-400","purificateur d'air NeoPur 400","Comparatif vers unité d'achat","À vérifier",'A FAIRE'],
  ["","","","","",""],
  ["A PRODUIRE AVANT DE REMPLIR","","","","",""],
  ["1","Carte XMind des silos, à partir du cocon sémantique existant (app.xmind.com/nAIkleML)","","","",'A FAIRE'],
  ["2","Relevé des liens internes déjà posés : sans ce contrôle, une partie du plan est du travail fantôme","","","",'A FAIRE'],
  ["3","Score de page interne actuel contre cible, pour savoir si un lien de plus sert à quelque chose","","","",'A FAIRE'],
  ["","","","","",""],
  ["REGLES D'ANCRE","L'expression cible reste contiguë : « purificateur d'air HEPA », pas « purificateur (…) HEPA »","","","",""],
  ["","Un jeu d'ancres qui tourne par cible, jamais la même ancre partout","","","",""],
  ["","Pas de lien inter-silo hors navigation","","","",""],
  ["","Un lien contextuel haut dans la page vaut plus qu'un lien de pied de page","","","",""],
 ])

FICHIERS["Profondeur et orphelines Eoleaf"] = (
 "Important ⚠️ : une page d'achat à plus de 3 clics de l'accueil ne reçoit pas d'autorité et ne se trouve "
 "pas. Une page orpheline, sans aucun lien interne entrant, est invisible pour les robots. L'onglet "
 "Pages orphelines de l'extraction indexation est resté vide : à remplir au re-crawl du ticket 01.",
 ["BLOC","NIVEAU OU URL","NOMBRE DE PAGES","DONT PAGES D'ACHAT","IMPRESSIONS 90 J","ACTION","STATUT"],
 [
  ["Distribution par niveau","Niveau 0 (accueil)","","","","",'A FAIRE'],
  ["Distribution par niveau","Niveau 1","","","","",'A FAIRE'],
  ["Distribution par niveau","Niveau 2","","","","",'A FAIRE'],
  ["Distribution par niveau","Niveau 3","","","","",'A FAIRE'],
  ["Distribution par niveau","Niveau 4 et au-delà","","","","Toute page d'achat ici est un ticket",'A FAIRE'],
  ["","","","","","",""],
  ["Pages d'achat trop profondes","À lister au re-crawl","","","","Remonter par un lien depuis la catégorie ou le pilier de silo",'A FAIRE'],
  ["","","","","","",""],
  ["Orphelines avec impressions","À lister au re-crawl","","","","Perte sèche : recevoir un lien interne depuis sa mère",'A FAIRE'],
  ["Orphelines sans impression","À lister au re-crawl","","","","Candidate à la fusion dans son pilier de cluster",'A FAIRE'],
  ["","","","","","",""],
  ["METHODE","Croiser le crawl (liens entrants = 0) avec les pages du sitemap ET les pages à impressions GSC","","","","",""],
  ["","Une page présente au sitemap mais sans lien interne est orpheline, même si elle répond 200","","","","",""],
 ])

FICHIERS["Pages geo villes Eoleaf"] = (
 "Important ⚠️ : quatre pages ville existent et deux portent déjà du trafic (Lyon en position 6, Paris en "
 "18). Cette couche géo n'est pas structurée : pas de gabarit commun, pas de lien vers l'unité d'achat, "
 "pas de LocalBusiness. C'est une couche à industrialiser ou à assumer comme éditoriale, pas à laisser "
 "au milieu du gué.",
 ["VILLE","URL","REQUETE CIBLE","VOLUME","POSITION","LIEN VERS UNITE D'ACHAT","GABARIT COMMUN","ACTION","STATUT"],
 [
  ["Lyon","/fr/pages/qualite-de-lair-a-lyon","qualité de l air lyon","480","6","À vérifier","Non","Poser le lien vers le pilier professionnel, mesurer avant d'étendre",'A FAIRE'],
  ["Paris","/fr/pages/qualite-de-lair-a-paris-idees-solutions-et-astuces-pour-respirer-un-air-sain","murs anti-pollution urbaine paris","1300","18","À vérifier","Non","Slug trop long : raccourcir avec 301, puis mêmes modules que Lyon",'A FAIRE'],
  ["Lille","/fr/pages/qualite-de-lair-a-lille","qualité de l'air lille","Non relevé","Non relevée","À vérifier","Non","Aligner sur le gabarit une fois défini",'A FAIRE'],
  ["Londres","/fr/pages/qualie-de-lair-a-londres-informations-solutions-et-conseils-pour-un-air-plus-sain","smog de londres","170","16","À vérifier","Non","Faute de frappe dans le slug (« qualie ») : corriger avec 301",'A FAIRE'],
  ["Paris (EN)","/pages/air-quality-in-paris-ideas-solutions-and-tips-for-clean-air","air pollution in paris france","260","7","À vérifier","Non","Version EN performante : aligner sur le même gabarit",'A FAIRE'],
  ["","","","","","","","",""],
  ["A TRANCHER","Cette couche géo est-elle un axe d'acquisition ou une vitrine éditoriale ?","","","","","","",""],
  ["Si axe d'acquisition","Un gabarit commun, un lien vers l'unité d'achat, un JSON-LD LocalBusiness si Eoleaf a une présence physique, et une extension aux villes à volume","","","","","","",""],
  ["Si vitrine éditoriale","Les 4 pages restent, on corrige les slugs et on les câble au pilier, sans en créer d'autres","","","","","","",""],
  ["POINT DE VIGILANCE","Les slugs de Paris et Londres portent une phrase entière, dont une faute de frappe : à corriger avec 301, pas en place","","","","","","",""],
 ])

FICHIERS["Comparatifs concurrents Eoleaf"] = (
 "Important ⚠️ : onze pages comparent Eoleaf à un concurrent. Ce sont des pages à forte intention "
 "d'achat : le visiteur compare avant de commander. Elles doivent porter un tableau de comparaison "
 "chiffré, une preuve vérifiable et un lien vers la fiche produit. Aucune ne ressort indexée au crawl du "
 "20/05, à confirmer au re-crawl.",
 ["CONCURRENT","URL","REQUETE CIBLE","VOLUME","POSITION","TABLEAU COMPARATIF","LIEN VERS FICHE PRODUIT","ACTION","STATUT"],
 [
  ["Levoit","/fr/pages/purificateurs-dair-levoit-vs-eoleaf","levoit purificateur d air","390","20","À vérifier","À vérifier","Position 20 sur 390 de volume : le premier comparatif à travailler",'A FAIRE'],
  ["Dyson Big+Quiet","/fr/blogs/blog/le-nouveau-dyson-big-quiet-laisse-encore-a-desirer","dyson big quiet","210","5","À vérifier","À vérifier","Déjà en position 5 : ne pas toucher le fond, poser le lien produit",'A FAIRE'],
  ["Dyson chauffant","/fr/pages/les-purificateurs-dair-avec-fonction-de-chauffage-fonctionnent-ils","dyson chauffant","1900","9","À vérifier","À vérifier","1900 de volume en position 9 : fort potentiel",'A FAIRE'],
  ["Dyson Hot+Cool","/fr/pages/purificateurs-dair-eoleaf-vs-dyson-hot-cool-comment-se-comparent-ils","dyson hot cool avis","Non relevé","Non relevée","À vérifier","À vérifier","Aligner sur le gabarit comparatif",'A FAIRE'],
  ["Coway Airmega","/fr/pages/purificateur-dair-terapur-600-deoleaf-vs-coway-airmega-mighty-lequel-vous-faut-il","coway airmega avis","Non relevé","Non relevée","À vérifier","Lien rompu relevé","Corriger le lien mort vers la fiche AltaPur 700",'A FAIRE'],
  ["Shark","/fr/pages/purificateur-d-air-shark-ou-altapur-700-d-eoleaf","purificateur d'air shark","Non relevé","Non relevée","À vérifier","Lien rompu relevé","Corriger le lien mort vers la fiche AltaPur 700",'A FAIRE'],
  ["Winix","/fr/pages/purificateurs-dair-eoleaf-vs-winix","winix purificateur avis","Non relevé","Non relevée","À vérifier","À vérifier","Lien sortant vers Winix rompu : le retirer",'A FAIRE'],
  ["Blueair","/fr/pages/purificateurs-dair-eoleaf-vs-blueair","blueair avis","Non relevé","Non relevée","À vérifier","À vérifier","Aligner sur le gabarit comparatif",'A FAIRE'],
  ["IQAir","/fr/pages/purificateurs-dair-eoleaf-vs-iqair","iqair avis","Non relevé","Non relevée","À vérifier","À vérifier","Aligner sur le gabarit comparatif",'A FAIRE'],
  ["Philips","/fr/pages/purificateurs-dair-eoleaf-vs-philips","philips purificateur avis","Non relevé","Non relevée","À vérifier","À vérifier","Aligner sur le gabarit comparatif",'A FAIRE'],
  ["Vax","/fr/pages/purificateur-dair-vax-vs-eoleaf","vax purificateur","Non relevé","Non relevée","À vérifier","À vérifier","Portait deux H1, corrigé le 24/08",'A FAIRE'],
  ["Airvia Medical","/fr/pages/qu-est-il-arrive-a-airvia-medical","airvia medical","Non relevé","Non relevée","Sans objet","À vérifier","Page de marque liée à l'historique produit : à conserver telle quelle",'A FAIRE'],
  ["Airvia Medical (SAV)","/fr/pages/reparation-purificateur-dair-airvia-medical-eoleaf","réparation airvia medical","Non relevé","Non relevée","Sans objet","À vérifier","Intention SAV, pas comparatif : lier vers le formulaire SAV",'A FAIRE'],
  ["","","","","","","","",""],
  ["MODULES ATTENDUS SUR CE GABARIT","","","","","","","",""],
  ["Tableau de comparaison","Surface couverte, débit, classe de filtration, niveau sonore, coût du filtre par an, garantie","","","","","","",""],
  ["Preuve","Le test indépendant Eoleaf existe déjà : le citer et le lier sur chaque comparatif","","","","","","",""],
  ["Mention honnête","Dire au moins un point où le concurrent est meilleur : c'est ce qui rend le reste crédible","","","","","","",""],
  ["Lien de sortie","Un lien vers la fiche produit du modèle Eoleaf comparé, ancre en exact match","","","","","","",""],
 ])
