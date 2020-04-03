liczba=input('Podaj liczbe:\n')
liczba=int(liczba)
while(liczba>=10):
    liczba = input('Podaj liczbe:\n')
    liczba = int(liczba)
else:
    print('Odpowiednia wysokosc wieży')

for i in range(1, liczba+1):
        print(i * '#')