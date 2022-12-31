#ejercicio 1
"""from operator import index
texto =str(input("excribe una frase: "))
n=0
for i in range(len(texto)):
    if texto[i]=="a":
        print("a",end="")#,end=""   :  para que las letras parescan juntas
    elif texto[i]=="e":
        print("e",end="")
    elif texto[i]=="i":
        print("i",end="")
    elif texto[i]=="o":
        print("o",end="")
    elif texto[i]=="u":
        print("u",end="")
    n=n+1
"""
from pickletools import uint2
"""
a=[]
e=[]
t=1
i=1
while i<=5:
    elemento=int(input("Intrdusca elemento: "))
    e.append(elemento)
    i=i+1
while t <= elemento:
        q=int(input("ingrese valor: "))
        print(a[t])
        t=t+1
else:
    a.append(elemento)
    print(a)

"""
#ctrl + L = selecion de una linea
#ctrl + x = borra una linea

i = 1
f = [] #Inicializamos una LISTA VACÍA
no_primos=[]
primos=[]

#Entrada
print("Ingrese Número de elementos a Ingresar: ")
numElementos = int( input())

while i<= numElementos:
    elemento=int(input("Ingrese un elemento: "))
    f.append(elemento)
    i=i+1
print(f)

z=0




for q in range(2,o):
        print("numero",q)
        if o%q==0:
            print("qso",o%q,"   ", q,"   ",q)
            print("lo que se remueve",o)
            if o  in f:
                print("lo que se remueve",o)
                f.remove(o)
        else:
            print("tmr",o)
        
            
print(f)

"""
lista = [3, 11, 6, 10, 97, 31, 2, 6, 14, 16, 17, 21, 199]

primos = []

def es_primo(num):
    if num < 2:
        return False        
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in f: 
    if es_primo(i):
        primos.append(i)
print(primos)





"""       

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
cantidad = int(input("Ingrese la cantidad de número: "))
for n in range(cantidad):
  elemento = int(input("Ingrese un elemento: "))
  A.append(elemento)
B = []
C = []
for m in A:
  B.append(primo(m))
for q in range(cantidad):
  if B[q] == True:
    C.append(A[q])

     




    

        
        
        











