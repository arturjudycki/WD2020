def zlicza_ilosc(** ilosc):
    suma = 0
    for i in ilosc.values():
        suma+=i
    print(suma)

zlicza_ilosc(jabłka=4, mleka=3, woda=2)