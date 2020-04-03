import sys
print('Podaj pierwszą wartość: ')
w1=sys.stdin.readline()
print('Podaj drugą wartość: ')
w2=sys.stdin.readline()
w1=int(w1)
w2=int(w2)
w=w1*w2
sys.stdout.write(str(w))