def alle_elemente_ausgabe(liste):
    i = 0
    while i < len(liste):
        print(liste[i])
        i = i + 1


def alle_elemente_positiv(liste):
    i = 0
    while i < len (liste):
        if liste(i) > 0:
            print(liste[i])
        i = i + 1


def einhundert():
    print(100)
    einhundert()


def einhundert_n(n):
    if n == 0:
        return
    print(100)
    einhundert_n(n + 1)