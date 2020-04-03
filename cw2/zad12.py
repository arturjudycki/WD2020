import sys

for i in range(1,11):
    for j in range(1,11):
        w=i*j
        sys.stdout.write(str(w)+" ")
    sys.stdout.write("\n")