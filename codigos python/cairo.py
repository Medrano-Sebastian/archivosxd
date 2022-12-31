#ejerccio de yt
"""
import datetime
ahora =datetime.datetime.now()
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
"""
#AREA DE UN CIRCULO
"""a=float(input("¿Cuál es el radio del circulo?: \n"))
area= 3.14*(a)**2
print("el área del circulo es : ",area)
"""
#representación inversa de una cadena
"""a='python'
for i in range(len(a)-1,-1,-1):
    print(a[i],end='')
print()
print(a[::1])#leer representacion inversa
"""
#Obtener un Conjunto de Números Seperados por Coma y Crear una Lista
"""entrada=input("escriba varios numeros separados por comas: ")
print(type(entrada))
numeros =entrada.split(',')
print(numeros)
print(type(numeros))
"""
#Obtener el Nombre de Extensión de un Nombre de Archivo
nombre_archivo=input("Ingrese el nombre de la extension del archivo: ")
nombre_archivo_partes=nombre_archivo.split('.')
print(nombre_archivo_partes)
print(nombre_archivo_partes[-1])
