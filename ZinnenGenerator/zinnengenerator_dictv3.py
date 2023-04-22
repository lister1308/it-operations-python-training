# De thema's en combinaties die logisch zijn
themas = {
    "voorwerpen": ["meubels", "voertuigen", "plaatsen", "gebouwen"],
    "meubels": ["plaatsen", "gebouwen"],
    "mensen": ["meubels", "voertuigen", "plaatsen", "gebouwen"],
    "dieren": ["plaatsen", "gebouwen", "bomen", "planten"],
    "voertuigen": ["plaatsen", "gebouwen"],
    "plaatsen": ["plaatsen"],
    "gebouwen": ["plaatsen"],
    "bomen": ["plaatsen", "gebouwen"],
    "planten": ["meubels", "voertuigen", "plaatsen", "gebouwen"],
}

zelfstandige_naamwoorden = {
    "voorwerpen": ["telefoon", "sleutel", "sjaal", "zonnebril", "muts", "revolver"],
    "meubels": ["bank", "bureau", "kruk", "kast", "tafel", "dressoir","stoel","burostoel",""],
    "mensen": ["rudi","evert","henny","vriend", "familie", "collega", "leraar", "politieagent", "vader","ouders","dochter","zoon","verpleegkundige", "chirurg", "helpdeskmedewerker", "systeembeheerder"],
    "dieren": ["hond", "kat", "konijn", "vogel", "rups", "kikker", "slang","tijger","olifant","bij"],
    "voertuigen": ["fiets", "auto", "bus", "trein", "e-bike", "vrachtwagen", "brandweerauto"],
    "plaatsen": ["park", "strand", "supermarkt", "ziekenhuis", "bos", "pretpark", "concertzaal"],
    "gebouwen": ["kasteel", "museum", "restaurant", "hotel", "vliegveld", "theater"],
    "bomen": ["eik", "beuk", "den", "esdoorn", "kastanje", "wilg"],
    "planten": ["cactus", "orchidee", "tulp", "varen", "klimop", "monstera", "duizendknoop", "lavendel"]
}

lijdende_voorwerpen = {
    "voorwerpen": ["kabel", "oplader", "adapter", "toetsenbord", "speaker","computer","netwerkswitch"],
    "meubels": ["kussen", "plaid", "stoelkussen", "onderzetter", "schemerlamp"],
    "mensen": ["brief", "cadeau", "paraplu", "tas", "boek"],
    "dieren": ["bal", "speeltje", "riem", "voerbak", "halsband"],
    "voertuigen": ["helm", "stoelhoes", "sneeuwkettingen", "dakdragers", "fietsendrager"],
    "plaatsen": ["karretje", "tas", "parasol", "koelbox", "rugzak"],
    "gebouwen": ["menukaart", "servet", "wijnkaart", "asbak", "stoel"],
    "bomen": ["blad", "eikel", "dop", "tak", "boomstam","boomwortel"],
    "planten": ["bloem", "blad", "pot", "gieter", "kweekbak"]
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
    "voorwerpen": {"ligt": ["op", "onder", "tussen"], "verdwijnt": ["in"],"staat": ["op","onder","naast"],"glijdt": ["in","onder"]},
    "meubels": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "mensen": {"staat": ["in","op"], "verdwijnt": ["in"], "ligt": ["in"],"danst": ["in","op"],"vecht": ["in","op"]},
    "dieren": {"kijkt": ["naar"], "springt": ["op", "over"], "ligt": ["naast"], "loopt": ["richting","naar"]},
    "voertuigen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "plaatsen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "gebouwen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "bomen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "planten": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]}
}