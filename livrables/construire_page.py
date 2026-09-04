# -*- coding: utf-8 -*-
"""Compose la page de roadmap a partir de donnees_roadmap.py.

Le CSS vit dans page_entete.html ; le contenu est genere, pour que la page
et le classeur ne puissent pas divorcer.
"""
import os, sys, html
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from donnees_roadmap import SEPTEMBRE, OCTOBRE, NOVEMBRE, CONSTATS

E = lambda s: html.escape(str(s), quote=True)
CHIP = {"bloque": "Bloque la vente", "freine": "Freine la page", "crawl": "Budget de crawl"}
CLASSE = {"bloque": "sev-block", "freine": "sev-slow", "crawl": "sev-crawl"}


def coupe(details):
    """Separe le corps du ticket de son critere d'acceptation."""
    marqueur = "Fini quand :"
    if marqueur in details:
        corps, _, critere = details.partition(marqueur)
        return corps.strip(), critere.strip()
    return details.strip(), ""


def ticket(num, t):
    mois, date, titre, details, repartition, heures, statut, livrable, intervenant, severite = t
    corps, critere = coupe(details)
    lib, _, url = livrable.partition("|") if livrable else ("", "", "")
    liv_html = (f'<span><a href="{E(url)}">{E(lib)}</a></span>' if url
                else '<span>livrable : pages HTML</span>')
    bloc_critere = (f'<p class="accept"><span class="lbl">Critère d\'acceptation</span>{E(critere)}</p>'
                    if critere else "")
    fini = ' <span class="chip chip-done">Terminé</span>' if statut == "TERMINE" else ""
    return f"""    <article class="ticket {CLASSE[severite]}{' is-done' if statut == 'TERMINE' else ''}">
      <div class="ticket-rail"><span class="ticket-num">{num:02d}</span><span class="ticket-bar"></span></div>
      <div class="ticket-body">
        <div class="ticket-head">
          <h3>{E(titre)}</h3>
          <span class="chip chip-sev">{CHIP[severite]}</span>{fini}
        </div>
        <p>{E(corps)}</p>
        {bloc_critere}
        <p class="meta"><span><b>{E(date[:5])}</b></span><span>{E(repartition.title())} · {E(intervenant)}</span><span><b>{heures:g} h</b></span>{liv_html}</p>
      </div>
    </article>"""


def rang_backlog(t):
    mois, date, titre, details, _r, heures, _s, livrable, _i, severite = t
    corps, _ = coupe(details)
    resume = corps.split(". ")[1] if ". " in corps else corps
    lib, _, url = livrable.partition("|") if livrable else ("", "", "")
    cell = f'<a href="{E(url)}">{E(lib)}</a>' if url else "pages HTML"
    return (f'        <tr><td class="mois">{E(mois[:3])} · {E(date[:2])}</td>'
            f'<td>{E(titre)}</td><td>{E(resume[:190])}</td>'
            f'<td>{cell}</td><td class="num">{heures:g} h</td></tr>')


def constat(c):
    volet, mesure, valeur, implique = c
    return (f'        <tr><td class="mois">{E(volet)}</td><td>{E(mesure)}</td>'
            f'<td class="num">{E(valeur)}</td><td>{E(implique)}</td></tr>')


def main():
    entete = open(os.path.join(ICI, "page_entete.html"), encoding="utf-8").read()
    h_sept = sum(t[5] for t in SEPTEMBRE)
    h_back = sum(t[5] for t in OCTOBRE + NOVEMBRE)
    tickets = "\n".join(ticket(i, t) for i, t in enumerate(SEPTEMBRE, start=1))
    backlog = "\n".join(rang_backlog(t) for t in OCTOBRE + NOVEMBRE)
    constats = "\n".join(constat(c) for c in CONSTATS)

    page = f"""<title>Roadmap technique Eoleaf</title>
{entete}

<div class="wrap">

<header class="masthead">
  <p class="eyebrow">Eoleaf · SEO Monkey · établie le 4 septembre 2026</p>
  <h1>Roadmap technique de septembre</h1>
  <p class="standfirst">Vingt-et-un chantiers ouverts, dont <strong>huit en septembre</strong> pour {h_sept:g} heures estimées, dans leur ordre d'exécution. L'ordre n'est pas décoratif : ce qui empêche une page de vendre passe avant ce qui la freine, et le budget de crawl vient en dernier. Chaque ticket porte son Sheet de travail, avec les URL, les valeurs relevées et les corrections déjà rédigées.</p>

  <dl class="figures">
    <div class="figure"><dt>Pages indexées · GSC 90 j</dt><dd>2 994</dd></div>
    <div class="figure"><dt>Clics hors français</dt><dd>79 <span>%</span></dd></div>
    <div class="figure"><dt>Clusters en cannibalisation</dt><dd>14</dd></div>
    <div class="figure"><dt>Pages EN sous /fr</dt><dd>36</dd></div>
    <div class="figure"><dt>Balises ALT vides</dt><dd>57 <span>% (192/334)</span></dd></div>
  </dl>
</header>

<section>
  <h2>Ce que la Search Console a tranché, le 4 septembre</h2>
  <p class="section-note">Deux données du dossier se contredisaient. La Search Console dit laquelle était fausse, et trois tickets en sortent modifiés.</p>

  <div class="caveat caveat-ok">
    <h3>Le crawl du 20/05/2026 était faux : le site est massivement indexé</h3>
    <p>Il déclarait 39 pages indexées et environ 250 URL en « erreur client ». La Search Console compte <strong>2 994 pages portant au moins une impression</strong> sur les 90 derniers jours, pour 28 889 clics et 3,77 M d'impressions. Les dix URL témoin ressortent toutes en « Envoyée et indexée », robots.txt autorisé, page récupérée avec succès, dernier passage de Google entre le 22 août et le 4 septembre. Y compris les six que le crawl donnait mortes.</p>
    <p>C'était bien un rejet Shopify sous la charge du crawl. Le re-crawl outillé reste à passer pour reconstituer profondeur, orphelines et liens internes — il ne peut pas se faire depuis cet environnement, eoleaf.com y étant bloqué — mais plus aucune décision n'attend ce chiffre.</p>
  </div>

  <div class="asks" style="margin-top:16px">
    <div class="ask">
      <h3>Le contact n'était pas cassé</h3>
      <p>Les pages contact FR, EN et DE sont indexées et saines. La FR est même en position 2,2 avec 477 impressions. Seule <code>/fr/pages/formulaire-apres-vente</code> est réellement morte, et la FAQ y renvoie. Le ticket tombe de 2 h à 30 min.</p>
    </div>
    <div class="ask">
      <h3>La fiche produit a déjà son JSON-LD</h3>
      <p>Google y détecte Product, Offer et AggregateRating, verdict PASS, avec extraits de produit, fiche de marchand et extraits d'avis. Le gabarit qui encaisse est équipé : le ticket ne porte plus que l'accueil, la catégorie, les pages métier et la FAQ.</p>
    </div>
    <div class="ask">
      <h3>Le français n'est pas le sujet principal</h3>
      <p>284 pages FR pour 6 106 clics, soit 21 % du total. Les onze autres langues en portent 79 %, et la page la plus cliquée du site est allemande — <code>kauf-eines-luftreinigers-fur-cannabis</code>, 928 clics. La priorisation par langue est à revoir avec Eoleaf.</p>
    </div>
  </div>
</section>

<section>
  <h2>Les huit chantiers de septembre</h2>
  <p class="section-note">La barre de couleur à gauche indique la nature du blocage : rouge, la page ne peut pas vendre ; ambre, elle vend moins bien qu'elle ne devrait ; bleu, du budget de crawl part en fumée. Le lien en bas de chaque ticket ouvre son Sheet de travail.</p>

  <div class="tickets">

{tickets}

  </div>
</section>

<section>
  <h2>Ce qui attend en octobre et novembre</h2>
  <p class="section-note">Treize chantiers, {h_back:g} heures estimées. Leur Sheet de travail existe déjà : ils sont prêts à démarrer, seule la place dans le mois manque.</p>
  <div class="scroller">
    <table>
      <caption>Quatre volets du process n'ont jamais été ouverts depuis le début de l'accompagnement : hreflang, vitesse, JSON-LD et maillage interne.</caption>
      <thead>
        <tr><th scope="col">Mois</th><th scope="col">Chantier</th><th scope="col">Ce qui manque aujourd'hui</th><th scope="col">Livrable</th><th scope="col">Est.</th></tr>
      </thead>
      <tbody>
{backlog}
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Les chiffres qui fondent la roadmap</h2>
  <p class="section-note">Tous relevés dans les extractions du Drive, le fichier H1 du 24 août ou l'onglet sémantique. Aucun n'est estimé.</p>
  <div class="scroller">
    <table>
      <thead>
        <tr><th scope="col">Volet</th><th scope="col">Ce qui est mesuré</th><th scope="col">Valeur</th><th scope="col">Ce que cela implique</th></tr>
      </thead>
      <tbody>
{constats}
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Trois choses à confirmer</h2>
  <p class="section-note">Les heures sont des estimations d'effort, pas des engagements contractuels.</p>
  <div class="asks">
    <div class="ask">
      <h3>Le volume d'heures du mois</h3>
      <p>Septembre est calé sur huit lignes pour {h_sept:g} heures. Le volume contractuel mensuel n'est pas dans le dossier : s'il est inférieur, les tickets 07 et 08 basculent en octobre — ce sont les deux dont le report coûte le moins.</p>
    </div>
    <div class="ask">
      <h3>L'accès au site pour vérifier</h3>
      <p>eoleaf.com est injoignable depuis l'environnement de travail, bloqué par la politique réseau de la session. Tous les constats viennent des extractions du Drive, dont la plus récente date du 24 août. L'état actuel des corrections de juillet et août n'a pas pu être revérifié en direct.</p>
    </div>
    <div class="ask">
      <h3>La Search Console</h3>
      <p>Le ticket 01 en dépend, et la priorisation par clics 90 jours comme le relevé des orphelines aussi. Aucun accès GSC n'est disponible ici.</p>
    </div>
  </div>
</section>

<footer>
  <span>Eoleaf · profil ECOM · Shopify, 12 langues</span>
  <span>Roadmap établie le 04/09/2026</span>
  <span>21 tickets · {h_sept + h_back:g} heures estimées</span>
  <span>Sheets de travail rangés dans « 2 - Technique / 5 - Mois 5 (septembre) »</span>
</footer>

</div>
"""
    chemin = os.path.join(ICI, "roadmap-septembre.html")
    open(chemin, "w", encoding="utf-8").write(page)
    print(f"page : {chemin} ({len(page)} caracteres)")


if __name__ == "__main__":
    main()
