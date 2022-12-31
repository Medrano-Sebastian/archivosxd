#ejercicio 1
"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por 
pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

"""nombre= str(input("¿Cuál es tu nombre?\n"))
print(f"Hola {nombre}")
num1= int(input(f"{nombre} denos un numero entero positivo: "))
while num1<0:
    print("Ingrese valores positivos")
    num1= int(input(f"{nombre} denos un numero entero positivo"))
for i in range(1,num1+1):
    print(nombre)"""

#ejercicio 2
"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por
 pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas 
 las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario 
 puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
"""nombre= str(input("¿Cuál es tu nombre completo?\n"))
print(nombre.upper())
print(nombre.capitalize())
print(nombre.title())
"""

#ejercicio 3

"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
 muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
  número de letras que tienen el nombre.
"""
"""nombre=str(input("¿Cuál es tu nombre: "))
print(nombre.upper() + " tiene " + str(len(nombre)) +" letras")
"""
#ejercicio 4
"""x="saludos"
print(x[0]==x[-1])#compara el contenido
print(x[0] is x[-1])#compara el ID
"""




#For
"""
texto="Hola grupo"
for i in range(len(texto)):
    print(texto[i])

texto="Hola grupo"
for i in range(len(texto)):
    print(texto[i],end="")#organiza de manera horizontal el texto
"""
"""def potencia():
    limite = 1000000
    exponente = 0
    potencia_2 = 2**exponente
    while potencia_2 < limite:
        print('2 elevado a ' + str(exponente) +
              ' es igual a: ' + str(potencia_2))
        exponente = exponente + 1
        potencia_2 = 2**exponente

if __name__ == "__main__":
    potencia()
"""

""" 
while True:
    mes = input("Indique el mes de sus vacaciones: ")
    if mes:
        break     """
"""def pisos_juego():
    N = 100
    T = 1
    P = 60
    nro_piso = 1
    for i in range(1, N+1):
        t = random.random()
        y = random.randint(1,6)
        if t < 0.01:
            nro_piso = 1
        if y == 1 or y == 2:
            if nro_piso >= 2:
                nro_piso -= 1
        elif y == 3 or y == 4 or y == 5 :
            nro_piso += 1
        elif y==6 :
            y = random.randint(1,6)
            nro_piso += y
        if nro_piso == 60:
            break
        
    
    return nro_piso

pisos_juego()
"""





"""Problema 1:
Una empresa automotriz necesita un programa para manejar los montos de ventas de sus N sucursales, a lo largo de los últimos M años. 
El programa que necesitan los directores debe considerar lo siguiente:
•	Ingresar los datos de las ventas de las N sucursales en los M años.  Escribir una función que tenga como parámetros de entrada
    N y M llamada lectura, lea los valores de los montos y los retorne en una estructura de listas (4 puntos)
•	Determine de cada año la sucursal en el que se obtuvo más ventas. Escribir una función llamada mayorSucursalA que tenga como 
    parámetros de entrada una estructura de lista con los montos leídos (retorno de la función lectura) y retorne  una lista con las
    sucursales con mayor venta en cada año  (4 puntos) 
•	Determine  la sucursal y el año con mayor venta. Escribir una función llamada MAYOR que tenga como parámetros de entrada una estructura 
    de lista con los montos leídos (retorno de la función lectura) y devuelva una dupla (sucursal, año) que corresponda al mayor monto 
    ingresado. (4 puntos) 
Nota: No se tomará en cuenta si utiliza funciones internas de Python como: sum, max, min, etc o de alguna librería
"""
#from pickle import TRUE
#from re import T


N=int(input("Ingrese camtidad de sucursales: "))
M=int(input("Ultimos años a analizar: "))

def lectura(N,M):
    z=[]
    q=0
    for i in range(M):
        if q<M:
            z.append([])
        for u in range(N):
            montos=int(input("Ingresar venta totalde la sucursal: "))
            z[q].append(montos)
        q=q+1
    return z
z= lectura(N,M)

def mayorSucursalA(z):
    print(z)
    for i in range(len(z)):
        l=0
        q=z[i][l]
        print(q)
        for y in range(0,len(z[i])):
            f=0
            r=[]
            print(z)
            print(y,"",i)
            print(len(z[i]))
            print(z[i][y-1])
            for k in range(M):
                if f<M:
                    r.append([])
                    f=f+1
            if q<=z[i][y]:
                q=q
                r[i].append(z[i][y])
            else:
                r[i].append(q)
                q=z[i][l+1]
    print(r)

mayorSucursalA(z)



        

            




