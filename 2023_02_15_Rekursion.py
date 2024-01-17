#Schreibe eine Funktion namens hallo, die "unendlich" oft "hallo" ausgibt
# Verwende keine Schleifen 
#def hallo():
    #print("hallo")
   # hallo()
#hallo()
#Schreibe eine Funktion namens hallo_n, dei einen Parameter n besitzt und n Mal "Hallo" ausgibt


#def hallo_n(n):
 #   if n <= 0:
   #     return
  #  print("hallo")
    #hallo_n(n - 1) 

#Schreibe eine Funktion namens n_bis_1_ausgabe, die einen Parameter n besitzt und alle Zahlen von n bis 1 ausgibt(von groß nach klein)

#def n_bis_1_ausgabe(n):
   # if n <= 0:
  #      return
 #   print(n)
#n_bis_1_ausgabe(n - 1)

#Schreibe eine Funktion namens eins_bis_n_ausgabe, die einen Parameter n besitzt und alle Zahlen von 1 bis  n ausgibt (von klein nach groß).

#def eins_bis_n_ausgabe(n):
    #if n <= 0:
  #      return
   # eins_bis_n_ausgabe(n - 1)
 #   print(n)



#Schreibe eine Funktion, namens m_bis_n_ausgabe, die zwei Parameter m bis n besitzt und alle Zahlen von n bis m ausgibt (von klein nach groß)
#TODO
#def n_bis_m_ausgabe(n, m):
#    if n > m:
   #     return
  #  print(n)
 #   n_bis_m_ausgabe(m , n - 1)
#n_bis_m_ausgabe
# Schreine eine Funktion namens m_bis_n_ausgabe, die zwei Parameter m und n besitzt und alle Zahlen von m bis n ausgibt (von groß nach klein) 
#TODO
#def m_bis_n_ausgabe(m, n):
#    if n > m:
#        return
#    print(n)
#    m_bis_n_ausgabe(m, n + 1)
#m_bis_n_ausgabe
#Schreibe eine Funktion namens n_zufallszahlen_ausgabe, die einen Parameter n besitzt und n Zufallszahlen zwischen 1 und 100 ausgib
#TODO
#import random
#def n_zufallszahlen_ausgabe(n):
    #if n <= 0:
 #   return
#    zufallszahl = random.choice(1, 100)
 #
#   print(zufallszahl)
  #  n_zufallszahlen_ausgabe(n - 1)
#n_z#ufallszahlen_ausgabe(200)

#Schreibe eine Funktion namens zwei_hoch, die einen Parameter n besitzt und die n`te Potenz von 2 zurückgibt (ohne **).
#TODO
def zwei_hoch(n):
    if n == 0:
        return 1
    vorgängerergebnis = zwei_hoch(n - 1)
    ergebnis = vorgängerergebnis * 2 
    return ergebnis
print(zwei_hoch(5))



#Schreibe eine Funktion namens m_mal_n, die zwei Parameter m und n besitzt und m mal n zurückgibt (ohne * )
def m_mal_n(m, n):
    if n == 0:
        return 1
    vorgängerergebnis = m_mal_n(n, m - 1)
    ergebnis = vorgängerergebnis * 2
    return ergebnis 
print(m_mal_n(5))   

#Schreibe eine Funktion Fibonacci, die einen Parameter n besitzt und über die "n" te Fibonaccizahl zurückgibt.
#Die 0` te Fibonaccizahl ist 0, die 
fib_1 = 0
fib_2 = 1
fib_3 = 1
fib_4 = 2
fib_5 = 3
fib_6 = 5
fib_7 = 8

fib_3 = fib_2 + fib_1 
fib_4 = fib_3 + fib_2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1  
    fibonacci_n = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_n 

print(fibonacci(1))
#Schreibe eine Funktion liste_n_1, die einen Parameter n besitzt und eine Liste mit n Mal der Zahl 1 zurückgibt.




#Schreibe eine Funktion namens m_hoch_n, die zwei Parameter m und n besitzt und n hoch n zurückgibt (ohne **).

def m_hoch_n(m, n):
    if n <= 0:
        return 1
    vorgängerergebnis = m_hoch_n(n, n - 1)
    ergebnis = vorgängerergebnis * n
    return ergebnis


#Schreibe eine Funktion namens m_mal_n, die zwei Parameter m und n besitzt und m mal n zurückgibt 
def m_mal_n(n, m):
    if n <= 0:
        return 0 











print/print/print/print/print/print/print/print/print/print/print/print             
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print 
print/print/print/print/print/print/print/print/print/print/print/print  
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print
print/print/print/print/print/print/print/print/print/print/print/print
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111           
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111









#Schreibe eine Funktion liste_n_2, die einen Parameter n besitzt und eine Liste mit n Mal der Zahl 1 zurückgibt.
def liste_n_1(n):
    if n == 0:
        return []
    vorgängerergebnis = liste_n_1(n - 1)
    vorgängerergebnis.append(1)
    return vorgängerergebnis


import random

def liste_n_zufallszahlen(n):
    if n == 0:
        return []
    vorgängerergebnis = liste_n_zufallszahlen(n - 1)
    vorgängerergebnis.append(random.randint(1, 100))
    return vorgängerergebnis

#Schreibe eine Funktion liste_1_bis_n, die einen Parameter n besitzt und eine Liste aller Zahlen von 1 bis n zurückgibt.
def liste_1_bis_n(n):
    if n == 0:
        return []
    vorgängerergebnis = liste_1_bis_n(n - 1)
    vorgängerergebnis.append(n)
    return vorgängerergebnis

#Schreibe eine Funktion liste_n_bis_1, die einen Parameter n besitzt und eine liste aller Zahlen von n bis 1 zurückgibt.
def liste_n_bis_1(n):
    if n == 0:
        return []
    vorgängerergebnis = liste_n_bis_1(n - 1)
    vorgängerergebnis.append(0, n)
    return vorgängerergebnis

# Schreibe eine Funktion potenzenliste, die einen Parameter n besitzt und eine Liste mit den ersten n Zweierpotenzen zurückgibt.
# für n = S soll beispielsweise (1, 2, 4, 8, 16) zurückgegeben werden.

def potenzenliste(n):
    if n == 0:
        return []
    vorgängerergebnis = potenzenliste(n - 1)
    vorgängerergebnis.append(2 ** n)
    return vorgängerergebnis

# Schreibe eine Funktion fakulitätenliste, die einen Parameter n besitzt und eine Liste mit den ersten n Fakulitäten zurückgibt.
# Für n = S soll beispielsweise (1, 2, 6, 24, 120) zurückgegeben werden.
def fakultätenliste(n):
    if n == 0:
        return []
    if n == 1:
        return[1]
    vorgängerergebnis = fakultätenliste(n - 1)
    vorgängerergebnis.append(vorgängerergebnis[len(vorgängerergebnis) - 1] * n)
    return vorgängerergebnis




























