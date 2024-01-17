# Schreibe eine Funktion namens funktion1, die einen einzigen Parameter namens parameter1 besitzt.
# TODO
def funktion1(parameter1):
    pass

# Schreibe eine Funktion namens begrüßung, die einen einzigen Parameter namens grußformel besitzt.
def begrüßung(grußformel):
    pass

# Schreibe eine Funktion namens produkt_vorbereitung, die zwei Parameter namens zahl1 und zahl2 besitzt.
def produkt_vorbereitung(zahl1, zahl2):
    pass

# Schreibe eine Funktion namens hallo, die keinen Parameter besitzt und "Hallo" ausgibt.
# TODO
def hallo():
    print("hallo")
# Schreibe eine Funktion namens doppeltes, die einen einzigen Parameter namens zahl besitzt und das Doppelte von zahl ausgibt.
# TODO
def doppeltes(zahl):
    print(zahl * 2)
# Schreibe eine Funktion namens summe, die zwei Parameter namens zahl1 und zahl2 besitzt und die Summe dieser Zahlen ausgibt.
# TODO

# Schreibe eine Funktion namens differenz, die zwei Parameter namens zahl1 und zahl2 besitzt und die Differenz dieser Zahlen ausgibt.
# TODO

# Schreibe eine Funktion namens produkt, die zwei Parameter namens zahl1 und zahl2 besitzt und das Produkt dieser Zahlen ausgibt.
# TODO

# Schreibe eine Funktion namens positiv, die einen einzigen Parameter namens zahl besitzt und "Positiv" ausgibt, falls zahl größer 0 ist, ansonsten "Nicht positiv".
# TODO

# Schreibe eine Funktion namens größer, die zwei Parameter namens zahl1 und zahl2 besitzt und 1 ausgibt, falls zahl1 größer ist als zahl2, ansonsten 2.
# TODO

# Schreibe eine Funktion namens größere, die zwei Parameter namens zahl1 und zahl2 besitzt und die größere von beiden Zahlen ausgibt.
# TODO

# Schreibe eine Funktion namens größte, die drei Parameter namens zahl1, zahl2 und zahl3 besitzt und die größte unter ihnen ausgibt.
# TODO
def größte(zahl1, zahl2, zahl3):
    if zahl1 > zahl2 and zahl2 > zahl3:
        print (zahl1)
    elif zahl2 > zahl1 and zahl2 > zahl3:
        print(zahl2)
    else:
        print(zahl3)
# Schreibe eine Funtion namens quadratOderMal10, die einen einzigen Parameter namens zahl besitzt und das größere aus dessen Quadrat und dessen Zehnfachem ausgibt.

def quadratOderMal10(zahl):
    if zahl * zahl > zahl * 10:
        print(zahl * zahl)
    else:
        print(zahl * 10)

# Schreibe eine Funktion namens summe_oder_differenz, die zwei Parameter namens zahl1 und zahl2 besitzt und das größere aus dessen Summe und dessen Differenz ausgibt.
def summe_oder_differenz(zahl1, zahl2):
    if zahl1 + zahl2 > zahl1 - zahl2:
        print(zahl1 + zahl2)
    else:
        print(zahl1 - zahl2)