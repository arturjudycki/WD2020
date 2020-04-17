import random

macierz = [[0]*4 for i in range(4)]

print(macierz)

for i in range(4):
    for j in range(4):
        macierz[i][j] = random.randint(0,9)

print(macierz)