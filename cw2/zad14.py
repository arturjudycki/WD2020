from math import *
liczba=input("Podaj liczbe\n")
liczba=int(liczba)
try:
    wynik=sqrt(liczba)
    print(str(wynik))
except ValueError:
    print("Nie można obliczyć pierwiastka z liczby ujemnej")