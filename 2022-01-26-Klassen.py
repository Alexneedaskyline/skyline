class Buch:
    def __intit__(self, titel: str, genre: str, seiten, jahr: int, bebildert: bool):
        self.titel = titel
        self.genre = genre 
        self.seiten = seiten
        self.jahr = jahr
        self.bebildert = bebildert
 
    def __str__(self) -> str: 
        return "Titel: " + self.titel + " aus dem Jahr " + str(self.jahr)

buch1 = Buch("Zweiter Weltkrieg", "Erzählung", 187, 1945, True)
print(buch1)

buch2 = Buch("Gründe warum danil nicht cool ist", "Erzählung", 3000, 2008, True)
print(buch2)
buch3 = Buch("Warum Fortnite für kinder ist"), "Erzählung", 100, 2022, True)
print(buch3)
class Bibliothek:
    def __init__(self, name: str, adresse:str, baujahr: int, bestand: list):
        self.name = name
        self.adresse = adresse
        self.baujahr = baujahr
        self.bestand = bestand

def buch_aufnehmen(self, buch: Buch) -> None:
    self.bestand.append(buch)

def bestandsgröße(self)
    return len(self.bestand)

def gesamtseiten(self): 
    ergebnis = 0
    for buch in self.bestand:
        buch.seiten
    return ergebnis

def längstes_buch(self) -> Buch:
    if self.bestandsgröße() == 0
        raise ValueError("Buchbestand leer")
    ergebnis = self.bestand[0]
    for buch in self.bestand:
        if buch.seiten > ergebnis.seiten:
            ergebnis = buch
    return ergebnis

def kürzestes_buch(self) -> Buch:
    if self.bestandsgröße() == 0
        raise ValueError("Buchbestand leer")
    ergebnis = self.bestand[0]
    for buch in self.bestand:
        if buch.seiten > ergebnis.seiten:
            ergebnis = buch
    return ergebnis

def durchschnittliche_buchlänge(self) -> float:
    return self.gesamtseiten() == 0
            raise ValueError("Buchbestand leer")
        ergebnis = self.bestand[0]
    for buch in self.bestand:
        if buch.seiten > ergebnis.seiten:
        ergebnis = buch
    return ergebnis
        
     
def anzeil_bebildert(self) -> Buch:
    if self.bestandsgröße() == 0 
            raise ValueError("Buchbestand leer")
        anzahl_bebildert = 0
    for buch in self.bestand:
        if buch.bebildert == True 
        anzahl_bebildert += 1
    return anzahl_bebildert / self.bestandsgröße()
    def 
                                













def suche(self, anfangsjahr: int, end jahr: int): 
ergebnis = []
for buch in self.bestand:
if buch.jahr >= anfangsjahr and buch.jahr <= endjahr: and ??? in ??? 
ergebnis.append(buch)   

bib1 = Bibliothek("Bayrische Staatbibliothek", "Ludwigstraße 16", 1843, [buch1, buch2, buch3])
buch4 = Buch("Die sieben Samurai", "Action", 567, 2022, True)
print(bib1.bestandgröße())
print(bib1.gesamtseiten())
print(bib1.suche(1900, 1990, ["Erzählung"]))

def buch_entfernen(self, titel: str)
    for buch in 


def bücher_aufsteigend_nach_jahr_sortiert(self) -> bool
    for i in range(len(self.bestand)):
        if self.bestand[i].jahr > self.bestand[i + 1].jahr:
            return False 




