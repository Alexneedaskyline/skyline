import random
zufallszahl = random.randint(1, 100)


eingabezahl = input("Bitte gib eine Zahl ein: ")


eingabezahl_int = int(eingabezahl)
if zufallszahl == eingabezahl_int:
    print("Gleich")
else:
    print("Ungleich")

    