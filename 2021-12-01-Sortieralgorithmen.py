import time 
import random


zufallsliste = []


liste = zufallsliste 

anfang = time.time()
liste_sortiert = []

durchlauf = len(liste):
while durchlauf = 0  

durchlauf = durchlauf -1
time.time




#liste = [7, 4, 5, 8, 3]
#liste_sortiert = []
 
#durchlauf = len(liste)
#while durchlauf > 0:

 #min = liste[0]
 #index = 0
 #while index < len (liste):
        #if liste[index] < min:
            #min = liste[index]
        #index = index + 1

    #liste.remove(min)
    #liste_sortiert.append(min)

    #durchlauf = durchlauf + 1

    #print(liste_sortiert)

#x = 5
#y = 10
#t = x
#x = y
#y = t

#print(x)
#print(y)


#x = 5
#y = 10
#z = 15
#t = x
#r = y
#x = z
#y = t
#z = r

#print(x)
#print(y)
#print(z)

liste = ["Flugzeug", "Rakete", "Mond", "Buch", "Kalender"]
index0 = 0
while index0 < len(liste):
    index = 0
    while index < len(liste) - 1:
        if liste[index] > liste[index + 1]:
            speicher = liste[index]
            liste[index] = liste[index + 1]
            liste[index + 1] = speicher 
        index += 1
    index0 += 1


print(liste)
        