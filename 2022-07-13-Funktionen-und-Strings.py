s1 = "Hallo"
s2 = "abc123"
s3 = ""
s4 = "[$das"

def ausgabe_hallo():
    print("Hallo!")
ausgabe_hallo()

def ausgabe_wort(wort):
    print(wort)
ausgabe_wort("Ciao!")

def ausgabe_wort1_wort2(wort1, wort2):
    print(wort1, wort2)
ausgabe_wort1_wort2("Hallo", "Welt")

def erster_buchstabe(wort):
    print(wort[0])
erster_buchstabe("Strand")


def länge(wort):
    print(len(wort))
länge("Abendrot")

def letzter_buchstabe(wort):
    print(wort[len(wort) - 1])
letzter_buchstabe("Kiosk")
def erster_A(wort):

 def erster_A(wort):
    if wort[0] == "A":
        print("Ja")
    else:
        print("Nein!")
erster_A("Angel")
erster_A("Chor")   

def alles_klein(wort):
    print(wort.lower())
alles_klein("Ein Hochhaus")

def erste_gleich_zweiter(wort, buchstabe):
    if wort.lower()[0] == buchstabe.lower(): 
        print("Ja!")
    else:
        print("Nein!")
erste_gleich("Hafen", "H") 
erste_gleich("Mikrofon", "N")

def erster_A(wort):
    if wort[0] == "A":
        print("Ja!")
    else:
        print("Nein")

def kommt_vor(wort, buchstabe):
    enthalten = False
    index = 0
    while index < len(wort):
        if wort[index] == buchstabe:
            enthalten == False


def kommt_vor(wort, buchstabe):
    enthalten = False
    index = 0
    while index < len(wort):
        if wort[index] == buchstabe:
            enthalten = True
        index = index + 1
    if enthalten == True:
        print("Ja!")            
    else:
        print("Nein!")
kommt_vor("Noah", "h")
kommt_vor("Cedric", "e")


def anzahl(wort, buchstabe):
    anz = 0
    index = 0
    while index < len(wort):
        if wort[index] == buchstabe:
            anz = anz + 1 
        index = index + 1 
    print(anz)
anzahl("Welle", "l")
anzahl("Kornmühle", "s")

