import random
import time


def calcOccProf(tableau):
    for i in range(10):
        occ = 0
        for val in tableau:
            if val == i:
                occ += 1
        print(f"La valeur {i} apparait {occ} fois.")


def calcOccDavid(tableau):
    occ = [0] * 10
    for val in tableau:
        occ[val] += 1
    for i in range(10):
        print(f'La valeur {i} apparait {occ[i]} fois.')


liste_aleatoire = [random.randint(0, 9) for _ in range(1000000)]

startProf = time.time()
calcOccProf(liste_aleatoire)
endProf = time.time()
tempsP = (endProf - startProf) * 1000
print(f"La solution du prof a pris {tempsP}ms\n")

startDavid = time.time()
calcOccDavid(liste_aleatoire)
endDavid = time.time()
tempsD = (endDavid - startDavid) * 1000
print(f"La solution de David a pris {tempsD}ms")
