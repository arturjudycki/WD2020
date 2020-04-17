def mon_funkcji_lin(a):
    if a>0:
        x = "Funkcja jest rosnąca"
        return x
    elif a == 0:
        x2 = "Funkcja jest stała"
        return x2
    else:
        x3 = "Funkcja jest malejąca"
        return x3

print(mon_funkcji_lin(57))
print(mon_funkcji_lin(0))
print(mon_funkcji_lin(-8))