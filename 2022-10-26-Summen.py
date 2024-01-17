import random

######################
##### Aufgabe 01 #####
# ######################
# # Berechne die Summe aller Zahlen von 1 bis 10.
# summe01 = 0
# # TODO
# print(summe01) # 55
# summe01 = 0
# summe01 += 1
# summe01 += 2
# summe01 += 3
# summe01 += 4
# summe01 += 5
# summe01 += 6
# summe01 += 7
# summe01 += 8
# summe01 += 9
# summe01 += 10
# print(summe01)
# ######################
##### Aufgabe 02 #####
######################
# Berechne die Summe aller Zahlen von 1 bis 100.

##### Aufgabe 03 #####
######################
# # Berechne die Summe aller Zahlen von -125 bis 25.
# summe03 = 0
# # TODO
# print(summe03) # -7550
# summe03 = 0
# i = -125
# while i <= 25:
#     summe03 += i
#     i += 1
# print(summe03)
# ######################
# ##### Aufgabe 04 #####
# ######################
# # Berechne die Summe aller geraden Zahlen von 190 bis 260.
# summe04 = 0
# # TODO
# print(summe04) # 8100
# summe04 = 0
# i = 190
# while i <= 25:
#     summe04 += i 
#     i += 2
# print(summe04)
######################
##### Aufgabe 05 #####
######################
# Berechne die Summe aller 2er-Potenzen von 1 bis 8192 (1 2 4 8 ... 4096 8192).
summe05 = 0
# TODO
print(summe05) # 16383
summe05 = 0
i = 190
while i <= 25:
    summe05 += i
    i *= 2 
######################
##### Aufgabe 06 #####
######################
# Berechne die Summe aller Quadratzahlen von 0 bis 625 (0 1 4 9 ... 576 625).
summe06 = 0
# TODO
print(summe06) # 5525

######################
##### Aufgabe 07 #####
######################
# Berechne die Summe aller Zahlen von -33 bis 66.
summe07 = 0
# TODO
print(summe07) # 1650

######################
##### Aufgabe 08 #####
######################
# Berechne die Summe aller durch 5 teilbaren Zahlen von 115 bis 775.
summe08 = 0
# TODO
print(summe08) # 59185
summe08 = 0
i = 115
while i <= 775:
    summe08 += i
    i += 5
print(summe08)
######################
#### Aufgabe 09 #####
######################
# Generiere 100 Zufallszahlen zwischen 1 und 250 und berechne deren Summe.
summe09 = 0
# TODO
print(summe09)
summe09

######################
##### Aufgabe 10 #####
######################
# Erstelle eine Liste zufallsliste, die 1000 zufällige Zahlen zwischen 1 und 1000 enthält.
zufallsliste = []
i = 1
while i <= 1000:
    zufallszahl = random.randint(1, 1000)
    zufallsliste.append(zufallszahl)
    i += 1
# print(zufallsliste)

######################
##### Aufgabe 11 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste.
summe11 = 0
i = 0
while i < len(zufallsliste):
    summe11 = summe11 + zufallsliste[i]
    i += 1
print(summe11)
######################
##### Aufgabe 12 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, deren Position gerade ist.
summe12 = 0
i = 0
while i < len(zufallsliste):
    summe11 = summe11 + zufallsliste[i]
    i = 1 + 2  
print(summe12)

######################
##### Aufgabe 13 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, deren Position durch 8 teilbar ist.
summe13 = 0
i = 0
while i < len(zufallsliste):
    summe13 = summe13 + zufallsliste[i]
    i = i + 8
######################
##### Aufgabe 14 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, deren Position durch 2 sowie durch 5 teilbar ist.
summe14 = 0
# TODO

######################
##### Aufgabe 15 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die größer als 500 sind.
summe15 = 0
# TODO

######################
##### Aufgabe 16 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die größer als 500 sind.
summe16 = 0
# TODO

######################
##### Aufgabe 17 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die kleiner als 135 sind.
summe17 = 0
# TODO

######################
##### Aufgabe 18 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die größer als 250 aber kleiner als 750 sind.
summe18 = 0
# TODO

######################
##### Aufgabe 19 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die größer als die erste Zahl in zufallsliste sind.
summe19 = 0
# TODO

######################
##### Aufgabe 20 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die größer als ihr Vorgänger sind (Position 0 wird übersprungen).
summe20 = 0
# TODO

######################
##### Aufgabe 21 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, deren Position eine Zweierpotenz ist.
summe21 = 0
# TODO

######################
##### Aufgabe 22 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, deren Position eine Quadratzahl ist.
summe22 = 0
# TODO

######################
##### Aufgabe 23 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, deren Position eine Fibonacci-Zahl ist.
summe23 = 0
# TODO

######################
##### Aufgabe 24 #####
######################
# Berechne die Summe aller Zahlen in zufallsliste, die gleich ihrer Position sind.
summe24 = 0
# TODO

######################
##### Aufgabe 25 #####
######################
# Sei zahl1 die erste Zahl in zufallsliste.
# Berechne die Summe aller Zahlen in zufallsliste, deren Position zwischen 0 und zahl1 liegt.
summe25 = 0
# TODO

######################
##### Aufgabe 26 #####
######################
# Gegeben sei folgenden Liste liste26 von Listen.
liste26 = [[1, 2, 3], [8, 0, 4], [5, 10, 9]]
# Berechne die Summe aller Zahlen in liste26.
summe26 = 0
# TODO

######################
##### Aufgabe 27 #####
######################
# Generiere eine zufällige Zahl anzahl_liste zwischen 1 und 10.
# Erstelle anschließend eine Liste liste27 von anzahl_liste vielen Listen mit 20 zufälligen Zahlen zwischen 1 und 100.
# Berechne nun die Summe aller Zahlen in liste27.
# TODO
summe27 = 0
# TODO