https://www.cursusburo.nl/course/traineeship-operations/lessons/teamopdracht-onze-eigen-zinnengenerator/

Teamopdracht “Onze eigen zinnengenerator”
In deze opdracht maken we een zinnengenerator die alinea’s met betekenisvolle zinnen kan genereren. Hiertoe maken de deelnemers ieder een functie die een deel van een zin kan genereren en maakt het team samen functies om zinnen en alinea’s samen te stellen.

Onderdelen van een zin
Een Nederlandse volzin kan kan op verschillende manieren worden samengesteld. De genootschap Onze Taal doet hierover een boekje open. Voor deze opdracht nemen we echter genoegen met vaste zinsconstructies:

<zin> :== <onderwerp> <werkwoord> “.” | <onderwerp> <werkwoord> <koppelwoord> <lijdend_voorwerp> “.”
<onderwerp> :== <lidwoord> <zelfstandig_naamwoord> | <lidwoord> <bijvoegelijk_naamwoord> <zelfstandig_naamwoord>
<lijdend_voorwerp> :== <onderwerp>
<koppelwoord> :== “op” | “in” | “voor” | “onder” | …
<lidwoord> :== “de” | “het” | “een”
<zelfstandig_naamwoord> :== “glas” | “pen” | “netwerkkabel” | …
<bijvoegelijk_naamwoord> :== “blauwe” | “grote” | “volle” | …
<werkwoord> :== “staat” | “zit” | “ligt” | …
Voorbeelden
De pen ligt
De pen staat in het glas
De netwerkkabel ligt onder de pen
Het volle glas staat op de grote ronde tafel
Alinea’s
Meerdere zinnen met een bepaalde samenhang vormen samen een alinea:

<alinea> :== <zin> | <zin> <zin> | <zin> <zin> <zin> | …
De samenhang wordt veroorzaakt doordat de zinnen in een alinea naar elkaar verwijzen, over het zelfde onderwerp verhalen of overeenkomstige onderwerpen bevatten. Deze samenhang wordt in te realiseren programma bestuurd met de parameter samenhang.

Programmabeschrijving
Elk van de in de taalconstructie beschreven elementen wordt in een eigen functie gevat. Elk van de functies zitten in een module (de deelnemers kunnen zelf bepalen of er één of meerdere modules worden gebruikt). De volgende functies worden verondersteld ontwikkeld te worden:

function lidwoord()
function zelfstandig_naamwoord(thema = None)
function lijdend_voorwerp(thema = None)
function bijvoegelijk_naamwoord(thema = None)
function koppelwoord()
function werkwoord(thema = None)
function volzin()
function alinea(samenhang = 0)
Het thema kan één van de volgende zijn: voorwerpen, meubels, mensen, dieren, voertuigen, plaatsen, gebouwen, bomen, planten en mag naar eigen inzicht worden uitgebreid.

Elk van de functies levert een random string terug. Functies met een parameter thema kunnen met of zonder thema worden aangeroepen. Zonder thema wordt een random string over alle thema’s heen teruggegeven, met een opgegeven (bestaand) thema wordt een random string van alleen dat thema teruggegeven.

Voor de dataopslag van de functies wordt de volgende datastructuur gesuggereerd:

{thema: lijst}

Voorbeelden
{
  "voorwerpen": ["glas", "pen", "netwerkkabel"],
  "meubels": ["tafel", "stoel", "kapstok"]
}
Met de parameter samenhang in de functie alinea wordt bedoeld, de mate waarin een onderwerp in de volgende zin herhaald wordt. Met 0 is er geen herhaling, met 1 wordt een gebruikt lijdend voorwerp in de volgende zin als onderwerp gebruikt, enzovoorts.

Voorbeelden
Het volle glas staat op de tafel. De kat loopt door de kamer. (samenhang 0)
Het volle glas staat op de tafel. De tafel staat in de kamer. (samenhang 1)
Beoordeling
Jip-en-Janneketaal – 6%
Hoofdletters en interpunctie (inclusief zinafsluitende punten) – 16%
Juiste zinsconstructie – 26%
Logische alinea’s – 10%
Fun en X-factor – 42%
