liczba=input("Podaj liczbę:\n")
liczba=int(liczba)
suma_cyfr=0
while(liczba!=0):
    suma_cyfr+=liczba%10
    liczba=liczba//10
else:
    print("Suma cyfr podanej liczby: " + str(suma_cyfr))