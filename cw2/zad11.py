liczba=input('Podaj liczbe:\n')
liczba=int(liczba)
while(liczba<3 or liczba>9):
    liczba = input('Podaj liczbe:\n')
    liczba = int(liczba)
else:
    print('Odpowiednia liczba')

import sys

for i in [1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5]:
        if i==2:
            sys.stdout.write("H")
        else:
            if j in [1,5]:
                sys.stdout.write("H")
            else:
                sys.stdout.write(" ")
    sys.stdout.write("\n")

for i in range(1, liczba+1):
    for j in range(1,liczba+1):
        if i==(liczba+1)//2:
            sys.stdout.write("o")
        else:
            if j == 4:
                sys.stdout.write("o")
    sys.stdout.write("\n")