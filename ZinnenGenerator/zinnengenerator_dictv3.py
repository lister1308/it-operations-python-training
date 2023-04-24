# De thema's en combinaties die logisch zijn
themas = {
    "voorwerpen": ["meubels", "voertuigen", "plaatsen", "gebouwen"],
    "meubels": ["plaatsen", "gebouwen"],
    "mensen": ["meubels", "voertuigen", "plaatsen", "gebouwen"],
    "dieren": ["plaatsen", "gebouwen", "bomen", "planten","mensen"],
    "voertuigen": ["plaatsen", "gebouwen"],
    "plaatsen": ["gebouwen","plaatsen"],
    "gebouwen": ["plaatsen","gebouwen"],
    "bomen": ["plaatsen", "gebouwen"],
    "planten": ["meubels", "voertuigen", "plaatsen", "gebouwen"],
}

docenten = ["rudi","evert","obbert","henny"]

zelfstandige_naamwoorden = {
    "voorwerpen": ["telefoon", "sleutel", "sjaal", "zonnebril", "muts", "revolver"],
    "meubels": ["bank", "bureau", "kruk", "kast", "tafel", "bijzettafel","stoel","burostoel"],
    "mensen": ["Rudi","Evert","Henny","Obbert","vriend", "familie", "collega", "leraar", "politieagent", "vader","ouder","opa","oma","dochter","zoon","verpleegkundige", "chirurg", "helpdeskmedewerker", "systeembeheerder"],
    "dieren": ["hond", "kat", "konijn", "vogel", "rups", "kikker", "slang","tijger","olifant","bij"],
    "voertuigen": ["fiets", "auto", "bus", "trein", "e-bike", "vrachtwagen", "brandweerauto"],
    "plaatsen": ["park", "strand", "supermarkt", "ziekenhuis", "bos", "pretpark", "concertzaal"],
    "gebouwen": ["kasteel", "museum", "restaurant", "hotel", "vliegveld", "theater"],
    "bomen": ["eik", "beuk", "den", "esdoorn", "kastanje", "wilg"],
    "planten": ["cactus", "orchidee", "tulp", "varen", "klimop", "monstera", "duizendknoop", "lavendel"]
}

bijvoeglijke_naamwoorden = {
    "voorwerpen": ["roze", "glanzende", "oude", "duurzame","oude","donkere","gele","nieuwe"],
    "meubels": ["comfortabele", "moderne", "klassieke", "verstelbare", "lelijke"],
    "mensen": ["sympathieke", "slimme", "grappige", "aardige","vervelende","boze","vriendelijke","angstige","bezorgde","trotse","kalme","moedige","geduldige"],
    "dieren": ["schattige", "speelse", "lieve", "trouwe"],
    "voertuigen": ["snelle", "efficiënte", "ruime", "luxueuze", "elektrische"],
    "plaatsen": ["drukke", "schone", "gezellige", "veilige"],
    "gebouwen": ["romantische", "chique", "historische", "unieke"],
    "bomen": ["grote", "oude", "mooie", "geurende"],
    "planten": ["groene", "bonte", "gezonde", "kleurrijke", "geurige"]
}

#Werkwoorden in enkelvoudige persoonsvorm in de vorm Hij/Zij/Het met bijpassen voorzetsels.
werkwoorden = {
    "voorwerpen": {
        "ligt": ["op", "onder", "tussen", "langs", "tegen"],
        "verdwijnt": ["in", "achter", "onder"],
        "staat": ["op", "onder", "naast", "tegen", "tussen"],
        "glijdt": ["in", "onder", "langs", "tegen", "tussen"],
        "valt": ["op","in","onder","tegen","tussen"],
        "zweeft": ["onder","over"]
    },
    "meubels": {
        "staat": ["in", "op", "onder", "tegen", "tussen"],
        "verdwijnt": ["in", "achter", "onder"],
        "ligt": ["in", "op", "onder", "tegen", "tussen"]
    },
    "mensen": {
        "staat": ["in", "op", "tegen", "voor", "achter"],
        "verdwijnt": ["in", "achter", "onder"],
        "ligt": ["op", "onder", "tegen", "naast"],
        "danst": ["in", "op", "tegen", "voor", "achter"],
        "vecht": ["in", "op", "tegen", "voor", "achter"],
        "loopt": ["in","tegen","voor"],
        "kruipt": ["in","over"],
        "zit": ["in"]
    },
    "dieren": {
        "kijkt": ["naar", "op", "over", "tegen", "voor"],
        "springt": ["op", "over", "tegen", "voor", "achter"],
        "ligt": ["naast", "op", "onder", "tegen", "voor"],
        "loopt": ["richting", "naar", "langs", "tegen", "voor"],
        "krabbelt": ["aan","onder"],
        "likt": ["aan"]
    },
    "voertuigen": {
        "rijdt": ["naar","om","langs"],
        "staat": ["in", "op", "tegen", "tussen"],
        "verdwijnt": ["in", "achter", "onder"],
        "ligt": ["in", "op", "onder", "tegen", "tussen"]
    },
    "plaatsen": {
        "ligt": ["naast"]
    },
    "gebouwen": {
        "staat": ["in", "bij", "op", "onder", "tegen"],
        "verdwijnt": ["in", "achter", "onder"],
        "ligt": ["in", "bij", "op", "onder", "tegen"]
    },
    "bomen": {
        "staat": ["bij", "op", "onder", "tegen", "naast"],
        "verdwijnt": ["in", "achter", "onder"],
        "ligt": ["in", "op", "onder", "tegen", "naast"]
    },
    "planten": {
        "staat": ["in", "op", "onder", "tegen", "tussen"],
        "verdwijnt": ["in", "achter", "onder"],
        "ligt": ["in", "op", "onder", "tegen", "tussen"],
        "bloeit": ["in","over"],
        "groeit": ["in","over","onder"]
    }
}
