slownik = {"mleko": "litry", "mąka": "kg", "jajka": "sztuki", "banany": "sztuki"}

#slownik2 = [x for x in slownik if "sztuki" in slownik.values()]
#print(slownik)
#print(slownik2)

lista = [x for x in slownik if slownik[x] == "sztuki"]

print(lista)