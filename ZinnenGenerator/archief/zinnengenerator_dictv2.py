# De thema's en combinaties die logisch zijn
themas = {
    "voorwerpen": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "meubels": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "mensen": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "dieren": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "voertuigen": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "plaatsen": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "gebouwen": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "bomen": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
    "planten": ["meubels", "mensen", "dieren", "voertuigen", "plaatsen", "gebouwen", "bomen", "planten"],
}

zelfstandige_naamwoorden = {
    "voorwerpen": ["telefoon", "sleutel", "sjaal", "zonnebril", "muts", "revolver"],
    "meubels": ["bank", "bureau", "kruk", "kast", "tafel", "dressoir"],
    "mensen": ["vriend", "familie", "collega", "leraar", "politieagent", "verpleegkundige", "chirurg", "helpdeskmedewerker", "systeembeheerder"],
    "dieren": ["hond", "kat", "konijn", "vogel", "rups", "kikker", "slang"],
    "voertuigen": ["fiets", "auto", "bus", "trein", "e-bike", "vrachtwagen", "brandweerauto"],
    "plaatsen": ["park", "strand", "supermarkt", "ziekenhuis", "bos"],
    "gebouwen": ["kasteel", "museum", "restaurant", "hotel", "vliegveld"],
    "bomen": ["eik", "beuk", "den", "esdoorn", "kastanje"],
    "planten": ["cactus", "orchidee", "tulp", "varen", "klimop", "monstera", "duizendknoop"]
}

lijdende_voorwerpen = {
    "voorwerpen": ["kabel", "oplader", "adapter", "toetsenbord"],
    "meubels": ["kussen", "plaid", "stoelkussen", "onderzetter"],
    "mensen": ["brief", "cadeau", "paraplu", "tas"],
    "dieren": ["bal", "speeltje", "riem", "voerbak"],
    "voertuigen": ["helm", "stoelhoes", "sneeuwkettingen", "dakdragers"],
    "plaatsen": ["karretje", "tas", "parasol", "koelbox"],
    "gebouwen": ["menukaart", "servet", "wijnkaart", "asbak"],
    "bomen": ["blad", "eikel", "dop", "tak"],
    "planten": ["bloem", "blad", "pot", "gieter"]
}

bijvoeglijke_naamwoorden = {
    "voorwerpen": ["roze", "glanzende", "oude", "duurzame"],
    "meubels": ["comfortabele", "moderne", "klassieke", "verstelbare", "lelijke"],
    "mensen": ["sympathieke", "slimme", "grappige", "aardige"],
    "dieren": ["schattige", "speelse", "lieve", "trouwe"],
    "voertuigen": ["snelle", "efficiënte", "ruime", "luxueuze", "elektrische"],
    "plaatsen": ["drukke", "schone", "gezellige", "veilige"],
    "gebouwen": ["romantische", "chique", "historische", "unieke"],
    "bomen": ["grote", "oude", "mooie", "geurende"],
    "planten": ["groene", "bonte", "gezonde", "kleurrijke", "geurige"]
}

#Werkwoorden in enkelvoudige persoonsvorm in de vorm Hij/Zij/Het met bijpassen voorzetsels.
werkwoorden = {
    "voorwerpen": {"ligt": ["op", "onder", "tussen"], "verdwijnt": ["in"]},
    "meubels": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "mensen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "dieren": {"kijkt": ["naar"], "springt": ["op", "over"], "ligt": ["naast"], "loopt": ["richting"]},
    "voertuigen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "plaatsen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "gebouwen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "bomen": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]},
    "planten": {"staat": ["in"], "verdwijnt": ["in"], "ligt": ["in"]}
}