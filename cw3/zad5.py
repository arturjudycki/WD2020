def rown_prost(a1,a2):
    if a1 == a2:
        return "Proste sa równoległe"
    elif a1*a2 == -1:
        return "Proste sa prostopadłe"
    else:
        return "Proste nie są ani równoległe ani prostopadłe"

print(rown_prost(1,1))
print(rown_prost(2,-1/2))
print(rown_prost(1,2))