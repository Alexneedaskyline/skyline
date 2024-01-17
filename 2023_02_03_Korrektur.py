import random
zeichen = random.choice(["+", "#", "&", "%"])


import time 
startzeit = time.time()
antwort = input("was ist 17 * 17")
endzeit = time.time()
antwortdauer = endzeit - startzeit


import random 
def roulette():
    return random.randint(0, 36)


def negativ(zahl):
    if zahl < 0:
        return True 
    else:
        return False
    

def listen_vergleich(liste1, liste2, index1, index2):
    if [liste1[index1] == liste2(index2)]:
        return True
    else:
        return False