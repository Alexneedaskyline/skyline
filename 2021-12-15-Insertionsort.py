liste_unsortiert = [5, 2, 4, 3]
liste_sortiert = []
print(liste_sortiert, liste_unsortiert)
while len(liste_unsortiert) > 0:
    entferntes_element = liste_unsortiert.pop(0)
    position = 0
    while position < len(liste_sortiert) and entferntes_element > liste_sortiert[position]:
        position = position + 1
    liste_sortiert.insert(position, entferntes_element)
    print(liste_sortiert, liste_unsortiert)                 
