 from _typeshed import IdentityFunction
from os import X_OK


liste = [1, 2, 3, 4]
print(len(liste))
print(liste[-4])

liste = ["Auto", "Biene", "Katze", "Flasche"]
print(liste.index("Auto"))
print(liste.count("Elch"))
liste.reverse()
print(liste)

einkaufsliste = ["paprika", "Chips", "Mars", "Brot", "Nudeln", "Bananen", "Orangensaft"]
preisliste = [1.60, 1.50, 0.90, 1.00, 1.90, 3.49, 1.99]

index = 0
while index < len(einkaufsliste):
    print("wir kaufen " + einkaufsliste[index] + " für " + str(preisliste[index]) + "€")
    index = index + 1





höchster_preis = preisliste[0]
index = 0
while index < len(preisliste): 
    if höchster_preis < preisliste[index]:
        höchster_preis = preisliste[index]
    index = index + 1
print(höchster_preis)


index = 0
while index < len(preisliste):
    if niedrigster_preis > preisliste[index:]
        niedrigster_preis = preisliste[index]
    index = index + 1
print(niedrigster_preis)


index_teuerstes_produkt = 0
index = 0
while index <len(preisliste):
    if preisliste[index_teuerstes_produkt] < preisliste[index]:   
       index_teuerstes_produkt =
    index = index + 1
print(einkaufsliste[index_teuerstes_produkt])


index = index 
anzahl = 0 
while index < len(preisliste):
    if preisliste[index] < 2.00 and preisliste[index] > 1.00
        anzahl = anzahl + 1
    index = index + 1
print(summe) 


index = 0
summe = 0
while index 














einkaufsliste[0][0]











liste_sortiert = []



anzahl = len(preisliste)
while anzahl > 0
min = preisliste[0]
index = 0
while index < len(preisliste):
    if preisliste[index] < min:
        min = preisliste[index]
    index = index + 1
    preisliste.remove(min)
    liste_sortiert.append(min)
anzahl = anzahl - 1 
print(liste_sortiert)

produktliste.append("Wasser")
preisliste.append(1.29)

produktliste.append("Kekse")
preisliste.append(2.19)

produktliste.append("Äpfel")
preisliste.append(1.50)

liste = ["Pudding", "Snickers", "Ingwer"]
produkt = random.choice(liste)
einkaufsliste.append(produkt)
preis = random.uniform(0.50, 2.50) 
preisliste.append(preis)
print(einkaufsliste)
print(preisliste)


x = input("was willst du einkaufen? ")
t = float(input)("Zu welchem Preis? ")
einkaufsliste.append(x)
preisliste.append(t)
print(einkaufsliste)
print(preisliste)

















































































