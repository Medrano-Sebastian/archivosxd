##programa para eliminra una lista
"""a=[1,2,3,4,5,56,3,2]
e =int(input("ingresar elemento a eliminar: "))

for i in range(len(a)):
    if a[i]==e:
        del(a[i])
        print(a)


## Programa para eliminar un elemento de una lista

B = [5,6,7,8,9]
print(B)
A = []
e = int(input('Ingresar el elemento a eliminar de la lista: '))

for i in range(len(B)):
    if B[i]!=e:
        A.append(B[i])
    else:
        print('Se elimina', e)
    i += 1
print(A)"""


def misterio(x,y):
    if x == 0:
        return y 
    return misterio(x-1,y+1)
misterio(5,2)




"""
i=0

while i<len(a):
    if a[i]==e:
        del(a[i])
    

    i=i+1
print(a)

A = [8,7,6,7,9]
e = int(input("ingrese elemento eliminar"))
s = 0
while True:
    if A[s] == e:
        del(A[s])
        s-=1
    s+=1
    if s == len(A):
        break   
print(A)
"""
#DICCIONARIOS
D={10:14.45,"10":34,"h":23,15.67:{1:2,3:4,5:6}}
print(type(D))
print(D.keys())
print(D.values())
print(D["h"])#extraer valores con un key(ejemplo "h")

for elemento in D:
    print(elemento)#imprime keys
print("-----------------")

for clave in D:
    print(D[clave])#inprime valores
print(clave,"->", D[clave])
print("--------------------------------------")


for x,y in D.items():#imprime el key con su valor
    print(x,y)

print(D.items())#devuelve cada key con su respectivo value 
print("--------------------------------------")

D.pop("10")#elimina
print(D)

E=D.copy()
print(id(E))

print(id(D))

#Clase 26/07/2022
"""def cuadradoA(numero):
    print(numero**2) #no se puede utilizar para operar ya que no pertenece a algun tipo
def cuadradoB(numero):
    return(numero**2)#aca si se puede
cuadradoA(23)
print(type(cuadradoA(23)))
cuadradoB(23)
print(type(cuadradoB(23)))
"""
"""
def potencia(x,y):
  f = 1
  i = 1
  if y == 0:
    return 1
  else:
    while i<=y :
      f = f*x
      i += 1
    return f
"""