class Mensch:
    def __init__(self, name: str, gewicht: int, herkunftsland: str, augenfarbe: str, haarfarbe: str, hautfarbe: str, größe: float, geschlecht: str, gesprochene_sprachen: str, religion: str, alter: int):
        self.name = name
        self.gewicht = gewicht
        self.herkunftsland = herkunftsland 
        self.augenfarbe = augenfarbe
        self.haarfarbe = haarfarbe
        self.hautfarbe = hautfarbe
        self.größe = größe
        self.geschlecht = geschlecht
        self.gesprochene_sprache = gesprochene_sprachen
        self.religion = religion
        self.alter = alter 

    def __str__(self):
        return "ich bin  ein Mensch, heiße " + self.name + ", wiege " + str(self.gewicht) + " kg und komme aus " + self.herkunftsland 

mensch1 = Mensch("Xin", 180, "Frankreich", "grün-blau", "rot", "schwarz", 1.98, "divers", ["französisch", "latein", "russisch"], "Islam", 88)

print(mensch1)