print('PROGRAMA PARA LOCALIZAR NÚMEROS PRIMOS EN UNA LISTA')
print('--------------------------------------------------')
def primo(i):
  B = []
  for j in range(1,i+1):
    if i%j == 0:
      B.append(j)
  if len(B) == 2:
    return True
  else:
    return False

A = []
z = 1
cantidad = int(input("Ingrese la cantidad de números: "))
for n in range(cantidad):
  elemento = int(input(f"{z}. Ingrese un número: "))
  A.append(elemento)
  z += 1
B = []
C = []
for m in A:
  B.append(primo(m))
for q in range(cantidad):
  if B[q] == True:
    C.append(A[q])
if len(C) == 0:
  print('Ningún número es primo')
else:
  print('Los números primos son:',C)
a=sum(C)/len(C)
print("El valor promedio de los numeros primos es: ",a)
print('--------------------------------------------------')