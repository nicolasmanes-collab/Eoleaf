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
    mois, date, titre, details, repartition, heures, _statut, livrable, intervenant, severite = t
    corps, critere = coupe(details)
    lib, _, url = livrable.partition("|") if livrable else ("", "", "")
    liv_html = (f'<span><a href="{E(url)}">{E(lib)}</a></span>' if url
                else '<span>livrable : pages HTML</span>')
    bloc_critere = (f'<p class="accept"><span class="lbl">Critère d\'acceptation</span>{E(critere)}</p>'
                    if critere else "")
    return f"""    <article class="ticket {CLASSE[severite]}">
      <div class="ticket-rail"><span class="ticket-num">{num:02d}</span><span class="ticket-bar"></span></div>
      <div class="ticket-body">
        <div class="ticket-head">
          <h3>{E(titre)}</h3>
          <span class="chip chip-sev">{CHIP[severite]}</span>
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
    <div class="figure"><dt>Clusters en cannibalisation</dt><dd>14</dd></div>
    <div class="figure"><dt>Pages EN sous /fr</dt><dd>36</dd></div>
    <div class="figure"><dt>Images · poids total</dt><dd>91,3 <span>Mo</span></dd></div>
    <div class="figure"><dt>Balises ALT vides</dt><dd>57 <span>% (192/334)</span></dd></div>
    <div class="figure"><dt>Volets jamais ouverts</dt><dd>4 <span>sur 7</span></dd></div>
  </dl>
</header>

<section>
  <h2>Ce qu'il faut trancher avant de croire un chiffre d'indexation</h2>
  <p class="section-note">Deux données du dossier se contredisent, et l'une des deux est fausse. Le dire maintenant coûte moins cher que de bâtir un trimestre de travail dessus.</p>

  <div class="caveat">
    <h3>L'extraction d'indexation du 20/05/2026 n'est pas exploitable en l'état</h3>
    <p>Elle classe environ 250 URL en « erreur client », dont des pages que l'onglet sémantique donne en position 4 à 8 sur leur requête cible — <code>acheter-un-purificateur-dair-de-qualite-medicale</code> en 7<sup>e</sup>, <code>ioniseurs-a-quoi-servent-ils</code> en 8<sup>e</sup>. Une page morte ne se classe pas. La cause la plus probable est un rejet Shopify sous la charge du crawl, pas un site cassé.</p>
    <p>Conséquence pratique : les 39 « pages indexées » relevées, la liste des orphelines et le décompte des erreurs sont tous à refaire. C'est le premier ticket du mois, et il conditionne la lecture des sept autres.</p>
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
