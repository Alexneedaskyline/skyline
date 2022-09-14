def erster_A (wort):
    if wort[0] == "A":
        print("ja")
    else:
        print("Nein")


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