try:
    liczba=input("Podaj liczbe\n")
    liczba=int(liczba)
    print(str(liczba))
except ValueError:
    print("Podałes literę zamiast liczby")