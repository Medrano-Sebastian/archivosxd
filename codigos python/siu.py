"""#Se importa la libreria turtle
import turtle
#Se estaclece los colores en una lista 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
#establece a la varible t todos los atributos de un lapiz
t = turtle.Pen()
#Cambia el color del fondo de la pantalla negro
turtle.bgcolor('black')

for x in range(181):#itera  el valor del rango del 0 al 180
    t.pencolor(colors[x%6])#establece los colores a utilizar
    t.width(x//100 + 2)#determina el grosor del lápiz 
    t.forward(x)#Da la orden de avanzar
    t.left(59)#Indica el ángulo en la q se desplazara hacia la izquierda
    
texto =str(input(""))"""

def es_primo(num):
    if num < 2:
        return False        
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

i = 1
f = [] #Inicializamos una LISTA VACÍA

primos=[]

#Entrada
print("Ingrese Número de elementos a Ingresar: ")
numElementos = int( input())

while i<= numElementos:
    elemento=int(input("Ingrese un elemento: "))
    f.append(elemento)
    i=i+1
print(f)

for i in f: 
    if es_primo(i):
        primos.append(i)
print(primos)

