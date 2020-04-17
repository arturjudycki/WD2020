def iloczyn_ciagu(* liczby):
    iloczyn=1
    for i in liczby:
        iloczyn*=i
    return iloczyn

print("Iloczyn elementow ciagu: " + str(iloczyn_ciagu(2,3,5)))