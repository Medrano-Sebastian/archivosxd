# Integrantes
### Medrano Alania, Sebastian Rodrigo (20211821)
### Rojas Melgarejo, Jairo Gonzalo    (20211829)
### Palacios Arias, Mattihus          (20170119)


# Función para determinar si una matriz es cuadrado latino o no

def latino(L):
  D = []
  n = 0
  U = []
  while n < len(L):
    D = []
    for i in range(len(L)):
      D.append(L[i].index(L[0][n]))
    if len(set(D)) == len(L):
      U.append("T")
    else:
      U.append("F")
    n += 1
  if len(set(U)) == 1:
    return "Sí es cuadrado latino"
  else:
    return "No es cuadrado latino"


# Función para generar un cuadrado latino de orden n

def cuadradolatino(n):
 a=[]
 import random
 for b in range(n):
  c=random.randint(1,100)
  a.append(c)

 M = []
 i = 0
 while i < len(a):
    M.append(a[i:]+a[:i])
    i +=1
 print(M)



